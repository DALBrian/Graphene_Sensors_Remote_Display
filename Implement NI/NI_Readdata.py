# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:16:57 2022

@author: user
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType
import time
sample_time = 60*5
s_freq = 2**12
num_samples = sample_time*s_freq
dt = 1/s_freq
i = 1
t1 = time.time()
while i <= 100:
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0",
                                            max_val = 0.5,
                                            min_val = -0.5,
                                            )
        # task.ai_channels.add_ai_voltage_chan("SimDev1/ai0",
        #                                     max_val = 0.5,
        #                                     min_val = -0.5,
        #                                     )
        task.timing.cfg_samp_clk_timing(51000,
                                        sample_mode = AcquisitionType.CONTINUOUS)
        #data = task.read(number_of_samples_per_channel = num_samples, timeout = nidaqmx.constants.WAIT_INFINITELY)
        data = task.read()
        #print(data)
        i+=1
t2 = time.time()
