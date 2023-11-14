# %%
import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt

# %%
def printUandY(i):
    # i = 0 ou i = 1 
    fs_u, u = wavfile.read("ressources/u" + str(i) + ".wav")
    fs_y, y = wavfile.read("ressources/y" + str(i) + ".wav")

    time_u = np.arange(len(u))/float(fs_u)
    time_y = np.arange(len(u))/float(fs_y)
    
    plt.figure(1)    
    plt.title("u_" + str(i) + " et y_" + str(i))
    plt.xlabel('Temps')
    plt.ylabel('Amplitude')
    plt.plot(time_y, y,"-b")
    plt.plot(time_u, u,"-r")
    plt.show()
    
    
# %%
printUandY(0)
printUandY(1)
