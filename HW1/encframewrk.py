import numpy as np
from scipy.io import wavfile
import pickle

audiofile = "Track16.wav"
binfile = "encoded.bin"

fs, data = wavfile.read(audiofile)
size = pickle.dump(data, open(binfile, "wb"), protocol=1)

# 2.5 Mb *.bin
# 1.8 Mb *.wav
