import pygame

from configuracion import *
from sonidos import *

from serpiente import *
from manzana import *

class Juego:
    def __init__(self):
        self.RUN = True
        self.pausa = True
        self.finalizado = False

        self.FPS = FPS
        self.reloj = pygame.time.Clock()

        self.VENTANA = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("La Culebritica de la cato")
        self.VENTANA.fill((0, 0, 0))

        self.serpiente = Serpiente(self.VENTANA, 1)
        self.serpiente.dibujar()
        self.manzana = Manzana(self.VENTANA)
        self.manzana.dibujar()

        self.sonido = Sonido()
        self.musica = Musica()
        self.musica.reproducir()

    def iniciar(self):
        pygame.init()

        self.VENTANA.fill(COLOR_FONDO)
        self.musica.pausar()
        self.mostrar_mensaje("Apucharalee al ENTER para jugar", 50, ANCHO / 2, ALTO / 2)

        while self.RUN:
            self.reloj.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUN = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.RUN = False
                    
                    if event.key == pygame.K_RETURN:
                        self.pausa = not self.pausa
                        
                        if self.pausa:
                            self.musica.pausar()
                        else:
                            self.musica.reanudar()

                        if self.finalizado:
                            self.reiniciar()

                    if event.key == pygame.K_UP:
                        self.serpiente.cambiar_direccion("arriba")
                    if event.key == pygame.K_DOWN:
                        self.serpiente.cambiar_direccion("abajo")
                    if event.key == pygame.K_RIGHT:
                        self.serpiente.cambiar_direccion("derecha")
                    if event.key == pygame.K_LEFT:
                        self.serpiente.cambiar_direccion("izquierda")

            if not self.pausa:
                if self.musica.posicion == -1:
                    self.musica.reproducir()
                self.actualizar()

        pygame.quit()

    def reiniciar(self):
        self.pausa = False
        self.finalizado = False
        self.FPS = FPS
        self.serpiente = Serpiente(self.VENTANA, 1)
        self.serpiente.dibujar()
        self.musica.reproducir()

    def finalizar(self):
        self.sonido.reproducir("Musiquitas,imagens/uhh.mp3")
        self.VENTANA.fill(COLOR_FONDO)

        self.mostrar_mensaje("PERDISTE PIPIPIPIPI :C", 70, ANCHO / 2, ALTO / 2 - 50)
        self.mostrar_mensaje(f"PUNTOS: {self.serpiente.longitud}", 50, ANCHO / 2, ALTO / 2 + 30)
        self.mostrar_mensaje("Presiona ESC para salir o ENTER para jugar de nuevo.", 30, ANCHO / 2, ALTO / 2 + 100)
        
        pygame.display.flip()
        
        self.musica.parar()
        self.pausa = True
        self.finalizado = True

    def mostrar_puntuacion(self):
        fuente = pygame.font.SysFont("calibri", 30)
        puntos = fuente.render(f"Puntos: {self.serpiente.longitud}", True, (200, 200, 200))
        self.VENTANA.blit(puntos, (10, 10))
        pygame.display.flip()

    def hay_colision(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return True
        else:
            return False

    def mostrar_mensaje(self, mensaje, tamano, x, y):
        fuente = pygame.font.SysFont("calibri", tamano)
        mensaje = fuente.render(mensaje, True, (200, 200, 200))
        self.VENTANA.blit(mensaje, (x - mensaje.get_width() / 2, y - mensaje.get_height() / 2))
        pygame.display.flip()

    def actualizar(self):
        self.serpiente.mover()
        self.serpiente.dibujar()

        # Comprobar colisiones con la manzana
        if self.hay_colision(self.serpiente.x[0], self.serpiente.y[0], self.manzana.x, self.manzana.y):
            self.FPS += 0.1
            self.manzana.mover()
            self.serpiente.crecer()
            self.sonido.reproducir("Musiquitas,imagens/yoshi.mp3")

        self.manzana.dibujar()
        self.mostrar_puntuacion()

        # Comprobar colisiones con la serpiente
        for i in range(1, self.serpiente.longitud):
            if self.hay_colision(self.serpiente.x[0], self.serpiente.y[0], self.serpiente.x[i], self.serpiente.y[i]):
                self.finalizar()

        # Comprobar colisiones con los bordes de la pantalla
        fuera_pantalla = self.serpiente.x[0] < 0 or self.serpiente.x[0] > ANCHO - TAMANO_BLOQUE or self.serpiente.y[0] < 0 or self.serpiente.y[0] > ALTO - TAMANO_BLOQUE
        if fuera_pantalla:
            self.finalizar()

        pygame.display.update()
        pygame.display.flip()

        if self.musica.posicion == -1:
            self.musica.reproducir()