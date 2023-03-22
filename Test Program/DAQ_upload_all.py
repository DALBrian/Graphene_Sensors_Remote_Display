import nidaqmx #DAQ
from nidaqmx.constants import AcquisitionType #DAQ
import pyrebase #for data upload, download
import matplotlib.pyplot as plt
import numpy as np
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
    
    def upload(self,i, data):
        self.db.child('Folder2').child(i).set(data)
def DAQ():
    task = nidaqmx.Task()
    # task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0",
                                            max_val = 0.5,
                                            min_val = -0.5,
                                            )
    task.timing.cfg_samp_clk_timing(4096,
                                        sample_mode = AcquisitionType.CONTINUOUS)
    data = task.read()
    task.close()
    return data
#%%
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
F = Firebase(locat,DBfolder = 'Folder2')
plt.ion()
figure1, ax1, = plt.subplots(nrows=1, ncols=1, figsize=(8,6)) #unpack value
plt.tight_layout()
ax = [ax1]
figure = [figure1]
plt.tight_layout()
line1, = ax1.plot([], [], lw=2, label = 'Sensor Voltage',color = 'white')
#%%   
update_x, update_y1,  update_y2 = np.array([]), np.array([]), np.array([])
i = 1
while True:
    data = DAQ()
    update_x = np.append(update_x,i)
    F.upload(i, data) 
    update_y1 = np.append(update_y1, data)
    xmin, xmax = ax1.get_xlim()
    line1.set_data(update_x, update_y1)
    figure1.canvas.draw()
    figure1.canvas.flush_events()
    i += 1
    