# Imports
import matplotlib.pyplot as plt
import numpy as np
import nidaqmx
from nidaqmx.stream_readers import AnalogMultiChannelReader
from nidaqmx import constants
import threading
import pickle
from datetime import datetime
import scipy.io
import time
import matplotlib.pyplot as plt
import pyrebase #for data upload, download
sampling_freq_in = 1000  
buffer_in_size = 100
bufsize_callback = buffer_in_size
buffer_in_size_cfg = round(buffer_in_size * 1)  
chans_in = 3 
refresh_rate_plot = 10  
crop = 10  
my_filename = 'test_3_opms' 
buffer_in = np.zeros((chans_in, buffer_in_size))
data = np.zeros((chans_in, 1))  
# Definitions of basic functions
def ask_user():
    global running
    input("Press ENTER/RETURN to stop acquisition and coil drivers.")
    running = False


def cfg_read_task(acquisition):  
    acquisition.ai_channels.add_ai_voltage_chan("SimDev1/ai0:2") 
    # acquisition.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0:2") 
    acquisition.timing.cfg_samp_clk_timing(rate=sampling_freq_in, sample_mode=constants.AcquisitionType.CONTINUOUS,
                                           samps_per_chan=buffer_in_size_cfg)


def reading_task_callback(task_idx, event_type, num_samples, callback_data): 
    global data
    global buffer_in

    if running:
        buffer_in = np.zeros((chans_in, num_samples))  
        stream_in.read_many_sample(buffer_in, num_samples, timeout=constants.WAIT_INFINITELY)
        data = np.append(data, buffer_in, axis=1)  
    return 0  
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
        return self.db.child(self.DBfolder).child(i).get().val()
    def upload(self,i, data):
        self.db.child(self.DBfolder).child(i).set(data)
    def upload2(self, data):
        self.db.child(self.DBfolder).set(data)    

# DAQ startup
task_in = nidaqmx.Task()
cfg_read_task(task_in)
stream_in = AnalogMultiChannelReader(task_in.in_stream)
task_in.register_every_n_samples_acquired_into_buffer_event(bufsize_callback, reading_task_callback)
# Start threading to prompt user to stop
thread_user = threading.Thread(target=ask_user)
thread_user.start()
running = True
time_start = datetime.now()
task_in.start()
# DB startup
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
F = Firebase(locat,DBfolder = 'DAQSet')
figure, ax1 = plt.subplots(nrows=1, ncols=1, sharex = True,figsize=(8,6), facecolor='black') 
plt.ion()
ax1.set_ylabel('Voltage (V)', fontsize=15)
ax1.set_title('Piezoelectric Signal', color="white",fontweight='bold', fontsize=18)
for AX in [ax1]:
    for side in ['top','bottom','left','right']:
        AX.set_facecolor("black")
        AX.spines[side].set_color('white')
        AX.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
        AX.yaxis.label.set_color('white') 
        AX.tick_params(axis='x', colors='white')
        AX.tick_params(axis='y', colors='white')
        AX.set_xlim(0,10)
        AX.set_xlabel('Time (s)', fontsize=15)
        AX.spines[side].set_linewidth(2)
ax1.set_title('Piezoelectric Signal', color="white",fontweight='bold', fontsize=18)
line1, = ax1.plot([], [], lw=2, label = 'Sensor Voltage',color = 'white')

#
i = 1
while running:  # make this adapt to number of channels automatically
    ax1.clear()
    y1 = data[0, -sampling_freq_in * 5:].T
    F.upload(i,np.ndarray.tolist(y1))
    ax1.plot(y1, label = 'Sensor Voltage',color = 'white')  # 5 seconds rolling window
    xticks = np.arange(0, data[0, -sampling_freq_in * 5:].size, sampling_freq_in)
    xticklabels = np.arange(0, xticks.size, 1)
    plt.pause(1/refresh_rate_plot)  
    i += 1
    figure.canvas.draw()
    figure.canvas.flush_events()
# Close task to clear connection once done
task_in.close()

#%%
task_in = nidaqmx.Task()
cfg_read_task(task_in)
stream_in = AnalogMultiChannelReader(task_in.in_stream)
task_in.register_every_n_samples_acquired_into_buffer_event(bufsize_callback, reading_task_callback)
# Start threading to prompt user to stop
thread_user = threading.Thread(target=ask_user)
thread_user.start()
running = True
time_start = datetime.now()
task_in.start()

plt.ion()
figure1, ax1, = plt.subplots(nrows=1, ncols=1, figsize=(8,6)) #unpack value
plt.tight_layout()
line1, = ax1.plot([], [], lw=2, label = 'Sensor Voltage',color = 'white')
plt.xlim(0,10)
ax1.set_ylim(-1,1)
ax1.set_ylabel('Voltage (V)', fontsize=15)
figure1.patch.set_facecolor('black')

for side in ['top','bottom','left','right']:
    ax1.set_facecolor("black")
    ax1.spines[side].set_color('white')
    ax1.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
    ax1.yaxis.label.set_color('white') 
    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='white')
    ax1.set_xlim(0,10)
    ax1.set_xlabel('Time (s)', fontsize=15)
    ax1.spines[side].set_linewidth(2)
ax1.set_title('Piezoelectric Signal', color="white",fontweight='bold', fontsize=18)
index = 1
x_update, y1_update, y2_update = np.array([]), np.array([]), np.array([])
#%%
while running:
    x_update = np.append(x_update, index)
    y1 = data[0, -sampling_freq_in * 5:].T
    y1_update = np.append(y1_update, y1)
    line1.set_data(x_update, y1_update)   
    figure.canvas.draw()
    figure.canvas.flush_events()
    index += 1
task_in.close()