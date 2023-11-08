import cmath as math
import scipy.io.wavfile as wavfile
import numpy as np
import numpy . fft as npft
import matplotlib.pyplot as plt

path=input("fichier 1 :")
rate,data = wavfile.read(path)
path=input("fichier 2 :")
rate1,data1 = wavfile.read(path)

plt.figure()
plt.plot(data)
plt.plot(data1)
plt.show()
Un=npft.fft(data) 
Deux=npft.fft(data1)
un=[]
deux=[]
for i in Un :
    un.append(i.real)
for i in Deux :
    deux.append(i.real)
mod1 = np.linalg.norm(un,2)
mod2 = np.linalg.norm(deux,2)
print("mod 1 :")
print(mod1)
print("mod 2 :")
print(mod2)
time1=np.arange(len(un))
Time1=[]
for t in time1 :
    Time1.append(t)
time2=np.arange(len(deux))
Time2=[]
for t in time2 :
    Time2.append(t)

visu_un=np.abs(Un)
visu_deux=np.abs(Deux)
plt.figure()    

plt.plot(Time1,visu_un,"-r", label="son 1")
plt.plot(Time2,visu_deux,"-b", label="son 2")
plt.show()