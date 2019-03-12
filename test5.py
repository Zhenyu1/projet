from vecteurprof import Vecteur3D
from Torseurprof import Torseur


def inputVecteur(msg=''):
    print(msg)
    x=float(input("entre x"))
    y = float(input("entre y"))
    z = float(input("entre z"))
    return Vecteur3D(x,y,z)


def inputTorseur(msg=''):
    print(msg)

    P = inputVecteur("point")
    R = inputVecteur("R")
    M = inputVecteur("M")
    return Torseur(P, R, M)

listFE=[]
rep= 'o'

while (rep=="o"):
    T=inputTorseur()
    listFE.append(T)
    rep=input ("entrer un effort extern? o/n\n")

S=Torseur()

for i in listFE:
    S=S+i
print("effort de liaison est ",-S)


#print(inputVecteur())

#torseur1=inputTorseur()

#print(torseur1)
#print(inputTorseur())
#for k in range(n):
 #   torseur2=inputTorseur()
 #   torseur1=torseur2+torseur1

#print(torseur1)




