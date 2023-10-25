import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt

path = input("quel est le fichier a visualisé :")
newrate = int(input("espace entre les points :"))
rate,data = wavfile.read(path)
time = np.arange(len(data))/float(rate)
newtime=[]
newdata=[]
newmoddata=[]
i=0
while(i<len(time)) :
    newtime.append(time[i])
    newdata.append(data[i])
    newmoddata.append(abs(data[i]))
    i=i+newrate
print(newdata)
print(newmoddata)
plt.plot(newtime,newdata)
plt.plot(newtime,newmoddata)
plt.show()