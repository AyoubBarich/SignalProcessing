import cmath as math
import scipy.io.wavfile as wavfile
import numpy
class vector() :
    def __init__(self,dim):
        self.dim=dim

    def value(self,l,n):
        return math.exp(complex(0,(2*math.pi*l*n)/self.dim))

V=vector(4096)
Vec=[]
Vec2=[]
Vec3=[]
for i in range(4096) :
    Vec.append(V.value(400,i))
    Vec2.append(V.value(600,i))
    Vec3.append(V.value(1000,i))
print(Vec)
Real=[]
Real2=[]
Real3=[]
for i in Vec :
    Real.append(i.real)
for i in Vec2 :
    Real2.append(i.real)
for i in Vec3 :
    Real3.append(i.real)
real=numpy.array(Real)
real2=numpy.array(Real2)
real3=numpy.array(Real3)
wavfile.write("test400.wav",4096,real)
wavfile.write("test600.wav",4096,real2)
wavfile.write("test1000.wav",4096,real3)     