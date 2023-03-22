#Read DAQ data, upload to DB and download DB data, finally plot it as 2 ani in 1 fig
import pyrebase #for data upload, download
import nidaqmx #DAQ
from nidaqmx.constants import AcquisitionType #DAQ
import time #time estimation
import matplotlib.pyplot as plt #data visualization
from matplotlib.animation import FuncAnimation #data visualization
#%% library
#Database
class Firebase():
    def __init__(self, DBfolder = 'folder2'):
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
    def upload(data):
        db.child('folder2').put(data)
# DAQ
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
#Plot
class Plotting():
    def __init__(self):
        self.xmin = 0.0
        self.xmax = 0.0
        self.ymin1 = 0.0
        self.ymax1 = 0.0
        self.ymin2 = 0.0
        self.ymax2 = 0.0
        self.Data1 = 0.0
        self.Data2 = 0.0
    def axis_update(self):
        self.xmin += 5
        self.xmax += 5
        # plt.gcf()
        # plt.gca()
        #plt.axis([xmin, xmax, -2,2])
        ax1.set_xlim(self.xmin, self.xmax)
 
    def ax1_scaling_max(self):
        # plt.gcf()
        # plt.gca()
        ax1.set_ylim(self.ymin1, round(self.Data1 + 1))
        fig.canvas.draw()
    def ax1_scaling_min(self):
        # plt.gcf()
        # plt.gca()
        ax1.set_ylim(round(self.Data1)-1, self.ymax1)
        fig.canvas.draw()
    def ax2_scaling_max(self):      
        print('ax2 max', 'data2', self.Data2)
        # plt.gcf()
        # plt.gca()
        ax2.set_ylim(self.ymin2, round(self.Data2 + 1))
        fig.canvas.draw()
    def ax2_scaling_min(self): 
        print('ax2 min', 'data2', self.Data2)
        # plt.gcf()
        # plt.gca()
        ax2.set_ylim(round(self.Data2)-1, self.ymax2)
        fig.canvas.draw()
    def update(self,i):
        self.Data1 = DAQ()
        self.Data2 = F.ReadData(i)
        self.xmin, self.xmax = ax1.get_xlim()
        self.ymin1, self.ymax1 = ax1.get_ylim()
        self.ymin2, self.ymax2 = ax2.get_ylim()
        # print('Data1 ', self.Data1, ' Data2 ', self.Data2)
        # print('xmin ', self.xmin, 'xmax ', self.xmax)
        # print('ymin1 ', self.ymin1, 'ymax1 ', self.ymax1)
        #print('ymin2 ', self.ymin2, 'ymax2 ', self.ymax2)
        # if i >= 10 and i%10 == 1:  
        #     Plotting().axis_update()
        # if self.Data2 == None and i > 1:
        #     time.sleep(0.05)
        # if self.Data1 > self.ymax1:
        #     Plotting().ax1_scaling_max()
        # elif self.Data1 < self.ymin1:
        #     Plotting().ax1_scaling_min()
        # if self.Data2 > self.ymax2:
        #     Plotting().ax2_scaling_max()
        # elif self.Data2 < self.ymax2:
        #     Plotting().ax2_scaling_min()
        ax2.autoscale(True)
        db.child('folder2').child(i).set(self.Data1)
        xdata.append(i)
        DAQdata.append(self.Data1)
        DBdata.append(self.Data2)
        
        #print('data ', i, 'DAQdata ', DAQ(), 'DBdata ', F.ReadData(i))
        line[0].set_data(xdata, DAQdata)
        line[1].set_data(xdata, DBdata)
        return line
       

#%%
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
#FB = Firebase()
db = pyrebase.initialize_app(Firebase().database_init(locat)).database()
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex = True) #unpack value
#plt.fig(figsize = (10,5))
ax1.set_ylim(-1, 2)
ax2.set_ylim(-50, 50) 
plt.tight_layout()
line1, = ax1.plot([], [], lw=2,label = 'DAQ Data')
line2, = ax2.plot([], [], lw=2, color='r', label = 'Cloud return')
ax2.set_xlabel('time')
ax1.set_ylabel('Voltage')
ax2.set_ylabel('Force')
line = [line1, line2]
DAQdata, xdata, DBdata, maxY = [], [], [], -9999999
#%% Main program
plt.ion()
ymin1, ymax1 = ax1.get_ylim()
ymin2, ymax2 = ax2.get_ylim()
#ln, = plt.plot([], [],marker='o',markersize=3)
F = Firebase(DBfolder = 'folder2')
ax1.legend()
ax2.legend()
#model = input('Input model type: ')
#db.child('Model').put(int(model))
ani = FuncAnimation(fig, Plotting().update, frames= range(1,10000)
                    , blit=False, interval = 0.01)
