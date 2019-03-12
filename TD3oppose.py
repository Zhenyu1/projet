import math
class Vecteur3D(object):
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
        #print(self.x,self.y,self.z)
    def __neg__(self):
        return Vecteur3D(-self.x,-self.y,-self.z)

    def __add__(self, autre): # addition vectorielle
        return Vecteur3D(self.x + autre.x , self.y + autre.y, self.z + autre.z)

    def __sub__(self,autre):
        #return Vecteur3D(self.x - autre.x, self.y - autre.y, self.z + autre.z)
        return self+(-autre)


    def __rmul__(self,autre):
        return self * autre

    def __mul__(self, autre):
        if type(autre)==Vecteur3D:
            #print(type(autre))
            #print(Vecteur3D)
            X=self.y*autre.z-self.z*autre.y
            Y=self.z*autre.x-self.x*autre.z
            Z=self.x*autre.y-self.y*autre.x
            return Vecteur3D(X,Y,Z)
           # return Vecteur3D(self.y*autre.z-self.z*autre.y,self.z*autre.x-self.x*autre.z,self.x*autre.y-self.y*autre.x)
        else:
            return Vecteur3D(self.x*autre,self.y*autre,self.z*autre)

    def __pow__(self, autre):
        if type(autre) == Vecteur3D:
            return (self.x*autre.x+self.y*autre.y+self.z*autre.z)
        else:
            return Vecteur3D(self.x * autre, self.y * autre, self.z * autre)

    def __rpow__(self, autre):
        return self **autre

    def mod(self):
        return (self**self)**0.5

    def __truediv__(self,autre):
        return self**(1/autre)

    def norm(self):
        return self/self.mod()


    def normed(self):
        M=self.norm()
        self.x = M.x
        self.y = M.y
        self.z = M.z
        print(M.x,M.y,M.z)



    def __str__(self):  # affichage d’un Vecteur2D
        return "Vecteur(%g, %g, %g)" % (self.x, self.y,self.z)


#print( dir (Vecteur3D))


#v1=Vecteur3D(20,3,2)
#v2=Vecteur3D(1,3,2)
#v3=Vecteur3D(19,3,2)


#print(-v1)
#print (v1 + v2 + v3)
#print (v1 - v2 )
#print(v1*10)
#print(v2*v1)
#print(v1**v2)

#print(v1.mod())
#print(v1.norm())
#v1.normed()
#print(v1.mod())
