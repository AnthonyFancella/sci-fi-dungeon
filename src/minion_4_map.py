import pygame

minion_4_image = pygame.image.load("assets/MINION_4.png")

minion_4_idle = [minion_4_image.subsurface((0, 0, 32, 32)),
                 minion_4_image.subsurface((32, 0, 32, 32)),
                 minion_4_image.subsurface((64, 0, 32, 32)),
                 minion_4_image.subsurface((96, 0, 32, 32))]
                 
minion_4_walk = minion_4_idle

minion_4_bite = [minion_4_image.subsurface((0, 32, 32, 32)),
                 minion_4_image.subsurface((32, 32, 32, 32)),
                 minion_4_image.subsurface((64, 32, 32, 32)),
                 minion_4_image.subsurface((96, 32, 32, 32))]