import pygame

# ----------- SCREEN -----------------
LONG  = 40
HIGH = 40
MARGIN = 5

SCREEN_WIDTH = 1042
SCREEN_HEIGHT = 810


# Colors
GREY =( 229, 231, 233 )
WHITE = (225,225,225)
BLACK = (0,0,0)
LIGHT_BLUE = (220, 241, 255)
# 93, 173, 226
# GREEN_SCREEN = (118, 215, 196)
# GREEN_ROBOT = (183,255,102) 

GREEN_ROBOT = (72, 201, 176)
YELLOW_GOAL = (247, 220, 111)
RED_ROBOT = ( 236, 112, 99 )

BACKGROUND_COLOR = (52,78,91)

RED = (192, 57, 43 )

def font(size):
    # retorna el estilo del texto
    return pygame.font.Font("assets/font.ttf", size)
