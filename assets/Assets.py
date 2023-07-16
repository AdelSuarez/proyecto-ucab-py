import pygame

robot = pygame.transform.scale(pygame.image.load("assets/robot.png"), (50, 50))
bomb = pygame.transform.scale(pygame.image.load("assets/bomba.png"), (35, 35))
goal = pygame.transform.scale(pygame.image.load("assets/engranaje.png"), (35, 35))
over = pygame.transform.scale(pygame.image.load("assets/explosion.png"), (45, 45))
victory = pygame.transform.scale(pygame.image.load("assets/victory.png"), (50, 50))

btn_start = pygame.image.load("assets/start_btn.png")
btn_exit = pygame.image.load("assets/exit_btn.png")
btn_reset = pygame.image.load("assets/reset.png")
btn_pause = pygame.image.load("assets/pause.png")
btn_continue = pygame.image.load("assets/continue2.png")
btn_return = pygame.image.load("assets/return.png")



victory_img =  pygame.transform.scale(pygame.image.load("assets/victory.png"), (700,500))
sensor_img =  pygame.transform.scale(pygame.image.load("assets/sensor.png"), (350,350))
keys_img =  pygame.transform.scale(pygame.image.load("assets/key2.png"), (350,350))


BG_opacity = pygame.image.load("assets/BG_opacity2.png")
icon = pygame.image.load("assets/robot.png")