class Repertoire(object):
    def __init__(self,nom="monRepertoire"):
        self.nom=nom
        self.contenu={}

    def __str__(self):
        msg="Repertoire("+ self.nom+")\n"+str(self.contenu)
        return msg


    def __repr__(self):
        msg = "Repertoire(" + self.nom + ")\n" + str(self.contenu)
        return msg


    def nouvelEntree(self,nom,numero):
        if type(nom)== str and \
        type(numero)== str and \
        nom not in self.contenu:
            self.contenu[nom]=[numero]
        elif type(nom)==str and \
        type(numero)==str and \
        nom in self.contenu:
            i=0
            newnom=nom+str(i)
            while nom + str(i) in self.contenu:
                i=i+1
                newnom= nom + str(i)
                self.contenu[newnom]=[numero]
           #self.contenu[nom].apprend(numero)
            else:
                print("erruer de format")

    def enleveEntree(nom):
        pass


if __name__ == "__main__":  # false lors d'un import
    Reppro=Repertoire('professionel')
    Reppro.nouvelEntree("111",'125643')
   # Reppro.nouvelEntree("Toto", '12574956643')
    Reppro.nouvelEntree("111", '125325665134643')

    print(Reppro)
    #Reppro.enleveEntree("Toto")

    print(Reppro)