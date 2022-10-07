import pygame
import sys


ANCHO=640
ALTO=480
color_azul=(0,0,64) #color azul para el fondo

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
        #Establecer velocidad inicial
        self.speed=[3,3]
     
    def update(self):
        #Evitar que salga por debajo
        if self.rect.bottom>=ALTO or self.rect.top<=0:
            self.speed[1]=-self.speed[1]
        #Evitar que salga por la derecha
        elif self.rect.right>=ANCHO or self.rect.left<=0:
            self.speed[0]=-self.speed[0]
        # mover en base a posición actual y velocidad
        self.rect.move_ip(self.speed)


class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('img/paleta.png')
        #Obtener rectángulo de la imagen
        self.rect=  self.image.get_rect()
        # Posicion inicial centrada en pantalla en X
        self.rect.midbottom=(ANCHO/2, ALTO-20)
        #Establecer velocidad inicial
        self.speed=[0,0]

    def update(self, evento):
        #Buscar si se presiono la tecla izquierda
        if evento.key==pygame.K_LEFT and self.rect.left>0:
            self.speed=[-5,0]
        #Buscar si se presiono la tecla derecha
        elif evento.key==pygame.K_RIGHT and self.rect.right<ANCHO:
            self.speed=[5,0]
        else:
            self.speed=[0,0]
        #Mover en base a posición actual y velocidad
        self.rect.move_ip(self.speed)


class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load('img/ladrillo.png')
        #Obtener rectángulo de la imagen
        self.rect=  self.image.get_rect()
        #Provisión inicial, provista externamente
        self.rect.topleft=posicion

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        pygame.sprite.Group.__init__(self)

        pos_x=0
        pos_y=20

        ladrillo1=Ladrillo((0,0))
        ladrillo2=Ladrillo((100,100))

        for i in range(cantidadLadrillos):
            ladrillo=Ladrillo((pos_x,pos_y))
            self.add(ladrillo)

            pos_x+=ladrillo.rect.width
            if pos_x>=ANCHO:
                pos_x=0
                pos_y+=ladrillo.rect.height





# Incilializando pantalla
pantalla=pygame.display.set_mode((ANCHO,ALTO))
#Confidurar título de la pantalla
pygame.display.set_caption('Juego Breakout')
#Crear reloj
reloj=pygame.time.Clock()
#Ajustar repetición de evento tecla presionada
pygame.key.set_repeat(30)

bolita= Bolita()
jugador=Paleta()
muro=Muro(50)


while True:
    #Establecer FPS
    reloj.tick(60)

    # Revisar todos los eventos
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            sys.exit()
        #Buscar eventos del teclado
        elif evento.type==pygame.KEYDOWN:
            jugador.update(evento)

    #Actualizar posición de bolita
    bolita.update()

    #Rellenar la pantalla
    pantalla.fill(color_azul)
    
    # Dibujar bolita en pantalla
    pantalla.blit(bolita.image, bolita.rect)   
    # Dibujar jugador en pantalla
    pantalla.blit(jugador.image, jugador.rect)
    #Dibujar los ladrillos
    muro.draw(pantalla )
    # Actualizar elementos de la pantalla
    pygame.display.flip()