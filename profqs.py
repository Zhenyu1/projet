from vecteurprof import Vecteur3D
from math import sin, cos, pi
import matplotlib.pyplot as plt


class Tortue(object):
    def __init__(self, nom='toto', position=Vecteur3D(), orientation=0, color='red'):
        self.nom = nom
        self.color = color
        self.positions = [position]
        self.orientations = [orientation]

    def __str__(self):
        msg = 'Tortue(' + str(self.positions[-1]) + ',' + str(self.orientations[-1]) + ')'
        return msg

    def __repr__(self):
        msg = 'Tortue(' + str(self.positions[-1]) + ',' + str(self.orientations[-1]) + ')'
        return msg

    def tourne(self, rad):
        self.positions.append(self.positions[-1])
        self.orientations.append(self.orientations[-1] + rad)

    def marche(self, dist):
        a = self.orientations[-1]
        v = Vecteur3D(dist * cos(a), dist * sin(a))
        self.positions.append(self.positions[-1] + v)
        self.orientations.append(self.orientations[-1])

    def teleport(self, position=Vecteur3D(), orientation=0):
        self.positions.append(position)
        self.orientations.append(orientation)

    def plot(self):
        X = []
        Y = []
        plt.figure("La route de " + self.nom)
        for i in self.positions:
            X.append(i.x)
            Y.append(i.y)

        plt.plot(X, Y, color=self.color)
        plt.show(block=False)


class Plage(object):
    Tortues = []

    def __init__(self, nom):
        self.nom = nom

    def ajoutTortue(self, T=Tortue()):
        self.Tortues.append(T)

    def enleveTortue(self, nom):
        for t in self.Tortues:
            if t.nom == nom:
                self.Tortues.remove(t)

    def trace(self):
        plt.figure('La plage de ' + self.nom)
        for t in self.Tortues:
            X = []
            Y = []
            for i in t.positions:
                X.append(i.x)
                Y.append(i.y)
            plt.plot(X, Y, color=t.color, label=t.nom)
            plt.legend()
        plt.show()


if __name__ == "__main__":  # false lors d'un import

    bob = Tortue('bob')
    mimi = Tortue('mimi', Vecteur3D(2, 4), pi / 4, 'blue')

    Paris = Plage('Paris')

    Paris.ajoutTortue(bob)
    Paris.ajoutTortue(mimi)
    Paris.Tortues[0].marche(3)

    bob.tourne(pi / 5)
    bob.marche(10)
    bob.tourne(-pi / 3)
    bob.marche(4)
    bob.tourne(pi / 9)
    bob.marche(6)
    # ~ bob.plot()

    mimi.marche(4)
    mimi.tourne(pi / 2)
    mimi.teleport(Vecteur3D(1, 1))
    mimi.tourne(pi / .15)
    mimi.marche(8)
    # ~ mimi.plot()

    # ~ input()

    Paris.trace()

