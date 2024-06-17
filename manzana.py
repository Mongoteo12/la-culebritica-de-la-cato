import pygame
import random

from configuracion import *

class Manzana:
    def __init__(self, VENTANA):
        self.imagen = pygame.image.load("Musiquitas,imagens/manzana.png").convert()
        self.VENTANA = VENTANA
        self.x = random.randint(0, (ANCHO // TAMANO_BLOQUE) - 1) * TAMANO_BLOQUE
        self.y = random.randint(0, (ALTO // TAMANO_BLOQUE) - 1) * TAMANO_BLOQUE

    def dibujar(self):
        self.VENTANA.blit(self.imagen, (self.x, self.y))

    def mover(self):
        self.x = random.randint(0, (ANCHO // TAMANO_BLOQUE) - 1) * TAMANO_BLOQUE
        self.y = random.randint(0, (ALTO // TAMANO_BLOQUE) - 1) * TAMANO_BLOQUE
