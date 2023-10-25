N = 4096 #cardDecoupage
T = 1    #temps echantilloné
possible_l = [400,600,1000]

class vector() :
    def __init__(self,dim):
        self.dim=dim
        self.values = [0 for i in range (dim)]

    def setCoordN(self,n,value):
        self.values[n] = value
        

def epsLN(l,n):
    return math.exp(complex(0,(2*math.pi*l*n)/self.dim))

def createEpsL(lIndex, cardDecoupage):
    EpsL = vector(cardDecoupage)
    for i in range(cardDecoupage):
        EpsL.setCoordN(i,epsLN(lIndex,i))

        