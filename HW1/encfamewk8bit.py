import numpy as np
from scipy.io import wavfile
import pickle

audiofile = "Track16.wav"
binfile = "encoded8bit.bin"

fs, data = wavfile.read(audiofile)
data8bit = np.int8(data/(2**8))
size = pickle.dump(data8bit, open(binfile, "wb"), protocol=1)

# 1.2 Mb *.bin
# 1.8 Mb *.wav
