import cmath as math
import scipy.io.wavfile as wavfile
import numpy as np
import numpy . fft as npft

path=input("fichier 1 :")
rate,data = wavfile.read(path)
path=input("fichier 2 :")
rate1,data1 = wavfile.read(path)
Un=npft.fft(data) 
Deux=npft.fft(data)
un=[]
deux=[]
for i in Un :
    un.append(i)
for i in Deux :
    deux.append(i)
print(un)
print(deux)