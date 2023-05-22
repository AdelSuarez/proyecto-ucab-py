# from src.create_map import Create_map
from src.create_map import Create_map
import style.style as st
import pygame
import random

class Main_screen:
    def __init__(self):
        self._map_game = Create_map(17,23).maker()
        self._robot= pygame.transform.scale(pygame.image.load("screen/assets/robot.png"), (40, 40))
        self._bomb= pygame.transform.scale(pygame.image.load("screen/assets/bomba.png"), (35, 35))
        self._goal= pygame.transform.scale(pygame.image.load("screen/assets/meta.png"), (35, 35))
        self.settings()
        self.wiget_main()

    def settings(self):
        self._game_over = False
        self._size = (1042, 772)
        pygame.init()
        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('ROBOTcok')
        self._clock = pygame.time.Clock()

    def wiget_main(self):

        while not self._game_over:
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
            self._screen.fill(st.BLACK)
            self.create_map()

            self._clock.tick(60)
            pygame.display.update()


    def create_map(self):
        for row in range(len(self._map_game)):
            for index_column, column in enumerate(self._map_game[row]):
                pygame.draw.rect(self._screen,
                                st.WHITE,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                
                if column == '>':   
                    pygame.draw.rect(self._screen,
                                st.GREEN_SCREEN,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                    self._screen.blit(self._robot, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-2,
                                st.HIGH,
                                st.LONG])
                    
                elif column == '*':
                    
                    self._screen.blit(self._bomb, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN+2,
                                (st.MARGIN+st.LONG) * row + st.MARGIN+5,
                                st.HIGH,
                                st.LONG])
                    
                elif column == 'H':
                    self._screen.blit(self._goal, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN+2,
                                (st.MARGIN+st.LONG) * row + st.MARGIN+2,
                                st.HIGH,
                                st.LONG])
                

 
# NEGRO = (0, 0, 0)
# BLANCO = (255, 255, 255)
# VERDE = ( 0, 255, 0)
# ROJO = (255, 0, 0)
 
# HIGH  = 40
# LONG = 40
 
# MARGIN = 5
 
 
# mapa = Create_map(17,23).maker()
# pygame.init()
  
# DIMENSION_VENTANA = [1042, 772]
# pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
 
# pygame.display.set_caption("Retículas y Matrices")
# robot= pygame.transform.scale(pygame.image.load("src/screen/assets/robot.png"), (40, 40))
# mina= pygame.transform.scale(pygame.image.load("src/screen/assets/bomba.png"), (35, 35))
# meta= pygame.transform.scale(pygame.image.load("src/screen/assets/meta.png"), (35, 35))



 
# hecho = False
 
# # Lo usamos para establecer cuán rápido de refresca la pantalla.
# reloj = pygame.time.Clock()
 
# # -------- Bucle Principal del Programa-----------
# while not hecho:
#     for evento in pygame.event.get(): 
#         if evento.type == pygame.QUIT: 
#             hecho = True
#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             # El usuario presiona el ratón. Obtiene su posición.
#             pos = pygame.mouse.get_pos()
#             # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
#             columna = pos[0] // (HIGH + MARGIN)
#             fila = pos[1] // (LONG + MARGIN)
#             # Establece esa ubicación a cero
#             print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
 
#     # Establecemos el fondo de pantalla.
#     pantalla.fill(NEGRO)
    
#     # Dibujamos la retícula
#     for fila in range(len(mapa)):
#         for columna in range(len(mapa[fila])):
#             color = BLANCO
#             pygame.draw.rect(pantalla,
#                              color,
#                              [(MARGIN+HIGH) * columna + MARGIN,
#                               (MARGIN+LONG) * fila + MARGIN+2,
#                               HIGH,
#                               LONG])
#             if mapa[fila][columna] == '>':

#                 pantalla.blit(robot, [(MARGIN+HIGH) * columna + MARGIN,
#                               (MARGIN+LONG) * fila + MARGIN,
#                               HIGH,
#                               LONG])
#             elif mapa[fila][columna] == '*':

#                 pantalla.blit(mina, [(MARGIN+HIGH) * columna + MARGIN+2,
#                               (MARGIN+LONG) * fila + MARGIN+5,
#                               HIGH,
#                               LONG])
#             elif mapa[fila][columna] == 'H':

#                 pantalla.blit(meta, [(MARGIN+HIGH) * columna + MARGIN+2,
#                               (MARGIN+LONG) * fila + MARGIN+5,
#                               HIGH,
#                               LONG])
     
#     # Limitamos a 60 fotogramas por segundo.
#     reloj.tick(60)
 
#     # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
#     pygame.display.flip()
     
# # Pórtate bien con el IDLE.
# pygame.quit()