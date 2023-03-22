import numpy as np
import time
import matplotlib.pyplot as plt
import nidaqmx #DAQ
from nidaqmx.constants import AcquisitionType #DAQ
import pyrebase #for data upload, download
#%%   
class Firebase():
    def __init__(self,JSONlocation ,DBfolder = 'Folder2'):
        self.DBfolder = DBfolder
        db_config = {
          "apiKey": "AIzaSyCJ7NBM2vTv71EM2AQMtfW3cXNnWiXvGBQ",
          "authDomain": "ntust-dal.firebaseapp.com",
          "databaseURL": "https://ntust-dal-default-rtdb.firebaseio.com/",
          "serviceAccount": JSONlocation,
          "projectId": "ntust-dal",
          "storageBucket": "ntust-dal.appspot.com",
          "messagingSenderId": "839926714277",
          "appId": "1:839926714277:web:f949cc304a2dd7948b224c",
          "measurementId": "G-0N1ZF71Q81"
        }
        self.db = pyrebase.initialize_app(db_config).database()
    def ReadForce(self,i):
        return self.db.child('Force').child(i).get().val()
    def ReadVolt(self,i):
        return self.db.child('Folder2').child(i).get().val()
    def upload(self,i, data):
        self.db.child('Folder2').child(i).set(data)
def autoscaleX(xmin, xmax):
    xmin += 5
    xmax += 5
    ax1.set_xlim(xmin, xmax)
    ax2.set_xlim(xmin, xmax)
    
def downsize(update_x,update_y):
    for i in range(5):
        update_x.pop(i)
        update_y.pop(i)
    return update_x, update_y
def DAQ():
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0",
                                            max_val = 0.5,
                                            min_val = -0.5,
                                            )
    # task.ai_channels.add_ai_voltage_chan("SimDev1/ai0",
    #                                         max_val = 0.5,
    #                                         min_val = -0.5,
    #                                         )
    task.timing.cfg_samp_clk_timing(4096,
                                        sample_mode = AcquisitionType.CONTINUOUS)
    data = task.read()
    #print(data)
    task.close()
    return data
#%%
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
#FB = Firebase()
F = Firebase(locat,DBfolder = 'Folder2')
plt.ion()
figure, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex = True,figsize=(8,6)) #unpack value 
line1, = ax1.plot([], [], lw=2, label = 'Sensor Voltage',color = 'blue')
line2, = ax2.plot([], [], lw=2, label = ' Force',color = 'red')
#plt.title("NTUST Program",fontsize=25)
#plt.axis([0,10,-2,2])
#plt.xlabel("time",fontsize=18)
#plt.ylabel("Sensor Voltage",fontsize=18)
#%%
ax1.set_xlim(0,10)
ax2.set_xlim(0,10)
ax1.set_ylim(-2,2)
ax2.set_ylim(-50,50)
ax1.set_xlabel('T (s)')
ax1.set_ylabel('Voltage (V)')
ax2.set_xlabel('T (s)')
ax2.set_ylabel('Force (N)')
ax1.set_title('NTUST program')

#%%   
update_x, update_y1,  update_y2 = np.array([]), np.array([]), np.array([])
for i in range(1000):
    update_x = np.append(update_x,i)
    new_y = DAQ()
    F.upload(i, new_y)
    update_y1 = np.append(update_y1, new_y)
    update_y2 = np.append(update_y2, F.ReadForce(i))
    xmin, xmax = ax1.get_xlim()
    if i >= xmax:
        autoscaleX(xmin, xmax)
        #update_x,update_y1 = downsize(update_x,update_y1)
    line1.set_data(update_x, update_y1)
    line2.set_data(update_x, update_y2)
    figure.canvas.draw()
    figure.canvas.flush_events()
    