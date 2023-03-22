import numpy as np
import time
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.cos(x)
update_x, update_y = [], []
plt.ion()

figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot([], [], lw=2)

plt.title("Dynamic Plot of sinx",fontsize=25)
plt.axis([0,10,-1,1])
plt.xlabel("X",fontsize=18)
plt.ylabel("sinX",fontsize=18)
#%%
for p in range(500):
    updated_y = np.cos(x-0.05*p)
    line1.set_xdata(x)
    line1.set_ydata(updated_y)
    figure.canvas.draw()
    figure.canvas.flush_events()
    print(np.size(updated_y))
    time.sleep(0.1)
#%%
def autoscale(xmin, xmax):
    xmin += 1
    xmax += 1
    ax.set_xlim(xmin, xmax)
    
def downsize(x,y):
    x.pop(0)
    y.pop(0)
    return x, y
    
for i in range(1000):
    new_x = i
    new_y = np.cos(new_x)
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
#%%
index = 1
while True:
    updated_y = np.cos(x-0.05*index)
    line1.set_xdata(x)
    line1.set_ydata(updated_y)
    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(0.1)
    index += 1
    