import numpy as np
from scipy.io import wavfile
import pickle

audiofile = "Track16.wav"
binfile = "encoded8bit.bin"
decoded = "decoded8bit.wav"
rate = 16000

data8bit = pickle.load(open(binfile, "rb"), encoding='int8')
wavfile.write(decoded, rate=rate, data=data8bit)


# 1.2 Mb *.bin
# 0.9 Mb *.wav
