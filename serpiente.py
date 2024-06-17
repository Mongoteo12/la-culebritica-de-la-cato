import pygame

from configuracion import *

class Serpiente:
    def __init__(self, VENTANA, longitud):
        self.VENTANA = VENTANA
        self.longitud = longitud

        self.cabeza = pygame.image.load("Musiquitas,imagens/yoshii.png").convert()
        self.cuerpo = pygame.image.load("Musiquitas,imagens/cuerpoyoshi.png").convert()

        self.x = [TAMANO_BLOQUE] * self.longitud
        self.y = [TAMANO_BLOQUE] * self.longitud

        self.direccion = "abajo"

    def dibujar(self):
        self.VENTANA.fill(COLOR_FONDO)

        for i in range(self.longitud):
            if i == 0:
                self.VENTANA.blit(self.cabeza, (self.x[i], self.y[i]))
            else:
                self.VENTANA.blit(self.cuerpo, (self.x[i], self.y[i]))

    def crecer(self):
        self.longitud += 1
        self.x.append(-1)
        self.y.append(-1)

    def mover(self):
        for i in range(self.longitud - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direccion == "arriba":
            self.y[0] -= TAMANO_BLOQUE
        if self.direccion == "abajo":
            self.y[0] += TAMANO_BLOQUE
        if self.direccion == "izquierda":
            self.x[0] -= TAMANO_BLOQUE
        if self.direccion == "derecha":
            self.x[0] += TAMANO_BLOQUE 

        self.dibujar()

    def cambiar_direccion(self, direccion):
        self.direccion = direccion
        self.dibujar()