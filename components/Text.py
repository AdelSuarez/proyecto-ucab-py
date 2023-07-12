import pygame
import style.style as st

class Text:
    def __init__(self, text, font, text_col) -> None:
        self._text = text
        self._font = font
        self._text_col = text_col

    def draw_text(self, screen, x, y):
        img = self._font.render(self._text, True, self._text_col)
        screen.blit(img, (x,y))

    def draw_text_center(self, screen, x):
        img = self._font.render(self._text, True, self._text_col)
        img_rect = img.get_rect(center=(st.SCREEN_WIDTH/2, x))
        screen.blit(img, img_rect)
