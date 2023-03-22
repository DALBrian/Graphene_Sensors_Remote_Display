import numpy as np
import time
import matplotlib.pyplot as plt
import nidaqmx #DAQ
from nidaqmx.constants import AcquisitionType #DAQ
#%%
update_x, update_y = [], []
plt.ion()
figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot([], [], lw=2)

plt.title("NTUST Program",fontsize=25)
plt.axis([0,10,-0.5,0.5])
plt.xlabel("T (s)",fontsize=18)
plt.ylabel(" Voltage (V)",fontsize=18)
#%%
def autoscale(xmin, xmax):
    xmin += 1
    xmax += 1
    ax.set_xlim(xmin, xmax+1)
    
def downsize(update_x,update_y):
    update_x.pop(0)
    update_y.pop(0)
    return update_x, update_y

def DAQ():
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0",
                                            max_val = 0.5,
                                            min_val = -0.5,
                                            )
    task.timing.cfg_samp_clk_timing(4096,
                                        sample_mode = AcquisitionType.CONTINUOUS)
    data = task.read()
    #print(data)
    task.close()
    return data
#%%   
for i in range(1000):
    new_x = i
    new_y = DAQ()
    update_x.append(new_x)
    update_y.append(new_y)
    xmin, xmax = ax.get_xlim()
    if i > xmax:
        autoscale(xmin, xmax)
        update_x,update_y = downsize(update_x,update_y)
    
    
    line1.set_data(update_x, update_y)
    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(0.1)