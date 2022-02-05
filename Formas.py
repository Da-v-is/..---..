import pygame,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400,400))

class Formas:
    def __init__(self):
        self.color = (52,142,65)
        self.largo = 200
        self.ancho = 200
        self.posx = (400 - self.largo)/2
        self.posy = (400 - self.ancho)/2
        self.tamaño = False
        if self.largo < 391 and self.ancho < 391:
            self.tamaño = True
       
    def circulo(self,diametro):
        if diametro <= 200:
            self.Diam = diametro
            pygame.draw.circle(screen,self.color,(200,200),self.Diam)
        else:
            print("muy grande el Diametro")
    
    def cuadrado(self):
        if self.tamaño:
            pygame.draw.rect(screen,self.color,(self.posx,self.posy,self.largo,self.ancho))
        else:
            print("muy grande el cuadrado")

    def triangulo(self):
        if self.tamaño:
            self.punto3 = self.largo + self.posx
            self.pos_y = self.posy + self.ancho
            pygame.draw.polygon(screen,self.color,((self.posx,self.pos_y),(200,self.posy),(self.punto3,self.pos_y)))
        else:
            print("muy grande el triangulo")
            
dibujo = Formas()

while True:
    screen.fill((222,14,5))
    #dibujo.circulo(100)
    #dibujo.cuadrado()
    #dibujo.triangulo()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


    
