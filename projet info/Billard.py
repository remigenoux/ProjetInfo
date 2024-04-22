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
                if dist(self[j].coords,(x1,y1))<r :
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
        """force = input("veuillez entrer une vitesse")
        x = input("veuillez entrer une direction x")
        y = input ("veuillez entrer une direction y")
        try
            force = int(force)
            direction = (int(x),int(y))
        except ValueError:
            print("Vous n'avez pas répondu correctement aux questions")
        Blanche.attribut = J"""


        #   on attribue la sous couleur "bleue ou rouge"
        #   on met la boule blanche dans la liste mouvement
        #   tant que au moins une bille est en mouvement : simulation()
        #   on récupère les nouvelles positions
        return 0

    def simulation(self):
        # On définit un pas de temps
        # on étudie les positions de toutes les billes en mouvement (liste) après ce pas de temps
        # on étbalit les potentiels contacts
        # on établit le temps des contacts
        # on gère le contacts avec les fonctions qu'on connaît déjà
        # on avance toute la simulation du temps
        # on
        return 0


    def partie(self):
        nbr = input("Voulez-vous jouer contre l'ordinateur ? (1=oui,2=non)")
        try:
            Joueur = int(nbr)
            print("La valeur entree est un entier = ", val)
        except ValueError:
            print("Vous n'avez pas répondu correctement à la question")
        tour=1
        J = 'Bleu'
        while not self.fin_partie():
            print("c'est le tour",tour,"c'est à ",J,"de jouer")
            self.UnTour(J)
            if val == 1 :
                if J == 'Bleu':
                    J='Rouge'
                else :
                    J = 'Bleu'
            elif val == 2 :
                if J == 'Bleu':
                    J='IA'
                else :
                    J = 'Bleu'
            tour+=1





