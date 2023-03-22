"""
Analog data acquisition for QuSpin's OPMs via National Instruments' cDAQ unit
The following assumes:
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np

import nidaqmx
from nidaqmx.stream_readers import AnalogMultiChannelReader
from nidaqmx import constants
import time

import threading
import pickle
from datetime import datetime
import scipy.io
#%%

# Parameters
sampling_freq_in = 1000  # in Hz
buffer_in_size = 100
bufsize_callback = buffer_in_size
buffer_in_size_cfg = round(buffer_in_size * 1)  # clock configuration
chans_in = 3  # set to number of active OPMs (x2 if By and Bz are used, but that is not recommended)
refresh_rate_plot = 10  # in Hz
crop = 10  # number of seconds to drop at acquisition start before saving
my_filename = 'test_3_opms'  # with full path if target folder different from current folder (do not leave trailing /)



# Initialize data placeholders
buffer_in = np.zeros((chans_in, buffer_in_size))
data = np.zeros((chans_in, 1))  # will contain a first column with zeros but that's fine


# Definitions of basic functions
def ask_user():
    global running
    input("Press ENTER/RETURN to stop acquisition and coil drivers.")
    running = False


def cfg_read_task(acquisition):  # uses above parameters
    acquisition.ai_channels.add_ai_voltage_chan("SimDev1/ai1:3")  # has to match with chans_in
    acquisition.timing.cfg_samp_clk_timing(rate=sampling_freq_in, sample_mode=constants.AcquisitionType.CONTINUOUS,
                                           samps_per_chan=buffer_in_size_cfg)


def reading_task_callback(task_idx, event_type, num_samples, callback_data):  # bufsize_callback is passed to num_samples
    global data
    global buffer_in

    if running:
        # It may be wiser to read slightly more than num_samples here, to make sure one does not miss any sample,
        # see: https://documentation.help/NI-DAQmx-Key-Concepts/contCAcqGen.html
        buffer_in = np.zeros((chans_in, num_samples))  # double definition ???
        stream_in.read_many_sample(buffer_in, num_samples, timeout=constants.WAIT_INFINITELY)
        data = np.append(data, buffer_in, axis=1)  # appends buffered data to total variable data
    return 0  # Absolutely needed for this callback to be well defined (see nidaqmx doc).

#%%
# Configure and setup the tasks
task_in = nidaqmx.Task()
cfg_read_task(task_in)
stream_in = AnalogMultiChannelReader(task_in.in_stream)
task_in.register_every_n_samples_acquired_into_buffer_event(bufsize_callback, reading_task_callback)


# Start threading to prompt user to stop
thread_user = threading.Thread(target=ask_user)
thread_user.start()


# Main loop
running = True
time_start = datetime.now()
task_in.start()


# Plot a visual feedback for the user's mental health
#f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex='all', sharey='none')
f, (ax1) = plt.subplots(1, 1, sharex='all', sharey='none')
while running:  # make this adapt to number of channels automatically
    ax1.clear()
   
    ax1.plot(data[0, -sampling_freq_in * 5:].T)  # 5 seconds rolling window
    
    # Label and axis formatting
    ax1.set_xlabel('time [s]')
    ax1.set_ylabel('voltage [V]')
    
    xticks = np.arange(0, data[0, -sampling_freq_in * 5:].size, sampling_freq_in)
    xticklabels = np.arange(0, xticks.size, 1)
    plt.pause(1/refresh_rate_plot)  # required for dynamic plot to work (if too low, nulling performance bad)


# Close task to clear connection once done
task_in.close()
duration = datetime.now() - time_start
