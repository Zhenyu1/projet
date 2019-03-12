#class C(object):
  #  """Documentation de la classe."""
 #   x = 23
#toto=C()
#print(toto.x)
#toto.x=5
#bob=C()
#print(bob.x)
#bob.y=1
##print(toto.y)
#print(dir(C))



class C(object):
    x = 23            # x et y : attributs de classe
    y = x + 5
    def affiche(self): # m ́ethode affiche()
        self.z = 42   # attribut d’instance
        print (C.y)# dans une m ́ethode, on qualifie un attribut    de classe,
        print (self.z)  # mais pas un attribut d’instance
ob = C()     # instanciation de l’objet ob
ob.affiche() # 28 42 (`a l’appel, ob affecte self