import pygame

minion_1_image = pygame.image.load("assets/MINION_1.png")

minion_1_idle = [minion_1_image.subsurface((0, 0, 32, 32)),
                 minion_1_image.subsurface((32, 0, 32, 32)),
                 minion_1_image.subsurface((64, 0, 32, 32)),
                 minion_1_image.subsurface((96, 0, 32, 32))]

minion_1_walk = [minion_1_image.subsurface((0, 32, 32, 32)),
                 minion_1_image.subsurface((32, 32, 32, 32)),
                 minion_1_image.subsurface((64, 32, 32, 32)),
                 minion_1_image.subsurface((96, 32, 32, 32))]

minion_1_bite = [minion_1_image.subsurface((0, 64, 32, 32)),
                 minion_1_image.subsurface((32, 64, 32, 32)),
                 minion_1_image.subsurface((64, 64, 32, 32)),
                 minion_1_image.subsurface((96, 64, 32, 32))]