import nidaqmx
from nidaqmx.constants import AcquisitionType
def DAQ():
    task = nidaqmx.Task()
    # task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0",
    #                                         max_val = 0.5,
    #                                         min_val = -0.5,
    #                                         )
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0",
                                            max_val = 0.5,
                                            min_val = -0.5,
                                            )
    task.timing.cfg_samp_clk_timing(4096,
                                        sample_mode = AcquisitionType.CONTINUOUS)
    data = task.read()
    #print(data)
    task.close()
    return data