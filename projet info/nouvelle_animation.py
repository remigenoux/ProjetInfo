import math

import numpy as np
import pygame
from sys import exit
from math import atan
screen_x = 1000
screen_y = 600


def norme2(u):
    return (u[0]**2+u[1]**2)**0.5

def couple_degre(u):

    if u[1] !=0 :
        cap = 180/np.pi*math.atan(u[0]/u[1])
        if u[1]< 0 :
            cap+=180
        if u[1]>0 and u[0]<0 :
            cap+= 360
    if u[1]== 0 :
        if u[0]<0 :
            cap = 180
        else :
            cap = 0
    return int(cap)

def english_color(color):
    if color == 'Bleue':
        return 'blue'
    if color == 'Rouge':
        return  'red'
    else :
        return 'white'
#interface canne au centre, bille qui bouge
def intro_afficher_queue(u, longueur):
    longueur_queue = longueur
    x, y = u
    x -= 400
    y -= 250
    v = (x, y)
    norme = norme2(v)
    dir_v = (v[0] / norme, v[1] / norme)
    if norme == 0:
        norme = 1e-3
    x = 400 + int(dir_v[0] * longueur_queue)
    y = 250 + int(dir_v[1] * longueur_queue)
    return (x, y)

#interface placer bille au bout
def intro_placer_bille(u, longueur):
    longueur_queue = longueur
    x, y = u
    x -= 400
    y -= 250
    v = (x, y)
    norme = norme2(v)
    dir_v = (v[0] / norme, v[1] / norme)
    if norme == 0:
        norme = 1e-3
    x = 400 + int(dir_v[0] * longueur_queue) - 10
    y = 250 + int(dir_v[1] * longueur_queue) - 10
    return (x, y)

#interface placer fleche direction + force
def infos_placer_fleche (mouse,blanche):
    x, y = mouse
    x -= blanche[0]
    y -= blanche[1]
    v = (x, y)
    norme = norme2(v)
    if norme == 0:
        norme = 1e-3
    dir_v = (v[0] / norme, v[1] / norme)
    if norme > 200 :
        norme = 200
    x = blanche[0] + int(dir_v[0] * norme)
    y = blanche[1] + int(dir_v[1] * norme)
    return (x, y), norme

#interface afficher queue qui suit la bille
def infos_afficher_queue(mouse,blanche,longueur_queue):
    x, y = mouse
    x -= blanche[0]
    y -= blanche[1]
    v = (x, y)
    norme = norme2(v)
    if norme == 0:
        norme = 1e-3
    dir_v = (v[0] / norme, v[1] / norme)
    x = blanche[0] - int(dir_v[0] * longueur_queue)
    y = blanche[1] - int(dir_v[1] * longueur_queue)
    return (x, y)

#interface + renvoie nombrebille,xmax,ymax,joueur
def intro():
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    pygame.display.set_caption('Bounce Box')
    clock = pygame.time.Clock()

    intro_font = pygame.font.Font('Super Squad.ttf', 20)


    surface_fond = pygame.Surface((800,500))
    surface_fond.fill('#743B24')
    surface_fond_rect = surface_fond.get_rect(center = (400,250))

    surface_billard = pygame.Surface((400,400))
    surface_billard.fill('#2A6E2D')
    surface_billard_rect = surface_billard.get_rect(center = (400,250))

    surface_4 = pygame.Surface((100,50))
    surface_4.fill('Grey')
    surface_4_rect = surface_4.get_rect(center = (400,50))

    surface_4_rouge = pygame.Surface((105, 55))
    surface_4_rouge.fill('red')
    surface_4_rouge_rect = surface_4_rouge.get_rect(center=(400, 50))

    surface_10 = pygame.Surface((100,50))
    surface_10.fill('Grey')
    surface_10_rect = surface_10.get_rect(center = (200,250))

    surface_10_rouge = pygame.Surface((105, 55))
    surface_10_rouge.fill('red')
    surface_10_rouge_rect = surface_10_rouge.get_rect(center=(200,250))

    surface_6 = pygame.Surface((100,50))
    surface_6.fill('Grey')
    surface_6_rect = surface_6.get_rect(center = (600,250))

    surface_6_rouge = pygame.Surface((105, 55))
    surface_6_rouge.fill('red')
    surface_6_rouge_rect = surface_6_rouge.get_rect(center=(600,250))

    surface_8 = pygame.Surface((100,50))
    surface_8.fill('Grey')
    surface_8_rect = surface_8.get_rect(center = (400,450))

    surface_8_rouge = pygame.Surface((105, 55))
    surface_8_rouge.fill('red')
    surface_8_rouge_rect = surface_8_rouge.get_rect(center=(400, 450))

    surface_ami = pygame.Surface((100, 50))
    surface_ami.fill('Grey')
    surface_ami_rect = surface_ami.get_rect(center=(200, 250))

    surface_ami_rouge = pygame.Surface((105, 55))
    surface_ami_rouge.fill('red')
    surface_ami_rouge_rect = surface_ami_rouge.get_rect(center=(200,250))

    surface_IA = pygame.Surface((100, 50))
    surface_IA.fill('Grey')
    surface_IA_rect = surface_IA.get_rect(center=(600, 250))

    surface_IA_rouge = pygame.Surface((105, 55))
    surface_IA_rouge.fill('red')
    surface_IA_rouge_rect = surface_IA_rouge.get_rect(center=(600,250))


    nb_boule_4 = intro_font.render('4 Billes',False,'black')
    nb_boule_4_rect = nb_boule_4.get_rect(center = (400,50))

    nb_boule_6 = intro_font.render('6 Billes',False,'black')
    nb_boule_6_rect = nb_boule_6.get_rect(center = (600,250))

    nb_boule_8 = intro_font.render('8 Billes',False,'black')
    nb_boule_8_rect = nb_boule_8.get_rect(center = (400,450))

    nb_boule_10 = intro_font.render('10 Billes',False,'black')
    nb_boule_10_rect = nb_boule_10.get_rect(center = (200,250))

    txt_ami = intro_font.render('Versus', False, 'black')
    txt_ami_rect = txt_ami.get_rect(center=(200, 250))

    txt_IA = intro_font.render('IA', False, 'black')
    txt_IA_rect = txt_IA.get_rect(center=(600, 250))

    blanche = pygame.Surface((20,20), pygame.SRCALPHA)
    pygame.draw.circle( blanche , 'white', (10,10), 7)


    animation = False
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                for e in [surface_4_rect,surface_6_rect,surface_8_rect,surface_10_rect] :
                    if e.collidepoint(pygame.mouse.get_pos()) :
                        animation = True
                        point_arrivee = pygame.mouse.get_pos()
                        if e == surface_4_rect:
                            nb_billes = 4
                            xmax = 400
                            ymax = 266
                        elif e == surface_6_rect:
                            nb_billes = 6
                            xmax = 434
                            ymax = 300
                        elif e == surface_8_rect:
                            nb_billes = 8
                            xmax = 466
                            ymax = 333
                        elif e == surface_10_rect:
                            nb_billes = 10
                            xmax = 500
                            ymax = 368


        screen.blit(surface_fond,surface_fond_rect)
        screen.blit(surface_billard,surface_billard_rect)
        pygame.draw.lines(screen, 'black', True, [(200, 50), (200, 450), (600, 450), (600, 50)], 5)

        for e in [surface_4_rect, surface_6_rect, surface_8_rect, surface_10_rect]:
            if e.collidepoint(pygame.mouse.get_pos()):
                if e == surface_4_rect:
                    screen.blit(surface_4_rouge, surface_4_rouge_rect)
                if e == surface_6_rect:
                    screen.blit(surface_6_rouge, surface_6_rouge_rect)
                if e == surface_8_rect:
                    screen.blit(surface_8_rouge, surface_8_rouge_rect)
                if e == surface_10_rect:
                    screen.blit(surface_10_rouge, surface_10_rouge_rect)
        screen.blit(surface_4,surface_4_rect)
        screen.blit(surface_6, surface_6_rect)
        screen.blit(surface_8, surface_8_rect)
        screen.blit(surface_10, surface_10_rect)

        screen.blit(nb_boule_4,nb_boule_4_rect)
        screen.blit(nb_boule_6, nb_boule_6_rect)
        screen.blit(nb_boule_8, nb_boule_8_rect)
        screen.blit(nb_boule_10, nb_boule_10_rect)

        if not animation :
            pos = 110
            pygame.draw.line(screen,'#EEEC90',(400,250),intro_afficher_queue(pygame.mouse.get_pos(),100),5)
            pygame.draw.line(screen, 'black', (400, 250), intro_afficher_queue(pygame.mouse.get_pos(), 40), 5)
            screen.blit(blanche , intro_placer_bille(pygame.mouse.get_pos(), 110))
        else :
            pygame.draw.line(screen, '#EEEC90', (400, 250), intro_afficher_queue(pygame.mouse.get_pos(), 100), 5)
            pygame.draw.line(screen, 'black', (400, 250), intro_afficher_queue(pygame.mouse.get_pos(), 40), 5)
            screen.blit(blanche, intro_placer_bille(point_arrivee, pos))
            pos += 8
            coord = intro_placer_bille(point_arrivee,pos)
            if coord[0]<200 or coord[0]> 600 or coord[1]<50 or coord[1]>450:
                break
        pygame.display.update()
        clock.tick(60)

    animation = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for e in [surface_ami_rect, surface_IA_rect]:
                    if e.collidepoint(pygame.mouse.get_pos()):
                        animation = True
                        point_arrivee = pygame.mouse.get_pos()
                        if e == surface_ami_rect:
                            joueur = 1
                        elif e == surface_IA_rect:
                            joueur = 2


        screen.blit(surface_fond, surface_fond_rect)
        screen.blit(surface_billard, surface_billard_rect)
        pygame.draw.lines(screen, 'black', True, [(200, 50), (200, 450), (600, 450), (600, 50)], 5)

        for e in [surface_ami_rect,surface_IA_rect]:
            if e.collidepoint(pygame.mouse.get_pos()):
                if e == surface_ami_rect:
                    screen.blit(surface_ami_rouge, surface_ami_rouge_rect)
                if e == surface_IA_rect:
                    screen.blit(surface_IA_rouge, surface_IA_rouge_rect)

        screen.blit(surface_ami, surface_ami_rect)
        screen.blit(surface_IA, surface_IA_rect)

        screen.blit(txt_ami, txt_ami_rect)
        screen.blit(txt_IA, txt_IA_rect)

        if not animation:
            pos = 110
            pygame.draw.line(screen, '#EEEC90', (400, 250), intro_afficher_queue(pygame.mouse.get_pos(), 100), 5)
            pygame.draw.line(screen, 'black', (400, 250), intro_afficher_queue(pygame.mouse.get_pos(), 40), 5)
            screen.blit(blanche, intro_placer_bille(pygame.mouse.get_pos(), 110))
        else:
            pygame.draw.line(screen, '#EEEC90', (400, 250), intro_afficher_queue(pygame.mouse.get_pos(), 100), 5)
            pygame.draw.line(screen, 'black', (400, 250), intro_afficher_queue(pygame.mouse.get_pos(), 40), 5)
            screen.blit(blanche, intro_placer_bille(point_arrivee, pos))
            pos += 8
            coord = intro_placer_bille(point_arrivee, pos)
            if coord[0] < 200 or coord[0] > 600 or coord[1] < 50 or coord[1] > 450:
                break
        pygame.display.update()
        clock.tick(60)
    return nb_billes, xmax, ymax,joueur

#interface + renvoie force et direction
def prends_les_infos(billard) :
    pygame.init()
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption('Bounce Box')
    clock = pygame.time.Clock()

    intro_font = pygame.font.Font('Pixeltype.ttf', 20)
    intro_font2 = pygame.font.Font('Pixeltype.ttf', 35)


    surface_fond = pygame.Surface((screen_x,screen_y))
    surface_fond.fill('#743B24')
    surface_fond_rect = surface_fond.get_rect(center=(screen_x//2, screen_y//2))

    surface_billard = pygame.Surface((billard.xmax, billard.ymax))
    surface_billard.fill('#2A6E2D')
    surface_billard_rect = surface_billard.get_rect(center=(screen_x//2, screen_y//2))

    surface_stats = pygame.Surface((110, 120))
    surface_stats.fill('grey')
    surface_stats_rect = surface_stats.get_rect(center=(50, 100))

    txt_stats = intro_font2.render(
        f'STATS',False, 'black')
    txt_stats_rect = txt_stats.get_rect(center=(50, 70))

    blanche = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.circle(blanche, 'white', (10, 10), 7)

    surfaces_boules=[0]*(len(billard)-1)
    for i in range (1, len(billard)) :
        if billard[i].coul == 'Rouge' :
            couleur = 'red'
        else :
            couleur = 'blue'
        surfaces_boules[i-1] = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(surfaces_boules[i-1], couleur, (10, 10), 7)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                direction = ((pygame.mouse.get_pos()[0]-(billard[0].x+screen_x//2-billard.xmax//2))/norme2(((pygame.mouse.get_pos()[0]-(billard[0].x+screen_x//2-billard.xmax//2)),
                                (pygame.mouse.get_pos()[1]-(billard[0].y+screen_y//2-billard.ymax//2)))),(pygame.mouse.get_pos()[1]-(billard[0].y+screen_y//2-billard.ymax//2))/norme2(((pygame.mouse.get_pos()[0]-(billard[0].x+screen_x//2-billard.xmax//2)),
                                (pygame.mouse.get_pos()[1]-(billard[0].y+screen_y//2-billard.ymax//2)))))
                force = infos_placer_fleche(pygame.mouse.get_pos(),(billard[0].x+screen_x//2-billard.xmax//2 , billard[0].y+screen_y//2-billard.ymax//2))[1]
                return force,direction
                break

        txt_force = intro_font.render(
            f'force : {int(infos_placer_fleche(pygame.mouse.get_pos(), (billard[0].x+screen_x//2-billard.xmax//2, billard[0].y+screen_y//2-billard.ymax//2))[1])}', False, 'black')
        txt_force_rect = txt_force.get_rect(center=(50, 115))

        txt_direction = intro_font.render(
            f'cap : {couple_degre((pygame.mouse.get_pos()[0] - (billard[0].x+screen_x//2-billard.xmax//2), -(pygame.mouse.get_pos()[1] - (billard[0].y+screen_y//2-billard.ymax//2))))}', False,
            'black')

        txt_direction_rect = txt_direction.get_rect(center=(50, 150))
        screen.blit(surface_fond, surface_fond_rect)
        screen.blit(surface_billard, surface_billard_rect)
        screen.blit(surface_stats,surface_stats_rect)
        pygame.draw.lines(screen, 'black', True, [(screen_x//2-billard.xmax//2, screen_y//2-billard.ymax//2), (screen_x//2+billard.xmax//2, screen_y//2-billard.ymax//2), (screen_x//2+billard.xmax//2, screen_y//2+billard.ymax//2), (screen_x//2-billard.xmax//2, screen_y//2+billard.ymax//2)], 5)

        pygame.draw.line(screen, 'black', (int(billard[0].x) + screen_x//2 - billard.xmax//2 , int(billard[0].y) + screen_y//2 - billard.ymax//2), infos_afficher_queue(pygame.mouse.get_pos(),(int(billard[0].x)+screen_x//2-billard.xmax//2, int(billard[0].y)+screen_y//2-billard.ymax//2),100),  5)
        pygame.draw.line(screen, '#EEEC90', (int(billard[0].x)+screen_x//2-billard.xmax//2, int(billard[0].y)+screen_y//2-billard.ymax//2), infos_afficher_queue(pygame.mouse.get_pos(),(int(billard[0].x)+screen_x//2-billard.xmax//2, int(billard[0].y)+screen_y//2-billard.ymax//2),60),  5)

        for i in range(len(surfaces_boules)):
            screen.blit(surfaces_boules[i], (int(billard[i+1].x) -10 +screen_x//2-billard.xmax//2, int(billard[i+1].y) -10 +screen_y//2-billard.ymax//2))

        screen.blit(blanche, (int(billard[0].x) -10+screen_x//2-billard.xmax//2, int(billard[0].y)-10+screen_y//2-billard.ymax//2))
        pygame.draw.line(screen,'red',(int(billard[0].x)+screen_x//2-billard.xmax//2,int(billard[0].y)+screen_y//2-billard.ymax//2), infos_placer_fleche(pygame.mouse.get_pos(),(int(billard[0].x)+screen_x//2-billard.xmax//2,int(billard[0].y)+screen_y//2-billard.ymax//2))[0]  )
        screen.blit(txt_stats,txt_stats_rect)
        screen.blit(txt_force,txt_force_rect)
        screen.blit(txt_direction,txt_direction_rect)

        pygame.display.update()
        clock.tick(60)


def animation_billard(billard,anim_list):
    pygame.init()
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption('Bounce Box')
    clock = pygame.time.Clock()

    intro_font = pygame.font.Font('Super Squad.ttf', 20)

    surface_fond = pygame.Surface((screen_x, screen_y))
    surface_fond.fill('#743B24')
    surface_fond_rect = surface_fond.get_rect(center=(screen_x//2, screen_y//2))

    surface_billard = pygame.Surface((billard.xmax, billard.ymax))
    surface_billard.fill('#2A6E2D')
    surface_billard_rect = surface_billard.get_rect(center=(screen_x//2, screen_y//2))

    surface_vitesse = pygame.Surface((100, 50))
    surface_vitesse.fill('Grey')
    surface_vitesse_rect = surface_vitesse.get_rect(center=(800, 50))

    txt_vitesse1 = intro_font.render('x1', True, 'black')
    txt_vitesse1_rect = txt_vitesse1.get_rect(center=(800, 50))

    txt_vitesse2 = intro_font.render('x2',True,'black')
    txt_vitesse2_rect = txt_vitesse2.get_rect(center=(800, 50))

    txt_vitesse3 = intro_font.render('x3', True, 'black')
    txt_vitesse3_rect = txt_vitesse3.get_rect(center=(800, 50))


    blanche = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.circle(blanche, 'white', (10, 10), 7)


    temps_match= 0
    k = 0
    vitesse = 1
    while True and k < len(anim_list):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if surface_vitesse_rect.collidepoint(pygame.mouse.get_pos()):
                    vitesse += 1

        txt_temps = intro_font.render(
            f'temps : {int(temps_match)}', False,
            'black')
        txt_temps_rect = txt_temps.get_rect(center=(50, 100))



        screen.blit(surface_fond, surface_fond_rect)
        screen.blit(surface_billard, surface_billard_rect)
        pygame.draw.lines(screen, 'black', True, [(screen_x//2 - billard.xmax // 2, screen_y//2 - billard.ymax // 2),
                                                  (screen_x//2 + billard.xmax // 2, screen_y//2 - billard.ymax // 2),
                                                  (screen_x//2 + billard.xmax // 2, screen_y//2 + billard.ymax // 2),
                                                  (screen_x//2 - billard.xmax // 2, screen_y//2 + billard.ymax // 2)], 5)

        surfaces_boules = [0] * (len(billard) - 1)
        for i in range(1, len(billard)):
            surfaces_boules[i - 1] = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(surfaces_boules[i - 1], english_color(anim_list[k][i+1][3]), (10, 10), 7)

        for i in range(2,len(anim_list[k])):
            screen.blit(surfaces_boules[i-2], (int(anim_list[k][i][0] - 10+screen_x//2-billard.xmax//2), int(anim_list[k][i][1] - 10+screen_y//2-billard.ymax//2)))
        temps_match+= anim_list[k][0]

        screen.blit(blanche, (int(anim_list[k][1][0]- 10+screen_x//2-billard.xmax//2), int(anim_list[k][1][1] - 10+screen_y//2-billard.ymax//2)))
        k += 1
        screen.blit(surface_vitesse,surface_vitesse_rect)
        if (vitesse-1)%3 +1 == 1 :
            screen.blit(txt_vitesse1,txt_vitesse1_rect)
        elif (vitesse - 1) % 3 + 1 == 2:
            screen.blit(txt_vitesse2, txt_vitesse2_rect)
        else :
            screen.blit(txt_vitesse3,txt_vitesse3_rect)
        screen.blit(txt_temps, txt_temps_rect)
        pygame.display.update()
        clock.tick(80 * ((vitesse-1)%3+1))
    print('<3')
def animation_fin(billard,color):
    pygame.init()
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption('Bounce Box')
    clock = pygame.time.Clock()

    intro_font = pygame.font.Font('BADABB__.TTF', 100)
    intro_font2 = pygame.font.Font('Super Squad.ttf', 20)

    surface_fond = pygame.Surface((screen_x, screen_y))
    surface_fond.fill('#743B24')
    surface_fond_rect = surface_fond.get_rect(center=(screen_x//2, screen_y//2))

    surface_billard = pygame.Surface((billard.xmax, billard.ymax))
    surface_billard.fill('#2A6E2D')
    surface_billard_rect = surface_billard.get_rect(center=(screen_x//2, screen_y//2))
    liste_carre =[]

    surface_rejoue = pygame.Surface((100, 50))
    surface_rejoue.fill('Grey')
    surface_rejoue_rect = surface_rejoue.get_rect(center=(800, 500))

    for i in range(4):
        surface_noir = pygame.Surface((screen_x //4, screen_y //4))
        surface_noir.fill('black')
        surface_noir_rect = surface_noir.get_rect(topleft=(screen_x //4*i, 0))
        liste_carre.append([surface_noir,surface_noir_rect])
    for i in range(1,4):
        surface_noir = pygame.Surface((screen_x // 4, screen_y // 4))
        surface_noir.fill('black')
        surface_noir_rect = surface_noir.get_rect(topleft=(screen_x // 4*3, screen_y // 4 *i))
        liste_carre.append([surface_noir, surface_noir_rect])
    for i in [2,1,0]:
        surface_noir = pygame.Surface((screen_x // 4, screen_y // 4))
        surface_noir.fill('black')
        surface_noir_rect = surface_noir.get_rect(topleft=(screen_x // 4 * i, screen_y // 4 * 3))
        liste_carre.append([surface_noir, surface_noir_rect])
    for i in [2,1]:
        surface_noir = pygame.Surface((screen_x // 4, screen_y // 4))
        surface_noir.fill('black')
        surface_noir_rect = surface_noir.get_rect(topleft=(0, screen_y // 4 * i))
        liste_carre.append([surface_noir, surface_noir_rect])
    for i in range(1,3):
        surface_noir = pygame.Surface((screen_x // 4, screen_y // 4))
        surface_noir.fill('black')
        surface_noir_rect = surface_noir.get_rect(topleft=(screen_x // 4 * i, screen_y//4))
        liste_carre.append([surface_noir, surface_noir_rect])
    for i in [2,1]:
        surface_noir = pygame.Surface((screen_x // 4, screen_y // 4))
        surface_noir.fill('black')
        surface_noir_rect = surface_noir.get_rect(topleft=(screen_x // 4 * i, screen_y // 4*2))
        liste_carre.append([surface_noir, surface_noir_rect])

    blanche = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.circle(blanche, 'white', (10, 10), 7)


    txt_fin = intro_font.render(
        f' And the winner is {color}  !', False,
        english_color(color))
    txt_fin_rect = txt_fin.get_rect(center=(screen_x//2, 200))

    txt_fin2 = intro_font.render(
        f' Nice Job !', False,
        english_color(color))
    txt_fin2_rect = txt_fin2.get_rect(center=(screen_x//2,450))

    txt_rejoue = intro_font2.render(
        f' REJOUER ', True,
        'black')
    txt_rejoue_rect = txt_rejoue.get_rect(center=(800, 500))

    indice = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if surface_rejoue_rect.collidepoint(pygame.mouse.get_pos()):
                    return True
        screen.blit(surface_fond, surface_fond_rect)
        screen.blit(surface_billard, surface_billard_rect)

        pygame.draw.lines(screen, 'black', True, [(screen_x//2-billard.xmax//2, screen_y//2-billard.ymax//2), (screen_x//2+billard.xmax//2, screen_y//2-billard.ymax//2), (screen_x//2+billard.xmax//2, screen_y//2+billard.ymax//2), (screen_x//2-billard.xmax//2, screen_y//2+billard.ymax//2)], 5)

        pygame.draw.line(screen, 'black', (50,400),(50,300),  5)
        pygame.draw.line(screen, '#EEEC90', (50,360),(50,300),  5)
        screen.blit(blanche, (40,280))

        surfaces_boules_fin = [0] * len(billard)
        for i in range(1,len(billard)):
            surfaces_boules_fin[i] = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(surfaces_boules_fin[i], english_color(billard[i].coul), (10, 10), 7)

        for i in range(1,len(surfaces_boules_fin)):
            screen.blit(surfaces_boules_fin[i], (int(billard[i].x) -10 +screen_x//2-billard.xmax//2, int(billard[i].y) -10 +screen_y//2-billard.ymax//2))

        for i in range(indice) :
            screen.blit(liste_carre[i][0], liste_carre[i][1])
        if indice <16 :
            indice += 1
        else :
            screen.blit(txt_fin, txt_fin_rect)
            screen.blit(txt_fin2, txt_fin2_rect)
            screen.blit(surface_rejoue,surface_rejoue_rect)
            screen.blit(txt_rejoue,txt_rejoue_rect)


        pygame.display.update()
        clock.tick(5)





class Billard (list):
    def __init__(self,xmax,ymax,nb_billes,dt):
        self.xmax = xmax
        self.ymax = ymax
        self.dt = dt
        nb_billes += nb_billes % 2
        self.append(Bille(500, 300, 'Blanche'))
        self.append(Bille(250,300,'Rouge'))
        self.append(Bille(580,350,'Bleue'))




class Bille () : # cette classe définit le comportement des billes à l'intérieur du Billard, ce sont des objets à part entière

    def __init__(self,abscisse,ordonnee, couleur = 'Blanche' , vitesse=0,direction=(0,0),taille=5): # une bille a  : une position, une vitesse, une direction pour la vitesse et une taille
        self._taille = taille
        self.__coords = (abscisse,ordonnee)
        self.__v = vitesse
        self.direction = direction
        self.coul = couleur
    @property
    def x(self):
        return self.__coords[0]
    @property
    def y(self):
        return self.__coords[1]






if __name__ == "__main__":
    liste_test = [[0.1, [350+i, 255+i, (1000, 600)], [250+i, 355, (1000, 600)], [400, 200-i, (1000, 600)]]for i in range(200)]
    n,x,y, joueur = 3,300,400,1
    billard= Billard(x,y,n,0.1)
    animation_fin(billard,'Bleue')



