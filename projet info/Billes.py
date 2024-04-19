import numpy as  np
from matplotlib.pyplot as plt

def scalaire(u,v):
    return u[0]*v[0]+u[1]*v[1]
def norme(u)
    return np.sqrt(u[0]**2+u[1]**2)

class Bille () :

    def __init__(self,abscisse,ordonnee,vitesse=0,direction=(0,0),taille=5):
        self._taille = taille
        self.coords = (abscisse,ordonnee)
        self.v = vitesse
        self.direction = direction


    def __str__(self) :
        return (self.coul,self.coords,self.v)

    def coul(self):
        return 'B'

    def attenuation(self):
        self.v = self.v - 20
        if self.v < 0 :
            self.v = 0
        return self.v

    def axe(self, boule2):
        axe = (self.x-boule2.x,self.y-boule2-y)
        axe = axe/norme(axe)
        if scalaire(axe,direction) < 0 :
            axe = -axe
        return axe

    def contact_boule(self, boule2):
        axe = axe(self,boule2)
        if self.attenuation() == 0 :
            boule2.x += axe[0]
            boule2.y += axe[1]
        else :
            self.v = self.attenuation()
            boule2.v = scalaire(axe,self.direction)*self.v
            boule2.direction = axe
            self.direction = (self.direction-axe)/norme(self.direction-axe)
class Blanche (Bille):
    def coul(self):
        return 'Blanche'
class Bleue (Bille):
    def coul(self):
        return 'Bleue'
class Rouge (Bille):
    def coul(self):
        return 'Rouge'


