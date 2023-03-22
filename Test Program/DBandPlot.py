#Read Firebase Data and plotting as OSCi
import pyrebase
import nidaqmx
import time
from nidaqmx.constants import AcquisitionType
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#%% library
class Firebase():
    def database_init(self, JSONlocation):
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
        return db_config
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
db = pyrebase.initialize_app(Firebase().database_init(locat)).database()
#%% Read data - library
def ReadData(i):
    return db.child('folder1').child(i).get().val()
def Update(i):
    if i > 50:
        axis_update()
    data = ReadData (i)
    print(i, ' data is: ', data)
    ydata.append(data)
    xdata.append(i)
    ln.set_data(xdata, ydata)
    return ln,
#%% Axis renew
def axis_update():
    xmin, xmax = ax.get_xlim()
    xmin += 1
    xmax += 1
    plt.axis([xmin, xmax, -2,2])
    #fig.canvas.draw() #update axis

#%%Plotting
plt.ion()
fig, ax = plt.subplots()
plt.axis([0,100,-2,2])
xdata, ydata = [0], [0]
#ln, = plt.plot([], [],marker='o',markersize=3)
ln, = ax.plot([], [])
ani = FuncAnimation(fig, Update, frames= range(1,10000)
                    , blit=True, interval = 0.01)

















