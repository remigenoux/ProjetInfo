import numpy as np

from Billard import *


def scalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]


def norme(u):
    return np.sqrt(u[0] ** 2 + u[1] ** 2)


class Bille():

    def __init__(self, abscisse, ordonnee, vitesse=0, direction=(0, 0), taille=5):
        self._taille = taille
        self.coords = (abscisse, ordonnee)
        self.v = vitesse
        self.direction = direction

    def __str__(self):
        return self.coul, self.coords, self.v

    def x(self):
        return self.direction[0]

    def y(self):
        return self.direction[1]

    def coul(self):
        return 'B'

    def attenuation(self):
        self.v = self.v - 20
        if self.v < 0:
            self.v = 0
        return self.v

    def axe(self, boule2):
        axe = (self.x - boule2.x, self.y - boule2.y)
        axe = axe / norme(axe)
        if scalaire(axe, self.direction) < 0:
            axe = -axe
        return axe

    def contact_boule_immobile(self, boule2):
        axe = self.axe(boule2)
        if self.attenuation() <= 0:
            boule2.x += axe[0]
            boule2.y += axe[1]
        else:
            self.v = self.attenuation()
            boule2.v = scalaire(axe, self.direction) * self.v
            boule2.direction = axe
            self.direction = (self.direction - axe) / norme(self.direction - axe)

    def contact_boule_mobile(self, boule2):
        axe = self.axe(boule2)
        # if self.attenuation() <= 0:
        #     if boule2.attenuation() <= 0:
        #         self.x += axe[0]
        #         self.y += axe[1]
        #         boule2.x -= axe[0]
        #         boule2.y -= axe[1]
        #     else:
        #         boule2.contact_boule_immobile(self)
        # else:
        #     if boule2.attenuation() <= 0:
        #         self.contact_boule_immobile(boule2)
        #     else:
        self.v = self.attenuation() - (scalaire(self.attenuation() - boule2.attenuation(), axe)) / norme(axe)
        boule2.v = boule2.attenuation() - (scalaire(boule2.attenuation() - self.attenuation(), axe)) / norme(axe)
        self.direction = (self.direction + boule2.direction - axe) / norme(self.direction + boule2.direction - axe)
        boule2.direction = (boule2.direction + self.direction + axe) / norme(
            boule2.direction + self.direction + axe)

    def contact_mur(self):
        self.v = self.attenuation()
        x, y = self.x, self.y
        r = self.taille
        cote = []
        if x <= r:
            cote.append('g')
        if x >= Billard.xmax - r:
            cote.append('d')
        if y <= r:
            cote.append('b')
        if y >= Billard.ymax - r:
            cote.append('h')
        for e in cote:
            if e == 'g' or e == 'd':
                self.x = - self.x
            if e == 'h' or e == 'b':
                self.y = -self.y


class Blanche (Bille):
    def __init__(self,abscisse,ordonnee,attribut,vitesse=0,direction=(0,0),taille=5):
        super().__init__(abscisse,ordonnee,vitesse,direction,taille)
        self.attribut = attribut


class Bleue(Bille):
    def coul(self):
        return 'Bleue'


class Rouge(Bille):
    def coul(self):
        return 'Rouge'



