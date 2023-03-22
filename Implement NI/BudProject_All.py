#Read DAQ data, upload to DB and download DB data, finally plot it as 2 ani in 1 fig
import pyrebase #for data upload, download
import nidaqmx #DAQ
from nidaqmx.constants import AcquisitionType #DAQ
import time #time estimation
import matplotlib.pyplot as plt #data visualization
from matplotlib.animation import FuncAnimation #data visualization
import random
#%% library
#Database
class Firebase():
    def __init__(self, DBfolder = 'Folder2'):
        self.DBfolder = DBfolder
    def database_init(self, JSONlocation):
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
        return db_config
    def ReadData(self,i):
        return db.child('Force').child(i).get().val()
    def ReadData2(self,i):
        return db.child('Folder2').child(i).get().val()
    def upload(i, data):
        db.child('Folder2').child(i).put(data)
# DAQ
def DAQ():
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0",
                                            max_val = 0.5,
                                            min_val = -0.5,
                                            )
    task.timing.cfg_samp_clk_timing(4096,
                                        sample_mode = AcquisitionType.CONTINUOUS)
    data = task.read()
    #print(data)
    task.close()
    return data
#Plot
class Plotting():
    def axis_update(self):
        xmin_new, xmax_new = ax1.get_xlim()
        print(xmin_new, xmax_new)
        xmin_new += 5
        xmax_new += 5
        plt.gcf()
        plt.gca()
        plt.axis([xmin_new, xmax_new, ymin, ymax])
        # fig.canvas.draw()
        # fig.canvas.flush_events()
        xmin_new, xmax_new = ax1.get_xlim()
        print(xmin_new, xmax_new)

    def update(self,i):
        Data1 = DAQ()
        #Data1 = F.ReadData2(i)
        Data2 = (F.ReadData(i))* -1 
        #print(Data2)
        #self.xmin1, self.xmax1 = ax1.get_xlim()
        if i >= 10 and i%10 == 1: 
            print('axis update')
            Plotting.axis_update()
        #db.child('Folder2').child(i).set(Data1)
        xdata.append(i)
        DAQdata.append(Data1)
        DBdata.append(Data2)
       
        #print('data ', i, 'DAQdata ', DAQ(), 'DBdata ', F.ReadData(i))
        line[0].set_data(xdata, DAQdata)
        #line[0].set_data(i, Data1)
        line[1].set_data(xdata, DBdata)
        return line
       

#%%
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
#FB = Firebase()
db = pyrebase.initialize_app(Firebase().database_init(locat)).database()
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex = True) #unpack value 
plt.tight_layout()
line1, = ax1.plot([], [], lw=2,label = 'Sensor Voltage')
line2, = ax2.plot([], [], lw=2, color='r', label = 'Force returning from Cloud database')
ax2.set_xlabel('time')
ax1.set_ylabel('Voltage (V)')
ax2.set_ylabel('Force (N)')
line = [line1, line2]
DAQdata, xdata, DBdata = [], [], []

#%% Main program
plt.ion()
xmin, xmax, ymin, ymax = 0, 100, -2, 2
plt.axis([xmin, xmax, ymin, ymax])
ax1.set_ylim(-1, 1)
ax2.set_ylim(-35, 35)
F = Firebase(DBfolder = 'Folder2')
#db.child('Folder2').remove()
#db.child('Force').remove()
ax1.legend()
ax2.legend()
ani = FuncAnimation(fig, Plotting().update, frames= range(1,10000)
                    , blit=False, interval = 0.01)
