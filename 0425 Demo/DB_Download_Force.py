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

#%%
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
F = Firebase(locat,DBfolder = 'Folder2')
plt.ion()
figure, ax1 = plt.subplots(nrows=1, ncols=1, sharex = False,figsize=(10,10), facecolor='black') #unpack value 
plt.tight_layout()
line1, = ax1.plot([], [], lw=2, label = 'Force',color = 'white')



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
update_x, update_y1,  update_y2 = np.array([]), np.array([]), np.array([])
i = 1
while True:
    t1 = time.time()
    update_x = np.append(update_x,i)
    time.sleep(0.1)
    new_y2 = F.ReadForce(i)
    while new_y2 == None:
        new_y2 = F.ReadForce(i)
    update_y2 = np.append(update_y2, new_y2)
    line1.set_data(update_x, update_y2)
    xmin, xmax = ax1.get_xlim()
    if i >= xmax:
        autoscaleX(xmin, xmax)
    figure.canvas.draw()
    figure.canvas.flush_events()
    t2 = time.time()
    i += 1
  
    