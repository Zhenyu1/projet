from vecteurprof import Vecteur3D as v3d
import math
import matplotlib.pyplot as plt

class Tortue(object):
    def __init__(self,nom='Toto',position=v3d(),orientation=0,color='red'):#,accelerationT=0,accelerationA=0,vitessedetranslation=0,vitesseangulaire=0):
        self.nom=nom
        self.color=color
        self.position= [position]
        self.orientation=[orientation]
        #self.accelerationT=accelerationT
        #self.accelerationA = accelerationA
        #self.vitessedetranslation=vitessedetranslation
        #self.vitesseangulaire=vitesseangulaire


    def __str__(self):
        msg="Nom de tortue"+str(self.nom)+"Tortue position "+ str(self.position)+"Tortue orientation"+str(self.orientation)
        return msg
    def __repr__(self):
        msg = "Nom de tortue"+str(self.nom)+"Tortue position " + str(self.position) + "Tortue orientation" + str(self.orientation)
        return msg


    def marche(self,distance):


    def tourne(self,rad):


    def ouEstElle(self):


    def teleport(self,position,orientation):


    def plot(self):

    def sauve(self):

    def charge(self):





if __name__ == "__main__":  # false lors d'un import
    omega=10.
    t=10e-3
    pas=[omega,t]
