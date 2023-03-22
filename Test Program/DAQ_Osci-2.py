import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
y = 0
#line, = ax.plot([],[])
line, = ax.plot(x, np.sin(x))

#%%
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    # print(i)
    return line,


ani = animation.FuncAnimation(
    ax, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()

#%% My try
from nidaqmx.constants import AcquisitionType
import nidaqmx
import random

def update(i):
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0",
                                            max_val = 0.5,
                                            min_val = -0.5,
                                            )
    task.timing.cfg_samp_clk_timing(4096,
                                        sample_mode = AcquisitionType.CONTINUOUS)
    #data = task.read()
    data =random.random()
    print(data)
    line.set_ydata(data)
    task.close()
    return line,
ani = animation.FuncAnimation(
    fig, update, interval=20, blit=True, save_count=50)
plt.show()