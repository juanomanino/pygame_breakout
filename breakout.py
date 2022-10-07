import pygame
import sys


ANCHO=400
ALTO=400

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('img/bolita.png')
        #Obtener rectángulo de la imagen
        self.rect=  self.image.get_rect()
        # Posicion inicial centrada en pantalla
        self.rect.centerx= ANCHO/2
        self.rect.centery= ALTO/2


# Incilializando pantalla
pantalla=pygame.display.set_mode((ANCHO,ALTO))
#Confidurar título de la pantalla
pygame.display.set_caption('Juego Breakout')



bolita= Bolita()

while True:
    # Revisar todos los eventos
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            sys.exit()
    
    # Dibujar bolita en pantalla
    pantalla.blit(bolita.image, bolita.rect)
    # Actualizar elementos de la pantalla
    pygame.display.flip()