import pygame
import sys

pygame.init()
HEIGHT = 720
WIDTH = 1280
FONDO = pygame.image.load('src/screen/assets/Background.png')
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ROBOT')


def fuente(size):
    return pygame.font.Font("assets/font.ttf", size)

def main():
    while True:
        ventana.blit(FONDO,(0,0))
        # MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = fuente(100).render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


        ventana.blit(MENU_TEXT, MENU_RECT)

        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

  