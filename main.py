import os
from dotenv import load_dotenv

import SoapySDR
from SoapySDR import Device
from SoapySDR import *
import numpy as np

load_dotenv()

server=os.getenv("RTLSDR_SERVER", "localhost:8000")
print(server)
sdr = Device(dict(
    #driver="rtltcp",
    rtltcp=server,
))

sample_rate = os.getenv("RTLSDR_SAMPLE_RATE", 2e6) # Sample rate in Hz
center_freq = os.getenv("RTLSDR_CENTER_FREQ", 100e6) # Center frequency in Hz
gain = os.getenv("RTLSDR_GAIN", "auto")

sdr.setSampleRate(SOAPY_SDR_RX, 0, sample_rate)
sdr.setFrequency(SOAPY_SDR_RX, 0, center_freq)

stream = sdr.setupStream(SOAPY_SDR_RX, SOAPY_SDR_CF32)
sdr.activateStream(stream)

buf = np.array([0]*1024, np.complex64)

# Stuff

sdr.deactivateStream(stream)
sdr.closeStream(stream)