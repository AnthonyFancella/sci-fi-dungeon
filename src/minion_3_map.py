import pygame

minion_3_image = pygame.image.load("assets/MINION_3.png")

minion_3_idle = [minion_3_image.subsurface((0, 0, 32, 32)),
                 minion_3_image.subsurface((32, 0, 32, 32)),
                 minion_3_image.subsurface((64, 0, 32, 32)),
                 minion_3_image.subsurface((96, 0, 32, 32))]

minion_3_walk = [minion_3_image.subsurface((0, 32, 32, 32)),
                 minion_3_image.subsurface((32, 32, 32, 32)),
                 minion_3_image.subsurface((64, 32, 32, 32)),
                 minion_3_image.subsurface((96, 32, 32, 32))]

minion_3_bite = [minion_3_image.subsurface((0, 64, 32, 32)),
                 minion_3_image.subsurface((32, 64, 32, 32)),
                 minion_3_image.subsurface((64, 64, 32, 32)),
                 minion_3_image.subsurface((96, 64, 32, 32))]