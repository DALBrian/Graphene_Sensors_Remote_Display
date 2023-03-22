import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import nidaqmx
from nidaqmx.constants import AcquisitionType
#%%
def init(self):
    self.x_start = 0
    self.x_end = 5
    self.y_start = -2
    self.y_end = 2
    # ax.set_xlim( self.x_start,  self.x_end)
    # ax.set_ylim(-0.1, 3)
    plt.axis([ self.x_start,  self.x_end,
               self.y_start,  self.y_end])
    return ln,
def abc(self,frame):
    self.x_start = 0
    self.x_end = 5
    self.y_start = -2
    self.y_end = 2
    #print(frame)
    if frame%5 == 1:
        xdata.pop(0)
        ydata.pop(0)
        self.x_start += 5
        self.x_end += 5
        plt.axis([self.x_start, self.x_end, 
                  self.y_start, self.y_end])

        #plt.axis([self.x_start, self.x_end, self.y_start, self.y_end])
    xdata.append(frame)
    ydata.append(DAQ())
    ln.set_data(xdata,ydata)
    return ln,
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
    print(data)
    task.close()
    return data

def UpdateAxis(x_start, x_end):
    x_start += 5
    x_end += 5
    plt.axis([x_start, x_end],0,1)
class Update:
    def init(self):
        self.x_start = 0
        self.x_end = 5
        self.y_start = -2
        self.y_end = 2

        plt.axis([ self.x_start,  self.x_end,
                   self.y_start,  self.y_end])
        return ln,
    def UpdateAxis(x_start, x_end):
        x_start += 5
        x_end += 5
        plt.axis([x_start, x_end],0,1)
        
#%%
def init():
    x_start = 0
    x_end = 5
    y_start = -2
    y_end = 2
    # ax.set_xlim( self.x_start,  self.x_end)
    # ax.set_ylim(-0.1, 3)
    plt.axis([ x_start, x_end,
               y_start,  y_end])
    return ln,
def abc(frame):
    ymin = -2
    ymax = 2
    print(frame)
    # if frame > 5:
    #     print(frame)
    #     xmin, xmax = ax.get_xlim()
    #     xmin += 5
    #     xmax += 5
    #     print('xmin: ', xmin,'xmax: ', xmax)
    #     plt.axis[xmin, xmax, ymin, ymax]
    xmin, xmax = ax.get_xlim()
    if frame == 0.0:
        xdata.clear()
        ydata.clear()
    xdata.append(frame)
    ydata.append(DAQ())
    ln.set_data(xdata,ydata)
    # ln.set_data(frame,DAQ())
    return ln,
def DAQ():
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0",
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
fig, ax = plt.subplots()
xdata, ydata = [0], [0]
#ln, = plt.plot([], [],marker='o',markersize=3)
ln, = ax.plot([], [], color='red', marker='o', markersize=10, markeredgecolor='black', linestyle='')
ani = FuncAnimation(fig, abc, frames=np.linspace(0,5,11),
                    init_func=init, blit=True, interval = 0.01)
plt.show()

 
       