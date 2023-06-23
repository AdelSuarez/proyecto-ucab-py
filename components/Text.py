import pygame

class Text:
    def __init__(self, text, font, text_col) -> None:
        self._text = text
        self._font = font
        self._text_col = text_col

    def draw_text(self, screen, x, y):
        img = self._font.render(self._text, True, self._text_col)
        screen.blit(img, (x,y))
