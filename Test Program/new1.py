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
    def test(self,i):
        return self.db.child('Force').get().val()   
def autoscaleX(xmin, xmax):
    xmin += 5
    xmax += 5
    ax1.set_xlim(xmin, xmax)
    
def autoscaleY1(ymin, ymax):
    ax1.set_ylim(ymin, ymax)
def DAQ():
    task = nidaqmx.Task()
    # task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0" )
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0")
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
figure, (ax1) = plt.subplots(nrows=1, ncols=1, sharex = True,figsize=(8,6), facecolor='black') #unpack value 
ax = [ax1]
plt.tight_layout()
line1, = ax1.plot([], [], lw=2, label = 'Sensor Voltage',color = 'white')
plt.xlim(0,10)
#ax1.set_ylim(-0.05,0.05)
ax1.set_ylim(-5,5)
ax1.set_ylabel('Voltage (V)', fontsize=15)
for i in ax:
    for side in ['top','bottom','left','right']:
        i.set_facecolor("black")
        i.spines[side].set_color('white')
        i.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
        i.yaxis.label.set_color('white') 
        i.tick_params(axis='x', colors='white')
        i.tick_params(axis='y', colors='white')
        i.set_xlim(0,10)
        i.set_xlabel('Time (s)', fontsize=15)
        i.spines[side].set_linewidth(2)
ax1.set_title('Piezoelectric Signal', color="white",fontweight='bold', fontsize=18)
#%%   
update_x, update_y1,  update_y2 = np.array([]), np.array([]), np.array([])
i = 1
while True:
    t1 = time.time()
    update_x = np.append(update_x,i)
    new_y1 = DAQ()
    F.upload(i, new_y1)
    update_y1 = np.append(update_y1, new_y1)
    time.sleep(0.1)
    #new_y = F. ReadVolt(i)
    xmin, xmax = ax1.get_xlim()
    if i >= xmax:
        autoscaleX(xmin, xmax)
    line1.set_data(update_x, update_y1)
    figure.canvas.draw()
    figure.canvas.flush_events()
    t2 = time.time()
    i += 1
    