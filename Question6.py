import numpy as np
import scipy.io wavfile as wavfile

N = 4096 #cardDecoupage
T = 1    #temps echantilloné
possible_l = [400,600,1000]

def epsLN(l,n):
    return math.exp(complex(0,(2*math.pi*l*n)/self.dim))

for l in possible_l:
    musicFileName = "test" + l + ".wav"
    print("musicFileName is :" musicFileName)

    vector_eps_l = np.array (epsLN(l,n) for n in range N)
    vector_eps_l = vector_eps_l.real
    wavfile.write( "RealOutPut" + musicFileName, fs, y )





"""
from scipy.io.wavfile import write

import numpy as np

samplerate = 44100; fs = 100

t = np.linspace(0., 1., samplerate)

amplitude = np.iinfo(np.int16).max

data = amplitude * np.sin(2. * np.pi * fs * t)

write("example.wav", samplerate, data.astype(np.int16))

"""
        