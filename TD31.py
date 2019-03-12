class C(object):
    def __init__(self, a=0,b=0,c=0):
        self.x = a# initialisation de l’attribut d’instance x
        self.y = b
        self.z = c
v = C(5,10,-3)   # param`etre obligatoire, affect ́e `a n
print (v.x )  # 42
print (v.y )
print (v.z )

