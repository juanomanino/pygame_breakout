import pygame
import sys
import time

ANCHO=640
ALTO=480
color_azul=(0,0,64) #color azul para el fondo
color_blanco=(255,255,255)#color blanco, para textos

class Escena:
    def __init__(self):
        "Incialización"
        self.proximaEscena=False
        self_jugando=True

    def leer_eventos(self,eventos):
        "Lee la lista de todos los eventos"
        pass
    def actualizar(self):
        "Cálculps y Lógica."
        pass
    def dibujar(self,pantalla):
        "Dibuja los objetos en pantalla"
        pass
    def cambiar_escena(self,escena):
        "Selecciona la nueva esscena a ser desplegada"
        self.proximaEscena=escena


class Director:
    def __init__(self, titulo="", res=(ANCHO,ALTO)):
        pygame.init()
        # Incilializando pantalla
        self.pantalla=pygame.display.set_mode(res)
        #Confidurar título de la pantalla
        self.pygame.display.set_caption(titulo)
        #Crear reloj
        reloj=pygame.time.Clock()
        self_escena=None
        self_escenas={}
    def ejecutar(self, escena_inicial, fps=60):
        self_escena=self_escenas[escena_inicial]
        jugando =True
        while jugando:
            self.reloj.tick(fps)
            eventos=pygame.event.get()
            # Revisar todos los eventos
            for evento in eventos:
                if evento.type==pygame.QUIT:
                    jugando=False

            self.escena.leer_eventos(eventos)
            self.escena.actualizar()
            self.escena.dibujar(self,pantalla)

            self_elegirEscena(self,escena.proximaEscena)

            if jugando:
                jugando=self.escena.jugando

            pygame.display.flip()
        time.sleep(3)

        def ElegirEscena(self, proximaEscena):
            if proximaEscena:
                if proximaEscena not in self.escenas:
                    self.agregarEscena(proximaEscena)
                self.escena=self.escenas[proximaEscena]
        def AgregarEscena(self,escena):
            escenaClase='Escena'+escena
            escenaObj=globlas()[escenaClase]
            self.escenas[escena]=escenaObj()


 


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
        if self.rect.top<=0:
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


#Funcion llamada tras dejar ir la bolita
def juego_terminado():
    fuente=pygame.font.SysFont('Arial', 72)
    texto=fuente.render('Juego terminado :(', True, color_blanco )
    texto_rect=texto.get_rect()
    texto_rect.center=[ANCHO/2,ALTO/2]
    pantalla.blit(texto, texto_rect)
    pygame.display.flip()
    #Pausar por 3 segundos
    time.sleep(3)
    #Salir
    sys.exit()


def mostrar_puntuacion():
    fuente=pygame.font.SysFont('Consolas', 20)
    texto=fuente.render(str(puntuacion).zfill(5), True, color_blanco )
    texto_rect=texto.get_rect()
    texto_rect.topleft=[0,0]
    pantalla.blit(texto, texto_rect)


def mostrar_vidas():
    fuente=pygame.font.SysFont('Consolas', 20)
    cadena="Vidas: "+ str(vidas.zfill(2))
    texto=fuente.render(cadena, True, color_blanco )
    texto_rect=texto.get_rect()
    texto_rect.topright=[0,0]
    pantalla.blit(texto, texto_rect)



#Ajustar repetición de evento tecla presionada
pygame.key.set_repeat(30)

bolita= Bolita()
jugador=Paleta()
muro=Muro(50)
puntuacion=0
vidas=3
esperando_saque= True

while True:
    #Establecer FPS
    reloj.tick(60)


        #Buscar eventos del teclado
        elif evento.type==pygame.KEYDOWN:
            jugador.update(evento)
            if esperando_saque == True and evento.key ==pygame.K_ESPACE:
                esperando_saque=False
                if bolita.rect.centerx < ANCHO/2:
                    bolita.speed=[3,-3]
                else:
                    bolita.speed=[-3,-3]



    #Actualizar posición de bolita
    if esperando_saque ==False:
        bolita.update()
    else:
        bolita.rect.midbottom=jugador.rect.midtop

    #Colisión entre bolita y jugador
    if pygame.sprite.collide_rect(bolita, jugador):
        bolita.speed[1]=-bolita.speed[1]

    #Colision de la bolita con el muro
    lista=pygame.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo=lista[0]
        cx=bolita.react.centerx
        if cx < ladrillo.rect.left or cx> ladrillo.rect.right:
            bolita.spped[0]=-bolita.speed[0]
        else:
            bolita.speed[1]=-bolita.speed[1]
        muro.remove(ladrillo)
        puntuacion += 10



    #Revisar si bolita sale de la pantalla
    if bolita.rect.top>ALTO:
        vidas -=1
        esperando_saque=True   


    #Rellenar la pantalla
    pantalla.fill(color_azul)
    #Mostrar puntuacion
    mostrar_puntuacion()
    #Mostrar vidas
    mostrar_vidas
    # Dibujar bolita en pantalla
    pantalla.blit(bolita.image, bolita.rect)   
    # Dibujar jugador en pantalla
    pantalla.blit(jugador.image, jugador.rect)
    #Dibujar los ladrillos
    muro.draw(pantalla )
    # Actualizar elementos de la pantalla
    pygame.display.flip()

    
    if vidas <= 0:
        juego_terminado()