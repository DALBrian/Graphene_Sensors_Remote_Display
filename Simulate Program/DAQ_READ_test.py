# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nidaqmx
import matplotlib.pyplot as plt
plt.ion()
i = 0


with open('daqdata.txt','a') as file:
    with  nidaqmx.Task() as task:
        #task.ai_channels.add_ai_voltage_chan("SimDev1/ai0:1")
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0:1")
        while i < 10:
            aiData = task.read()
            plt.scatter(i, aiData[0], c = 'r')
            plt.scatter(i, aiData[1], c = 'b')
            plt.pause(0.05)
            #a = str(aiData)
            #file.write(a+"\n")
            i= i+1
            print(aiData)
plt.ioff()
plt.show()


