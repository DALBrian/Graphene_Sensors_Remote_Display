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

#%% DAQ startup
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
plt.xlim(0,10000)
ax1.set_ylim(-10,10)
ax1.set_ylabel('Voltage (V)', fontsize=15)
figure1.patch.set_facecolor('black')
#figure2, (ax2) = plt.subplots(nrows=1, ncols=1, sharex = True,figsize=(8,6), facecolor='black')
for axis in [ax1]:
    for side in ['top','bottom','left','right']:
        axis.set_facecolor("black")
        axis.spines[side].set_color('white')
        axis.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
        axis.yaxis.label.set_color('white') 
        axis.tick_params(axis='x', colors='white')
        axis.tick_params(axis='y', colors='white')
        axis.set_xlim(0,10)
        axis.set_xlabel('Time (s)', fontsize=15)
        axis.spines[side].set_linewidth(2)
ax1.set_title('Piezoelectric Signal', color="white",fontweight='bold', fontsize=18)
ax1.set_title('Signal History', color="white",fontweight='bold', fontsize=18)
index = 1
x_update, y1_update, y2_update = np.array([]), np.array([]), np.array([])
#%%
index = 1
sampling_freq_in = 1000
x_update = np.array([1])
history = np.array([])
while running:
    y1 = data[0, -sampling_freq_in * 5:].T
    history = np.append(history, y1)
    x_update = np.arange(1, np.size(history)+1)
    time.sleep(2)
    line1.set_data(x_update, history)   
    xmin, xmax = ax1.get_xlim()
    if x_update[-1] > xmax:
        ax1.set_xlim(xmin+sampling_freq_in * 5, xmax+sampling_freq_in * 5)
    figure1.canvas.draw()
    figure1.canvas.flush_events()
    index += 1
task_in.close()
#ax2.plot(history, label = 'Sensor Voltage',color = 'black')
