import numpy as np
from scipy.io import wavfile
import pickle

audiofile = "Track16.wav"
binfile = "encoded8bit.bin"

fs, data = wavfile.read(audiofile)
#data8bit = (data/(2**8)).astype(np.uint8)
data8bit = (data/(2**8) + 127).astype(np.uint8)
size = pickle.dump(data8bit, open(binfile, "wb"), protocol=1)

# 1.2 Mb *.bin
# 0.9 Mb *.wav
