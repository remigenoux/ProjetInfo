from numpy.random import randint
from sympy.solvers import solve
from sympy import Symbol
from operator import itemgetter

from Billes import *
from nouvelle_animation import *
"""on importe les classes associées au billes pour 
pouvoir directement les manipuler sur le Billard"""

def dist(u,v):
    return ((u[0]-v[0])**2+(u[1]-v[1])**2)**0.5

""" définition classique de la distance pour éviter de devoir
refaire le calcul à chaque fois"""

class Billard (list):
    def __init__(self,xmax,ymax,nb_billes,dt):
        self.xmax = xmax
        self.ymax = ymax
        self.dt = dt
        nb_billes += nb_billes % 2
        self.append(Blanche(xmax//2 , ymax//2,'Bleue'))
        r= self[0]._taille

                            #on initialise un Billard avec une taille propre et qui est géré par un pas de temps
                            #Le nombre de bille Bleue ou Rouge est choisi pair (si non on le remet pair) et la blanche
                            #définit le premier élément de Billard

        while len(self)<=(nb_billes/2):
            x1,y1 = randint(r , xmax-r), randint(r , ymax-r )
            deja_pris = False
            for j in range (len(self)):
                if dist((self[j].x,self[j].y),(x1,y1))<2 * r :
                    deja_pris = True
            if not deja_pris :
                print((x1, y1))
                self.append(Bleue(x1,y1))

                            #on remplit le billard de Bleue (jusqu'à la moitié du nombre de bille à jouer)
                            #de sorte à ce qu'elles ne se chevauchent pas

        while len(self) <= (nb_billes):
            x2,y2 = randint(r, xmax-r) , randint(r, ymax-r)
            deja_pris = False
            for j in range(len(self)):
                if dist((self[j].x,self[j].y) , (x2,y2)) < 2 * r:
                    deja_pris = True
            if not deja_pris:
                print((x2,y2))
                self.append(Rouge(x2,y2))
                            #De même avec les rouges, qui ne chevauchent ni les rouges ni les Bleues


    def __str__(self):
        return "le billard fait {}cm par {}cm".format(self.xmax,self.ymax)

    def partie(self,Joueur):  # la fonction précédente aurait pu être une classe en elle même mais elle définit comment la partie se déroule au sein du Billard

        tour = 1  # initialise le nombre de tour à 1
        J = 'Bleue'  # le joueur 1 joue les Bleues par défaut

        while not self.fin_partie():  # La partie continue jusqu'à ce que la partie se finisse, jusque là, rien d'inquétant

            print("c'est le tour", tour, "c'est à ", J, "de jouer")
            print(J)
            self.UnTour(J, self.dt)  # un tour se déroule avec demande de coup & simulation

            if Joueur == 1:  # changement de joueur sur le prochain coup
                if J == 'Bleue':
                    J = 'Rouge'
                else:
                    J = 'Bleue'

            elif Joueur == 2:
                if J == 'Bleue':
                    J = 'IA'
                else:
                    J = 'Bleue'

            tour += 1
        print("Bravo ! ")

    def fin_partie(self):  # cette fonction sert à déterminer si la partie est finie ou non ( si toutes les billes sont de la même couleur)
        fin = True
        color = self[1].coul  # prends la première couleur

        for e in self :  # si un bille a une couleur différente, le jeu n'est pas fini

            if e.coul != 'Blanche' and e.coul != color:
                fin = False

        if fin:
            animation_fin(self,color)
        return fin  # renvoie un booléen qui répond à la question : la partie est-elle finie ?
    def UnTour(self,J,dt):

        if J == 'IA' :
            self[0].attribut = 'Rouge'                  #   on attribue la sous couleur "rouge" le joueur jouant les bleues par défaut
            force,x,y = self.coup_intelligent()         # joue le coup de l'IA

        else :
            self[0].attribut = J
            force, direction = prends_les_infos(self)
        self[0].v = force                                                       # on applique les choix à la blanche pour pouvoir lancer la simulation
        self[0].direction = direction
        anim_list = self.simulation(dt)   # le billard s'actualise d'un instant à l'autre avec la fonction simulation
        animation_billard(self,anim_list)
    def avancer(self,temps,anim_list,i):
        valmax = (self.xmax,self.ymax)
        for e in self:
            e.coords = (e.x + e.direction[0] * e.v * temps , e.y + e.direction[1] * e.v * temps, valmax)
            e.v -= 0.05
            anim_list[i].append([e.x , e.y , valmax,e.coul])

    def simulation(self,dt):
        valmax = (self.xmax,self.ymax)
        mouvement = [0]
        anim_list = []
        i=0
        while len(mouvement) != 0 :

            clone = []
            for e in self :
                clone.append((e.x + e.v * e.direction[0]  *dt, e.y + e.v * e.direction[1]  * dt,e.v,e.direction, e._taille, self.index(e),e.coul))
            list_collisions = self.collisions(clone,dt)
            print(list_collisions)



            if len(list_collisions)!=0 :
                sorted(list_collisions, key=itemgetter(2))
                boule_1 = list_collisions[0][0]
                obstacle = list_collisions[0][1]
                temps_mini = list_collisions[0][2]
                print('obstacle=', obstacle)
                print('temps mini = ', temps_mini)



                if obstacle == -1 :
                    print('coords=', self[boule_1].coords)
                    self[boule_1].contact_mur(valmax)
                else :
                    self[boule_1].contact_boule(self[obstacle])
                anim_list.append([temps_mini])
                self.avancer(temps_mini, anim_list, i)
            else :
                anim_list.append([dt])
                self.avancer(dt,anim_list,i)
            i += 1
            print('i',i)

            mouvement = []
            for j in range(len(self)):
                if self[j].v != 0 :
                    mouvement.append(j)
        return anim_list

    def collisions(self,clone,dt):
        collisions = []
        r = clone[0][4]
        for i in range(len(clone)):

            if clone[i][0] > self.xmax-r :
                if clone[i][3][0] != 0 and clone[i][2]!=0 :
                    temps_impact = (self.xmax - r - clone[i][0]) / (clone[i][3][0] * clone[i][2])
                    collisions.append((i,-1,-temps_impact))

            if clone[i][0] < r  :
                if clone[i][3][0] != 0 and clone[i][2] != 0 :
                    temps_impact = (r - clone[i][0]) / (clone[i][3][0] * clone[i][2])
                    collisions.append((i,-1,-temps_impact))

            if clone[i][1] > self.ymax-r :
                if clone[i][3][1] != 0 and clone[i][2]!=0 :
                    temps_impact = (self.ymax - r - clone[i][1]) / (clone[i][3][1] * clone[i][2])
                    collisions.append((i,-1,-temps_impact))

            if clone[i][1] < r:
                if clone[i][3][1] != 0 and clone[i][2] != 0:
                    temps_impact = (r - clone[i][1]) / (clone[i][3][1] * clone[i][2])
                    collisions.append((i, -1, -temps_impact))

        clone = sorted(clone, key = itemgetter(0))
        print(clone,self[0].attribut)
        for i in range(len(clone)-1):
            d=1
            if i+d < len(clone) :
                if abs(clone[i][0]-clone[i+d][0])< 2 * r :
                    if dist((clone[i][0] , clone[i][1]) , (clone[i+d][0] , clone[i+d][1])) < 2 * r :
                        temps_collision = self.temps_col(clone[i],clone[i+d],dt)
                        collisions.append((clone[i][5],clone[i+d][5],temps_collision))
                    d+=1
                    print('d=',d)
        return collisions

    def temps_col(self,clone1,clone2,dt):
        r = clone1[4]
        tcol = Symbol("tcol")  # Définition de la variable qu'on recherche dans nos équations
        tcol = solve((clone1[0] + clone1[2] * tcol * clone1[3][0] - (
                    clone2[0] + clone2[2] * tcol * clone2[3][0])) ** 2 + (
                                 clone1[1] + clone1[2] * tcol * clone1[3][1] - (
                                     clone2[1] + clone2[2] * tcol * clone2[3][1])) ** 2 - 4 * r ** 2, tcol)

        # la ligne précédente calcule le temps précis auquel à lieu la collision. On aura pourra ainsi déterminer la position et la vitesse des deux billes après la collision au prochain rafraîchissement du Billard
        print("tcol c'est",tcol,clone1,clone2)
        if len(tcol)==0 :
            tcol = 1e-2
        else :
            tcol = min(dt,abs(tcol[0]), abs(tcol[1]))

        return tcol

if __name__ == "__main__":
    n,x,y,j = intro()
    billard = Billard(x,y,n,1/60)
    billard.partie(j)





