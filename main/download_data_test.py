import numpy as np
import time
import matplotlib.pyplot as plt
import firebase_admin
from firebase_admin import db
"""
@author: Small Brian
@date: 2022-04-2
@version: 1.3
@brief: Download from firebase, for test purpose.s
"""
import time
cred = firebase_admin.credentials.Certificate( r'D:\\BudProgram\\ntust-dal-firebase-adminsdk-np6tl-32a4c12061.json')
firebase_admin.initialize_app(cred, {
	'databaseURL':'https://XXX.com/'
	})
ref = db.reference('/')
#%%   
def autoscaleX(xmin, xmax):
    xmin += 5
    xmax += 5
    ax1.set_xlim(xmin, xmax)    
def downsize(update_x,update_y):
    for i in range(5):
        update_x.pop(i)
        update_y.pop(i)
    return update_x, update_y

#%%
plt.ion()
figure, ax1 = plt.subplots(nrows=1, ncols=1, sharex = False,figsize=(10,10), facecolor='black') #unpack value 
plt.tight_layout()
line1, = ax1.plot([], [], lw=2, label = 'Sensor Voltage',color = 'white')
plt.xlim(0,10)
ax1.set_ylim(-50,50)
ax1.set_ylabel('Force (N)', fontsize=15)
for i in [ax1]:
    for side in ['top','bottom','left','right']:
        i.set_facecolor("black")
        i.spines[side].set_color('white')
        i.xaxis.label.set_color('white')        #setting up X-axis label color to yellow
        i.yaxis.label.set_color('white') 
        i.tick_params(axis='x', colors='white')
        i.tick_params(axis='y', colors='white')
        i.set_xlim(0,10)
        i.set_xlabel('Time (s)', fontsize=15)
        i.spines[side].set_linewidth(2)
ax1.set_title('Cloud Computing: electricity convert to mechanical', color="white",fontweight='bold', fontsize=18)
#%%    
i = 1
DNTime = ()
while True and i <= 100: 
    ax1.clear()
    t1 = time.time()
    new_y2 = np.array(ref.child('ForceSet18').child(str(i)).get())
    t2 = time.time()
    DNTime = DNTime + (t2-t1, )
    plt.axis([0,5000,-0.1,0.1])
    # while np.size(new_y2) == 1:
    #         new_y2 = np.array(ref.child('ForceSet7').child(str(i)).get())
    ax1.plot(new_y2, label = 'Sensor Voltage',color = 'white')
    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(0.03)
    i += 1
import csv
with open('Fast_dnloadTime.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)
  writer.writerow(DNTime)