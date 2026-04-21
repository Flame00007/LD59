import pygame

import time

import random

pygame.init()

ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

tailleX , tailleY = ecran.get_size()


ring = pygame.image.load('ring.png')
ring = pygame.transform.scale(ring, (tailleX, tailleY))

class goutte():
    def __init__(self, moveX, moveY, x, y, degree):
        self.image = pygame.image.load('goutte.png')
        self.image = pygame.transform.scale(self.image, (75, 50))
        self.x = x
        self.y = y
        self.moveX = moveX
        self.moveY = moveY
        self.degree = degree
        self.image = pygame.transform.rotate(self.image, self.degree)
    def move(self):
        self.x += self.moveX
        self.y += self.moveY

    def fin(self):
        if self.x > tailleX:
            return True
        if self.x < -100:
            return True
        if self.y > tailleY:
            return True
        if self.y < -100:
            return True
        return False
    def show(self):
        ecran.blit(self.image, (self.x, self.y))


class dentifrice():
    def __init__(self):
        self.image = pygame.image.load('Signal3b.png')
        self.image = pygame.transform.scale(self.image, (300, 400))
        self.liste = []
        self.degree = 0
        self.en_cours = False
        self.tailleX, self.tailleY = ecran.get_size()
        self.directXreturn = 0
        self.directYreturn = -1
        self.directX = 1
        self.directY = 0
    def createtir(self, moveX, moveY):
        if self.degree == 0:
            self.liste.append(goutte(moveX, moveY, self.x + 120, self.y , self.degree + 90))
        if self.degree == 90:
            self.liste.append(goutte(moveX, moveY, self.x, self.y + 130, self.degree + 90))
        if self.degree == 180 :
            self.liste.append(goutte(moveX, moveY, self.x + 130, self.y + 300, self.degree + 90))
        if self.degree == 270:
            self.liste.append(goutte(moveX, moveY, self.x + 300, self.y + 120, self.degree + 90))
    def tir(self, dent):
        suppr = []
        for i in range(len(tube.liste)):
            if tube.liste[i].fin():
                suppr.append(i)
            if dent.touch(tube.liste[i].x, tube.liste[i].y, 75, 50):
                suppr.append(i)
            tube.liste[i].move()
            tube.liste[i].show()
        for elem in suppr:
            tube.liste.pop(elem)
        if suppr != []:
            return True
        return False
    def offense(self, perso, tailleX):
        x = perso.x + 50 - 200
        x2 = perso.x + 50 + 200
        y = perso.y + 50 - 200
        y2 = perso.y + 50 + 200
        if 0.185*tailleX > perso.x + 50 - 200 :
            x = 0.185*tailleX
        if tailleX - 0.185*tailleX < perso.x + 50 + 200 :
            x2 = tailleX - 0.185*tailleX
        if 0.180*tailleY > perso.y + 50 - 200 :
            y = 0.180*tailleY
        if tailleY - 0.180*tailleY < perso.y + 50 + 200 :
            y2 = tailleY - 0.180*tailleY
        self.cibleX = random.randint(int(x), int(x2))
        self.cibleY = random.randint(int(y), int(y2))
        self.en_cours = True
    def tp(self, x, y):
        self.x = x
        self.y = y
    def rotate(self, degree):
        self.degree = degree
        self.image = pygame.transform.rotate(self.image, self.degree)
    def changerotate(self):
        self.image = pygame.image.load('Signal3b.png')
        self.image = pygame.transform.scale(self.image, (300, 400))
        self.degree = 0
        a = random.randint(0,3)
        if a == 0:
            self.rotate(0)
            self.tp((self.tailleX - 300) / 2, self.tailleY )
            self.directXreturn, self.directYreturn = 0, 1
            self.directX, self.directY = 1, 0
        if a == 1:
            self.rotate(270)
            self.tp(- 400, (self.tailleY - 300) / 2)
            self.directXreturn, self.directYreturn = -1, 0
            self.directX, self.directY = 0, 1
        if a == 2:
            self.rotate(180)
            self.tp((tailleX - 300)/2, - 400)
            self.directXreturn, self.directYreturn = 0, -1
            self.directX, self.directY = 1, 0
        if a == 3:
            self.rotate(90)
            self.tp(self.tailleX , (self.tailleY - 300 ) / 2)
            self.directXreturn, self.directYreturn = 1, 0
            self.directX, self.directY = 0, 1
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
    def show(self):
        ecran.blit(self.image, (self.x, self.y))


class dent():
    def __init__(self, x, y):
        self.listImage = ['dent1.png', 'dent2.png', 'dent3.png', 'dent4.png']
        self.image = pygame.image.load(self.listImage[3])
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.x = x
        self.y = y
        self.etat = 3
    def tp(self, x, y):
        self.x = x
        self.y = y
    def touch(self, x, y, tailleX1, tailleY1):
        zone_rect1 = pygame.Rect((x, y), (tailleX1, tailleY1))
        zone_rect2 = pygame.Rect((self.x, self.y), (100, 100))
        if zone_rect1.colliderect(zone_rect2):
            return True
        return False
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        tailleX, tailleY = ecran.get_size()
        if self.y > tailleY - 0.24*tailleY:
            self.y = tailleY - 0.24*tailleY
        if self.y < 0.05*tailleY + 100:
            self.y = 0.05*tailleY + 100
        if self.x > tailleX - 0.185*tailleX:
            self.x = tailleX - 0.185*tailleX
        if self.x < 0.185*tailleX - 100:
            self.x = 0.185*tailleX - 100
    def choice(self, etat):
        self.etat = etat
        self.image = pygame.image.load(self.listImage[self.etat])
        self.image = pygame.transform.scale(self.image, (100, 100))
    def show(self):
        ecran.blit(self.image, (self.x, self.y))


def delai(time1, time2, ecart):
    if time2 - time1 > ecart:
        return True
    else:
        return False


def lv(score1, score2):
    if score2 - score1 < 20:
        ecart = 2
        vitesse = 0.8
        vitesseBalle = 1
    if score2 - score1 > 20:
        ecart = 1.5
        vitesse = 1
        vitesseBalle = 1.5
    if score2 - score1 > 40:
        ecart = 1
        vitesse = 1.5
        vitesseBalle = 2
    if score2 - score1 > 60:
        ecart = 0.75
        vitesse = 2
        vitesseBalle = 2.5
    if score2 - score1 > 80:
        ecart = 0.5
        vitesse = 2.5
        vitesseBalle = 3
    return ecart, vitesse, vitesseBalle


tube = dentifrice()
tube.tp((tailleX - 300)/2,-200)
tube.rotate(180)

perso = dent((tailleX-100)/2, (tailleY-100)/2)

time1 = time.perf_counter()

pygame.mouse.set_visible(False)

score1 = time.perf_counter()

myfont = pygame.font.SysFont("monospace", 50)

tempschange1 = time.perf_counter()

changeAller = False

changeRetour = False

compteur = 0

var = True



while var == True:
    tempschange2 = time.perf_counter()
    if delai(tempschange1, tempschange2, 5):
        tempschange1 = time.perf_counter()
        changeAller = True
        compteur = 0
    if changeAller == True:
        if compteur == 200:
            tube.changerotate()
            changeAller = False
            changeRetour = True
            compteur = 0
        tube.move(tube.directXreturn, tube.directYreturn)
        compteur += 1
    if changeRetour == True:
        if compteur == 200:
            changeRetour = False
        tube.move(-tube.directXreturn, -tube.directYreturn)
        compteur += 1
    if changeAller == False and changeRetour == False:
        score2 = time.perf_counter()
    ecart, vitesse, vitesseBalle = lv(score1, score2)
    ecran.blit(ring, (0, 0))
    phrase = f'{int(score2 - score1)}'
    score_display = myfont.render(phrase, 1, (255, 255, 0))
    ecran.blit(score_display, (0, 0))
    perso.show()
    for i in range (len(tube.liste)):
        a = perso.touch(tube.liste[i].x, tube.liste[i].y, 75, 50)
        if a == True :
            perso.etat -= 1
            if perso.etat < 0:
                var = False
            perso.choice(perso.etat)
    tube.tir(perso)
    tube.show()
    time2 = time.perf_counter()
    if delai(time1, time2, ecart):
        tube.offense(perso, tailleX)
        time1 = time.perf_counter()
        tube.en_cours = True
    if tube.en_cours == True:
        if tube.cibleX-10 < tube.x + 150 < tube.cibleX+10:
            tube.createtir(-tube.directXreturn * vitesseBalle, -tube.directYreturn * vitesseBalle)
            tube.en_cours = False
        if tube.degree == 0 or tube.degree == 180:
            if tube.cibleX < tube.x + 150:
                tube.move(-vitesse, 0)
            if tube.cibleX > tube.x + 150 :
                tube.move(vitesse, 0)
        if tube.degree == 90 or tube.degree == 270:
            if tube.cibleY < tube.y + 150:
                tube.move(0, -vitesse)
            if tube.cibleY > tube.y + 150:
                tube.move(0, vitesse)
        if tube.cibleY-10 < tube.y + 150 < tube.cibleY+10:
            tube.createtir(-tube.directXreturn * vitesseBalle, -tube.directYreturn * vitesseBalle)
            tube.en_cours = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                var = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        perso.move(0, -1.5)
    if pressed[pygame.K_DOWN]:
        perso.move(0, 1.5)
    if pressed[pygame.K_LEFT]:
        perso.move(-1.5, 0)
    if pressed[pygame.K_RIGHT]:
        perso.move(1.5, 0)
    pygame.display.flip()
    ecran.fill((0, 0, 0))


scoreFinal = score2 - score1

myfont = pygame.font.SysFont("monospace", 200)

debut = time.perf_counter()

var = True


while var == True:
    temps = time.perf_counter()
    if delai(debut, temps, 5):
        var = False
    phrase = f'{int(score2 - score1)}'
    score_display = myfont.render(phrase, 1, (255, 0, 0))
    ecran.blit(score_display, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                var = False
    ecran.fill((0, 0, 0))
    ecran.blit(ring, (0, 0))
    ecran.blit(score_display, ((tailleX - 100)/2, (tailleY - 300)/2))
    pygame.display.flip()



