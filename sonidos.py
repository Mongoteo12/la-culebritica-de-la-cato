import pygame

from configuracion import *

class Musica:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.2)

    def reproducir(self):
        pygame.mixer.music.load("Musiquitas,imagens/musica.mp3")
        pygame.mixer.music.play()

    def parar(self):
        pygame.mixer.music.stop()

    def pausar(self):
        pygame.mixer.music.pause()

    def reanudar(self):
        pygame.mixer.music.unpause()

    def posicion(self):
        return pygame.mixer.music.get_pos()

class Sonido:
    def __init__(self):
        pygame.mixer.init()

    def reproducir(self, sonido):
        pygame.mixer.Sound(sonido).play()