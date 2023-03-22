import matplotlib.pyplot as plt
plt.ion()
figure, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex = True,figsize=(8,6), facecolor='black') #unpack value 
plt.tight_layout()
ax = [ax1, ax2]
line1, = ax1.plot([], [], lw=2, label = 'Sensor Voltage',color = 'white')
for i in ax:
    i.set_facecolor("black")
    i.spines['bottom'].set_color('white')
    i.spines['top'].set_color('white') 
    i.spines['right'].set_color('white')
    i.spines['left'].set_color('white')
    i.tick_params(axis='x', colors='white')
    i.tick_params(axis='y', colors='white')