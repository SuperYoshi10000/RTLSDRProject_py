import os
from dotenv import load_dotenv
from rtlsdr import RtlSdrTcpClient
import SoapySDR

load_dotenv()

sdr = RtlSdrTcpClient(
    hostname=os.getenv("RTLSDR_HOSTNAME", "localhost"),
    port=int(os.getenv("RTLSDR_PORT", 8000)),
    test_mode_enabled=bool(os.getenv("RTLSDR_TEST_MODE", False))
)

sample_rate = os.getenv("RTLSDR_SAMPLE_RATE", 2e6) # Sample rate in Hz
center_freq = os.getenv("RTLSDR_CENTER_FREQ", 100e6) # Center frequency in Hz
gain = os.getenv("RTLSDR_GAIN", "auto")

sdr.sample_rate = int(sample_rate)
sdr.center_freq = int(center_freq)
sdr.gain = "auto" if gain == "auto" else int(gain)

sdr.open()

while True:
    samples = sdr.read_samples(sample_rate) # One second
    print(samples)
    break