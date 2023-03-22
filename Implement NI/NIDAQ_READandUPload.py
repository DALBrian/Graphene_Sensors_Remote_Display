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
#%%
while i<100:
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
        i+=1
time.sleep(0.5)
#db.child("0225Test").set(ai_data)




























#%% simulate to upload
import time
t1 = time.time()
t2 = time.time()
print(t1, t2)
#%%
i = 1
while i < 20:
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("SimDev/ai0",
                                           max_val = 0.5,
                                           min_val = -0.5,
                                           )
        task.timing.cfg_samp_clk_timing(4096,
                                        sample_mode = AcquisitionType.CONTINUOUS)
        #data = task.read(number_of_samples_per_channel = num_samples, timeout = nidaqmx.constants.WAIT_INFINITELY)
        #print(data)
        print(task.read())
        i += 1
# #%%
# with nidaqmx.Task() as task:
#     task.ai_channels.add_ai_voltage_chan("SimDev/ai0",
#                                        max_val = 0.5,
#                                        min_val = -0.5,
#                                        )
#     task.timing.cfg_samp_clk_timing(4096,
#                                     sample_mode = AcquisitionType.CONTINUOUS)