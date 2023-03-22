import numpy as np
import time
import matplotlib.pyplot as plt
import nidaqmx #DAQ
from nidaqmx.constants import AcquisitionType #DAQ
import pyrebase #for data upload, download
#%%   
class Firebase():
    def __init__(self,JSONlocation ,DBfolder = 'Folder2'):
        self.DBfolder = DBfolder
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
        self.db = pyrebase.initialize_app(db_config).database()
    def ReadForce(self,i):
        return self.db.child('Force').child(i).get().val()
    def ReadVolt(self,i):
        return self.db.child('Folder2').child(i).get().val()
    def upload(self,i, data):
        self.db.child('Folder2').child(i).set(data)
    def test(self,i):
        return self.db.child('Force').get().val()   
def autoscaleX(xmin, xmax):
    xmin += 5
    xmax += 5
    ax1.set_xlim(xmin, xmax)
    ax2.set_xlim(xmin, xmax)
    
def downsize(update_x,update_y):
    for i in range(5):
        update_x.pop(i)
        update_y.pop(i)
    return update_x, update_y

#%%
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
F = Firebase(locat,DBfolder = 'Folder2')
plt.ion()
figure, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex = False,figsize=(10,10), facecolor='black') #unpack value 
ax = [ax1, ax2]
plt.tight_layout()
line1, = ax1.plot([], [], lw=2, label = 'Sensor Voltage',color = 'white')
line2, = ax2.plot([], [], lw=2, label = ' Force',color = 'white')



plt.xlim(0,10)
ax1.set_ylim(-1,1)
ax2.set_ylim(-50,50)
ax1.set_ylabel('Voltage (V)', fontsize=15)
ax2.set_ylabel('Force (N)', fontsize=15)
for i in ax:
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
ax1.set_title('Piezoelectric Signal', color="white",fontweight='bold', fontsize=18)
ax2.set_title('Cloud Computing: electricity convert to mechanical', color="white",fontweight='bold', fontsize=18)
#%%   
update_x, update_y1,  update_y2 = np.array([]), np.array([]), np.array([])
i = 1
ind1, ind2 =0, 0
while True:
    t1 = time.time()
    update_x = np.append(update_x,i)
    new_y1 = F.ReadVolt(i)
    #F.upload(i, new_y1)
    time.sleep(0.1)
    #new_y = F. ReadVolt(i)
    new_y2 = F.ReadForce(i)
    update_y1 = np.append(update_y1, new_y1)
    update_y2 = np.append(update_y2, new_y2)
    test = F.test(i)
    line1.set_data(update_x, update_y1)
    line2.set_data(update_x, update_y2)
    figure.canvas.draw()
    figure.canvas.flush_events()
    t2 = time.time()
    #print(t2-t1)
    i += 1
    ind1 += 1
    ind2 += 1
    