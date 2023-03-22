import pyrebase
import nidaqmx
import time
from nidaqmx.constants import AcquisitionType
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

#%%initialization
locat =  'D:\\BudProgram\\ntust-dal-firebase.json'
db = pyrebase.initialize_app(Firebase().database_init(locat)).database()
sample_time = 60*5
s_freq = 2**12
num_samples = sample_time*s_freq
dt = 1/s_freq
i = 1
ai_data = list()
time_read = tuple()
time_upload = tuple()
#%%
while i<50:
    t1 = time.time()
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0",
                                           max_val = 0.5,
                                           min_val = -0.5,
                                           )
        task.timing.cfg_samp_clk_timing(4096,
                                        sample_mode = AcquisitionType.CONTINUOUS)
        #data = task.read(number_of_samples_per_channel = num_samples, timeout = nidaqmx.constants.WAIT_INFINITELY)
        ai_data.append(task.read())
        print(task.read())
        db.child("BudProgram").set(ai_data)
        
        i+=1


#%%
while i <= 100:
    t1 = time.time() #time of reading data
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0",
                                           max_val = 0.5,
                                           min_val = -0.5,
                                           )
    task.timing.cfg_samp_clk_timing(4096,
                                    sample_mode = AcquisitionType.CONTINUOUS)
    #data = task.read(number_of_samples_per_channel = num_samples, timeout = nidaqmx.constants.WAIT_INFINITELY)
    ai_data.append(task.read())
    t2 = time.time() # read data
    #print(task.read())
    db.child("BudProgram").set(ai_data)
    task.close()
    t3 = time.time()
    time_read += (t2-t1,)
    time_upload += (t3-t2,)
    i+= 1
    

#%%
i = 1
data = list()
time_download = tuple()
while i < 100:
    t3 = time.time() #download time 
    temp = db.child('BudProgram').child(i).get().val()
    data.append(temp)
    t4 = time.time()
    time_download += (t4-t3,)
    i+=1

#%% 
import pandas as pd
df = pd.DataFrame(time_read)
df.to_csv('D:\\SynologyDrive\\Paper work\\BudProgram\\Implement NI\\time_readDAQ_wifi1101.csv')

df = pd.DataFrame(time_upload)
df.to_csv('D:\\SynologyDrive\\Paper work\\BudProgram\\Implement NI\\time_upload_wifi1101.csv')

df = pd.DataFrame(time_download)
df.to_csv('D:\\SynologyDrive\\Paper work\\BudProgram\\Implement NI\\time_download_wifi1101.csv')
