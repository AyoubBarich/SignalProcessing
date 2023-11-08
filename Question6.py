N = 4096 #cardDecoupage
T = 1    #temps echantilloné
possible_l = [400,600,1000]

class vector() :
    def __init__(self,dim):
        self.dim=dim
        self.valcoords = [0 for i in range (dim)]

def epsLN(l,n):
    return math.exp(complex(0,(2*math.pi*l*n)/self.dim))

def createEpsL(l, cardDecoupage):
    EpsL = vector(cardDecoupage)
    for i in range(cardDecoupage):
        EpsL.coords[i] = epsLN(l,i)

def getRealEpsL(EpsL):
    ReEpsL = vector(EpsL.dim)
    for i in range(EpsL.dim):
        ReEpsL.coords[i] = EpsL.coords[i].real

"""
from scipy.io.wavfile import write

import numpy as np

samplerate = 44100; fs = 100

t = np.linspace(0., 1., samplerate)

amplitude = np.iinfo(np.int16).max

data = amplitude * np.sin(2. * np.pi * fs * t)

write("example.wav", samplerate, data.astype(np.int16))

"""
        