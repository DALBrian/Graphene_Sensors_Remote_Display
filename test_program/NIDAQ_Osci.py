#Read DAQ data, upload to DB and download DB data, finally plot it as 2 ani in 1 fig
import nidaqmx #DAQ
from nidaqmx.constants import AcquisitionType #DAQ
import time #time estimation
import matplotlib.pyplot as plt #data visualization
from matplotlib.animation import FuncAnimation #data visualization
#%% library
#Database
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
def axis_update():
    #print('axis update')
    for ax in [ax1]:
        xmin, xmax = ax.get_xlim()
        xmin += 5
        xmax += 5
        plt.gcf()
        plt.gca()
        plt.axis([xmin, xmax, -2,2])
def update(i):
    #print(i)
    if i >= 90 and i%10 == 1:
        axis_update()
    data = DAQ()
    if data == None and i > 1:
        time.sleep(0.05)
    Data = DAQ()
    xdata.append(i)
    DAQdata.append(Data)
    #print('data ', i, 'DAQdata ', DAQ(), 'DBdata ', F.ReadData(i))
    line[0].set_data(xdata, DAQdata)
    return line
       

#%%
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
#FB = Firebase()
fig, ax1 = plt.subplots(nrows=1, ncols=1, sharex = True) #unpack value 
line1, = ax1.plot([], [], lw=2,label = 'DAQ Data')
line = [line1]
DAQdata = []
xdata = []
DBdata=[]
#%% Main program
plt.ion()
plt.axis([0,100,-2,2])
ax1.set_ylim(-4, 4)
#ln, = plt.plot([], [],marker='o',markersize=3)
ax1.legend()
ani = FuncAnimation(fig, update, frames= range(1,10000)
                    , blit=False, interval = 0.01)
