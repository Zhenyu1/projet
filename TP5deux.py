from vecteurprof import Vecteur3D as V3D
from Torseurprof import Torseur

class SolideEncastre(object):
    """un solide rigide encastré à l'origine de son repère local"""
    def __init__(self,centredemasse=V3D(),masse=0.,Effortsext=[]):
        self.centredemasse= centredemasse
        self.masse= masse
        self.poids=Torseur(centredemasse,V3D(0,0,-masse*9.81),V3D())
        self.poids.chgPt()
        self.Effortsext= Effortsext+[self.poids]
        self.effortliaison=Torseur()
        self.equilibre()

    def __str__(self):
        msg='SolideEncastre('+str(self.centredemasse)+','+str(self.masse)+','+str(self.Effortsext)+')'
        return msg

    def __repr__(self):
        msg="SolideEncastre("+str(self.centredemasse)+','+str(self.masse)+','+str(self.Effortsext)+')'
        return msg

    def equilibre(self):
        S=Torseur()
        for i in self.Effortsext:
            S=S+i
        self.effortliaison=-S
        return -S

    def ajoutFEXT(self,T=Torseur()):
        self.Effortsext.append(T)
        self.equilibre()

class Structure(object):

    def __init__(self,centredemasse=V3D(),masse=0.,Effortsext=[],enfants={},parent=None):
        self.solide=SolideEncastre(centredemasse,masse,Effortsext)
        self.enfants=enfants
        self.parent=parent
        self.enfantstotorseur()

    def ajoutenfant(self,S=SolideEncastre(),Position=V3D()):
        self.enfants[S]=Position
        self.enfantstotorseur()

    def Enfantstotoseur():
        for enfant in self.enfants
            Position =self.enfants[enfant]
            enfant.Enfantstotorseur()
            enfant.eauilibre()


if __name__=="__main__":#false lors d'un import
    P1 = V3D(y=3)
    R1 = V3D(1, 2, 3)
    M1 = V3D(3, 2, 3)

    P2 = V3D()
    R2 = V3D(4, 1, 3)
    M2 = V3D(3, 0, 3)

    T1 = Torseur(P1, R1, M1)
    T0 = Torseur()
    T2 = Torseur(P2, R2, M2)


    S0=SolideEncastre(masse=10)
    #print(S0, "\n")
    #print(S0.effortliaison)
    S0.ajoutFEXT(T1)

    #print(S0,"\n")
    #print(S0.effortliaison)

    S0.ajoutFEXT(T2)

    #print(S0,"\n")
    #print(S0.effortliaison)
    #print(S0.Effortsext)


def inputVecteur(msg=''):
    print(msg)
    x = float(input("entre x\n"))
    y = float(input("entre y\n"))
    z = float(input("entre z\n"))
    return Vecteur3D(x,y,z)


def inputTorseur(msg=''):
    print(msg)

    P = inputVecteur("point\n")
    R = inputVecteur("R\n")
    M = inputVecteur("M\n")
    return Torseur(P, R, M)

