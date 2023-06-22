import pygame

class Button:
    def __init__(self, x, y , image, scale):
        width = image.get_width()
        height = image.get_height()
        self._imagen = pygame.transform.scale(image, (int(width *scale), int(height * scale)))
        self._rect = self._imagen.get_rect()
        self._rect.topleft = (x, y)
        self._clicked = False

    def draw(self, screen):
        action = False
        # pisicion del mause 
        position = pygame.mouse.get_pos()

        if self._rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self._clicked == False:
                self._clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self._clicked = False


        screen.blit(self._imagen, (self._rect.x, self._rect.y))
        return action