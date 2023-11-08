import scipy.io.wavfile as wavfile
import numpy as np
import numpy . fft as npft

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


path=input("fichier à débruité :")
rate,data = wavfile.read(path)
débruité=filtrage(20000,data)
wavfile.write("./out/pasbruit.wav",rate,débruité)