import numpy as np
import time
from numpy.random import randint


from Billes import *
def dist(u,v):
    return np.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)

class Billard (list):
    def __init__(self,xmax,ymax,nb_billes):
        self.xmax = xmax
        self.ymax = ymax
        nb_billes += nb_billes%2
        self.append(Blanche(xmax//2,ymax//2))
        r= Bille.taille
        while len(self)<=(nb_billes/2):
            x1,y1 = randint(0+r, xmax-r), randint(0+r, ymax-r )
            Plein=False
            for j in range (len(self)):
                if dist(self[j],(x1,y1))<r :
                    Plein = True
            if not Plein :
                self.append(Bleue(x1,y1))
        while len(self) <= (nb_billes):
            x2,y2 = randint(0+r, xmax-r ), randint(0+r, ymax-r)
            Plein = False
            for j in range(len(self)):
                if dist(self[j], (x2,y2)) < r:
                    Plein = True
            if not Plein:
                self.append(Rouge(x2, y2))
    def UnTour(self,J):
        return 0

    def simuler(self):
        tour=1
        J = 'Bleu'
        while not self.fin_partie():
            print("c'est le tour",tour)
            self.UnTour(J)
            if J == 'Bleu':
                J='Rouge'
            else :
                J = 'Bleu'
            tour+=1





