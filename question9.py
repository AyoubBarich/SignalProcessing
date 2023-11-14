# %%
import cmath as cmath
import scipy.io.wavfile as wavfile
import numpy as np
import numpy.fft as npft
import matplotlib.pyplot as plt

# %%
fs_0, u_0 = wavfile.read("u0.wav")
fs_1, u_1 = wavfile.read("u1.wav")
u_0_hat = npft.fft(u_0)
u_1_hat = npft.fft(u_1)
u_0_hat_real = u_0_hat.real
u_1_hat_real = u_1_hat.real

# %%

mod_u_0_hat = [np.linalg.norm(c) for c in u_0_hat]
mod_u_1_hat = [np.linalg.norm(c) for c in u_1_hat]

# %%
plt.figure(1)    
plt.title('Modules')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.plot(mod_u_0_hat,"-r")
plt.plot(mod_u_1_hat,"-b")

# %%
plt.figure(1)
plt.title('U_0 et U_1')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.plot(u_0, "-r")
plt.plot(u_1, "-b")
plt.show()

plt.figure(2)    
plt.title('U_0_hat et U_1_hat')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.plot(u_0_hat_real,"-r")
plt.plot(u_1_hat_real,"-b")
plt.show()

def filtrage(M,y):
    y_hat = np.fft.fft(y)
    N = ychap.size
    mask = np.ones(N)
    coord = np.arrange(M+1, N-M, 1)
    mask[coord] = 0
    y_filtered_hat = mask * y_hat
    y_filtered = np.fft.ifft(y_filtered_hat)
    y_filtered = y_filtered.real
    return y_filtered

wavfile.write("./out/filtrageTest.wav", fs, filtrage() )

    """

def findnoise(sons) :
    i=0
    while i<len(sons) :
        if sons[i]>13000 :
            break
        i=i+1
    return i
def filtrage(M,y) :
    ychap = npft.fft(y)
    N = ychap.size
    mask=np.ones(N)
    coord = np.arange(M+1,N-M,1)
    mask[coord]=0
    yfiltchap = mask*ychap
    yfilt = npft.ifft(yfiltchap)
    yfilt = yfilt.real
    return yfilt


rate,data = wavfile.read("y0.wav")
print(findnoise(np.abs(npft.fft(data))))
débruité=filtrage(20000,data)
wavfile.write("./out/pasbruit.wav",rate,débruité)
    """