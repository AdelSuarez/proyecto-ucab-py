import pygame
import sys

pygame.init()
vetana = pygame.display.set_mode((800, 600))


pygame.display.set_caption('ROBOTOTO')
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()