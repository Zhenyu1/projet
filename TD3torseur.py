from TD3oppose import Vecteur3D

class Torseur (object):
    def __init__(self,x,y,z):
        self.x=Vecteur3D(x)
        self.y=Vecteur3D(y)
        self.z=Vecteur3D(z)

    def BA(self,autre):
        return Vecteur3D(self.x-autre.x)

    #def BABAR(self):

    def st(self):  # affichage d’un Vecteur2D
        return "Vecteur(%g, %g, %g)" % (self.x, self.y,self.z)

T1=([0,1,2],[1,2,3],[2,3,6])
T2=([1,3,2],[1,2,3],[2,3,6])
#T1.st()
print(T1)
print(dir(Torseur))