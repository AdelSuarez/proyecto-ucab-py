import pygame
import style.style as st

class Button:
    def __init__(self, image, scale):
        width = image.get_width()
        height = image.get_height()
        self._imagen = pygame.transform.scale(image, (int(width *scale), int(height * scale)))
        self._clicked = False

    def btn_center(self, screen, x):
        self._rect = self._imagen.get_rect(center=(st.SCREEN_WIDTH/2, x))
        action = False
        
        # pisicion del mause 
        position = pygame.mouse.get_pos()

        if self._rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self._clicked == False:
                self._clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self._clicked = False


        screen.blit(self._imagen, self._rect)
        return action