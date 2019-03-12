class Vecteur2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, autre): # addition vectorielle
        return Vecteur2D(self.x + autre.x, self.y + autre.y)
    def __str__(self):      # affichage d’un Vecteur2D
        return "Vecteur(%g, %g)" % (self.x, self.y)
v1 = Vecteur2D(1.2, 2.3)
v2 = Vecteur2D(3.4, 4.5)
print (v1 + v2 )# affiche : Vecteur(4.6, 6.8)
print(v1.x)
