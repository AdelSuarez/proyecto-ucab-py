import pygame

robot = pygame.transform.scale(pygame.image.load("assets/robot1.png"), (50, 50))
bomb = pygame.transform.scale(pygame.image.load("assets/bomba.png"), (35, 35))
goal = pygame.transform.scale(pygame.image.load("assets/unavainaloca.png"), (35, 35))
over = pygame.transform.scale(pygame.image.load("assets/explosion.png"), (45, 45))
victory = pygame.transform.scale(pygame.image.load("assets/victory.png"), (50, 50))
btn_start = pygame.image.load("assets/start_btn.png")
btn_exit = pygame.image.load("assets/exit_btn.png")
victory_img =  pygame.transform.scale(pygame.image.load("assets/victory.png"), (700,500))
BG_opacity = pygame.image.load("assets/b_opacity.png")