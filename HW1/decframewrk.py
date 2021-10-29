import numpy as np
from scipy.io import wavfile
import pickle

audiofile = "Track16.wav"
binfile = "encoded.bin"
decoded = "decoded.wav"
rate = 16000

data = pickle.load(open(binfile, "rb"), encoding='int16')
wavfile.write(decoded, rate=rate, data=data)


# 2.5 Mb *.bin
# 1.8 Mb *.wav
