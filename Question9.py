# %%
import cmath as cmath
import scipy.io.wavfile as wavfile
import numpy as np
import numpy.fft as npft
import matplotlib.pyplot as plt
    
# %%
def question9_a(fileName):
    fs, vector = wavfile.read("ressources/" + fileName + ".wav")
    vector_hat = npft.fft(vector)
    vector_hat_real = vector_hat.real
    mod_vector_hat = [np.linalg.norm(c) for c in vector_hat]
    
    plt.figure(1)    
    plt.title("Modules des coordonées de " + fileName + " chapeau.")
    plt.xlabel('Temps')
    plt.ylabel('Amplitude')
    plt.plot(mod_vector_hat,"-r")
    plt.show()
# %%
question9_a("u0")
question9_a("y0")
question9_a("u1")
question9_a("y1")

# %%
def question9_b(i, M):
    # M est la fs ou l'on coupe
    def filtrage(M,y):
        y_hat = npft.fft(y)
        N = y_hat.size
        mask = np.ones(N)
        coord = np.arange(M+1, N-M, 1)
        mask[coord] = 0
        y_filt_hat = mask * y_hat
        y_filt = npft.ifft(y_filt_hat)
        return y_filt


    fs, u = wavfile.read("ressources/u" + str(i) + ".wav")
    fs, y = wavfile.read("ressources/y" + str(i) + ".wav")
    y_filt = filtrage(M,y)
    diff_u_y = u - y_filt
    
    plt.figure(1)    
    plt.title("u_" + str(i) + " (en rouge), y_" + str(i) + " filtré (en bleu)  et (u_" + str(i) + " - y_" + str(i) + " filtré) (en vert)")
    plt.xlabel('Temps')
    plt.ylabel('Amplitude')
    plt.plot(u.real ,"-r")
    plt.plot(y_filt.real,"-b")
    plt.plot(diff_u_y.real,"-g")
    plt.show()
    
    wavfile.write("./out/filteredY"+str(i)+".wav", fs, y_filt.real )

# %%
question9_b(0, 20000)
# apres 20000 (time) sur y_0, dirac de grande amplitude à couper 