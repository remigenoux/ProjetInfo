import numpy as  np

def scalaire(u,v):
    return u[0]*v[0]+u[1]*v[1]
def norme2(u):
    return (u[0]**2+u[1]**2)**0.5
# on définit le produit scalaire classique et la norme 2 pour les réutiliser plus tard

class Bille () : # cette classe définit le comportement des billes à l'intérieur du Billard, ce sont des objets à part entière

    def __init__(self,abscisse,ordonnee, couleur = 'Blanche' , vitesse=0,direction=(0,0),taille=5): # une bille a  : une position, une vitesse, une direction pour la vitesse et une taille
        self._taille = taille
        self.__coords = (abscisse,ordonnee)
        self.__v = vitesse
        self.direction = direction
        self.coul = couleur

    def __str__(self) :
        return "une bille {} de coordonnée {} de vitesse (norme,direction) {}{}".format(self.coul , (self.x,self.y) , self.v , self.direction)
    @property
    def x(self):
        return self.__coords[0]

    @property
    def y(self):
        return self.__coords[1]
    @property
    def coords(self):
        return self.__coords
    @coords.setter
    def coords(self,nouv_coords):
        x,y,valmax = nouv_coords
        if x > valmax[0] - self._taille :
            x = valmax[0] - self._taille
        if x < self._taille:
            x =  self._taille
        if y > valmax[1] - self._taille :
            y = valmax[1] - self._taille
        if y < self._taille:
            y =  self._taille
        self.__coords = (x , y)

    def coul(self): # la couleur par défaut est Blanche
        return 'Blanche'
    @property
    def v(self):
        return(self.__v)
    @v.setter
    def v(self,valeur_vitesse):
        if valeur_vitesse <= 5 :
            self.__v = 0
        else :
            self.__v = valeur_vitesse
    def attenuation(self):          # quand une bille heurte un autre objet (bille, billard) elle subit une atténuation de sa vitesse qui la conduit à s'arrêter
        self.v -= 20

    def axe(self, boule2):                      # cette fonction définit le vecteur porteur de l'axe passant par les deux centres de gravités des billes, orienté dans le sens de la vitesse (produit scalaire positif), il est utile pour défnir la direction de la vitesse d'une boule immobile après un contact
        axe = (self.x-boule2.x,self.y-boule2.y) # on calcule le vecteur porteur de l'axe
        axe = (axe[0]/ norme2(axe),axe[1]/ norme2(axe))     # on normalise ce vecteur
        return axe



    def contact_boule(self,boule2):
        self.attenuation
        print('je dois pas être la')
        axe = self.axe(boule2)

        if boule2.v != 0 :

            vitesse_2_ref1 = (boule2.v*boule2.direction[0],boule2.v*boule2.direction[1])
            vitesse_1_ref1 = (self.v*self.direction[0],self.v*self.direction[0])


            vitesse_1_ref2 = (vitesse_1_ref1[0] - vitesse_2_ref1[0],vitesse_1_ref1[1] - vitesse_2_ref1[1])  #passage dans le référentiel de la boule 2
            #la boule 2 est immobile dans le référentiel 2

            norme_vitesse_1_ref2 = norme2(vitesse_1_ref2)
            direction_vitesse_1_ref2 =( vitesse_1_ref2[0]/norme_vitesse_1_ref2 , vitesse_1_ref2[1]/norme_vitesse_1_ref2)

            if scalaire(axe, direction_vitesse_1_ref2) < 0:  # on le met dans le sens de la vitesse
                axe = (-axe[0],-axe[1])

            vitesse_2_ref2_apres_contact = (scalaire(axe,direction_vitesse_1_ref2) * vitesse_1_ref2[0] , scalaire(axe,direction_vitesse_1_ref2) * vitesse_1_ref2[1])
            vitesse_1_ref2_apres_contact = ((direction_vitesse_1_ref2[0] - axe[0]) / norme2((direction_vitesse_1_ref2[0] - axe[0], direction_vitesse_1_ref2[1] - axe[1])) * (1-scalaire(axe,direction_vitesse_1_ref2) ) * norme_vitesse_1_ref2,
                                            (direction_vitesse_1_ref2[1] - axe[1]) / norme2((direction_vitesse_1_ref2[0] - axe[0],direction_vitesse_1_ref2[1] -axe[1])) * (1-scalaire(axe,direction_vitesse_1_ref2) ) * norme_vitesse_1_ref2)

            vitesse_2_ref1_apres_contact = (vitesse_2_ref2_apres_contact[0] + vitesse_2_ref1[0] , vitesse_2_ref2_apres_contact[1] + vitesse_2_ref1[1])
            vitesse_1_ref1_apres_contact = (vitesse_1_ref2_apres_contact[0] + vitesse_2_ref1[0] , vitesse_1_ref2_apres_contact[1] + vitesse_2_ref1[1])

            boule2.v = norme2(vitesse_2_ref1_apres_contact)
            if boule2.v != 0 :
                boule2.direction = (vitesse_2_ref1_apres_contact[0]/boule2.v , vitesse_2_ref1_apres_contact[1]/boule2.v)


            self.v = norme2(vitesse_1_ref1_apres_contact)
            self.direction =  (vitesse_1_ref1_apres_contact[0]/self.v , vitesse_1_ref1_apres_contact[1]/self.v)

        elif boule2.v == 0 :
            if scalaire(axe, self.direction) < 0:  # on le met dans le sens de la vitesse
                axe = (-axe[0],-axe[1])
            boule2.v = scalaire(axe,self.direction) * self.v  # on a ommis la division par le produit des normes des directions qui doit être égal à 1
            boule2.direction = axe
            self.v = self.v * (1 - abs(scalaire(axe, self.direction)))
            self.direction = ((self.direction[0] - axe[0])/ norme2((self.direction[0] - axe[0] , self.direction[1] - axe[1])),(self.direction[1] - axe[1])/ norme2((self.direction[0] - axe[0] , self.direction[1] - axe[1])))

            print('scalaire',scalaire(axe,self.direction), norme2(self.direction))
        if self.coul == 'Blanche' :
            boule2.coul = self.attribut
        if boule2.coul == 'Blanche' :
            self.coul = boule2.attribut




    def contact_mur(self,valmax):  # cette fonction sert à modéliser le comportement d'une bille après un contact sur une bande
        xmax,ymax = valmax
          # la vitesse est atténuée comme après chaque choc
        x, y = self.x, self.y
        r = self._taille
        cote = []
        if x <= r:
            cote.append('g')
        if x >= xmax - r:
            cote.append('d')
        if y <= r:
            cote.append('b')
        if y >= ymax - r:
            cote.append('h')
        print('cote =',cote)
        for e in cote:  # Pour chaque rebond sur chaque côté, la bande renvoie parfaitement la composante normale de la vitesse qu'elle a reçu ( elle la transforme en son opposée)
            if e == 'g' or e == 'd':
                self.direction = (- self.direction[0], self.direction[1])
                self.attenuation()
                print('je change dir x ')
            if e == 'h' or e == 'b':
                self.direction = (self.direction[0], - self.direction[1])
                self.attenuation()
                print('je change direction y ')


class Blanche (Bille):          # Cette sous classe hérite de Bille et décrit plus particulièrement la bille Blanche
    def __init__(self,abscisse,ordonnee,attribut, couleur = 'Blanche',vitesse=0,direction=(0,0),taille=5):
        super().__init__(abscisse,ordonnee,couleur, vitesse,direction,taille)
        self.attribut = attribut    # On rajoute un attribut à la bille blanche puisqu'elle peut être jouée soit par le joueur Rouge soit par le joueur Bleu
                                    # son comportement dans un cas ou dans l'autre sera différent
class Bleue (Bille):# Cette sous classe hérite de Bille et décrit plus particulièrement la bille Bleue
    def __init__(self,abscisse,ordonnee,couleur = 'Bleue',vitesse=0,direction=(0,0),taille=5):
        super().__init__(abscisse,ordonnee,couleur,vitesse,direction,taille)
        self.coul = couleur
    #def coul(self):
    #    return 'Bleue'
class Rouge (Bille):# Cette sous classe hérite de Bille et décrit plus particulièrement la bille Rouge
    def __init__(self,abscisse,ordonnee,couleur = 'Rouge',vitesse=0,direction=(0,0),taille=5):
        super().__init__(abscisse,ordonnee,couleur,vitesse,direction,taille)
        self.coul = couleur
    #def coul(self):
    #   return 'Rouge'
if __name__ == "__main__":
    bille = Bleue(3,4,'Bleue', 25,(12,13))
    #print(bille)
    bille.coords= ((110,4,(100,100)))
