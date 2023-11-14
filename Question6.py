import cmath as cmath
import scipy.io.wavfile as wavfile
import numpy.fft as npft

N = 4096 #cardDecoupage
fs = 4096 #fréquence
T = 1    #temps echantilloné
possible_l = [400,600,1000]

def epsLN(l,n):
    return cmath.exp(complex(0,(2*cmath.pi*l*n)/N))

print(epsLN(400, 1520))

for l in possible_l:
    musicFileName = "Test" + str(l) + ".wav"
    outPutRealPathName = "./out/RealOutPut" + musicFileName
    outPutRealHatPathName = "./out/RealHatOutPut" + musicFileName
    print("musicFileName is :" + musicFileName)

    vector_eps_l = np.array([epsLN(l,n) for n in range(N)])
    vector_eps_l_real = vector_eps_l.real

    vector_eps_l_hat = npft.ifft(vector_eps_l)
    vector_eps_l_hat_real = vector_eps_l.real

    print("vector_eps_l:")
    for elt in vector_eps_l:
        print(elt)

    wavfile.write(outPutPathName, fs, vector_eps_l )

