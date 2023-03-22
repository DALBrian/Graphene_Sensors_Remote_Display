# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:08:07 2022

@author: user
"""
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import nidaqmx
import random
#%% libary
class Scope:
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(0, 1)
        self.ax.set_xlim(0, self.maxt)
    def update(self, y):
        while i <= 100:
            with nidaqmx.Task() as task:
                task.ai_channels.add_ai_voltage_chan('SimDev1/ai0')
                data = task.read()
                return data
                
                
class ReadDAQ:

    def DATA():
        task = nidaqmx.Task()
        task.ai_channels.add_ai_voltage_chan('SimDev1/ai0')
        data = task.read()
        task.close()
        return data
    def RANDOM():
        number = random.randint(1,10)
        return number
    
i = 1
while i<10:
    A = ReadDAQ.DATA()
    print(A)
    i+=1
    
#%%main program      
fig, ax = plt.subplots()
scope = Scope(ax)
# pass a generator in "emitter" to produce data for the update funcion)
ani = animation.FuncAnimation(fig, scope.update, ReadDAQ.DATA, interval=50,
                              blit=True)
plt.show()

#%% Test 2
import numpy as np
import matplotlib.pyplot as plt
import random
xmin = 0
xmax = 4 * np.pi
A = 4
N = 1000
x = np.linspace(xmin, xmax, N)
y = A*np.sin(x)
y2 = np.array(x * random.random())
fig = plt.figure(figsize=(7, 6), dpi=100)
ax = fig.gca()
line, = ax.plot(x, y, color='blue', linestyle='-', linewidth=3)
dot, = ax.plot([], [], color='red', marker='o', markersize=10, markeredgecolor='black', linestyle='')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)

def update1(i):
    print(i)
    dot.set_data(x[i], y2[i])
    return dot,

def init():
    dot.set_data(x[0], y2[0])
    return dot,
def update2(i):
    dot.set_data(i, -2)
    return dot

ani = animation.FuncAnimation(fig=fig, func=update1, frames=N, init_func=init, interval=1000/N, blit=True, repeat=True)
plt.show()
#%% Try
import numpy as np
import matplotlib.pyplot as plt
def READDAQ(i):
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan('SimDev1/ai0')
    data = task.read()
    task.close()
    return data

    



fig = plt.figure(figsize=(5,5), dpi=100)
ax = fig.gca()
ax.set_xlabel('time')
ax.set_ylabel('voltage')
