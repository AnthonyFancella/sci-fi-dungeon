import pygame

minion_2_image = pygame.image.load("assets/MINION_2.png")

minion_2_idle = [minion_2_image.subsurface((0, 0, 32, 32)),
                 minion_2_image.subsurface((32, 0, 32, 32)),
                 minion_2_image.subsurface((64, 0, 32, 32)),
                 minion_2_image.subsurface((96, 0, 32, 32))]

minion_2_walk = [minion_2_image.subsurface((0, 32, 32, 32)),
                 minion_2_image.subsurface((32, 32, 32, 32)),
                 minion_2_image.subsurface((64, 32, 32, 32)),
                 minion_2_image.subsurface((96, 32, 32, 32))]

minion_2_bite = [minion_2_image.subsurface((0, 64, 32, 32)),
                 minion_2_image.subsurface((32, 64, 32, 32)),
                 minion_2_image.subsurface((64, 64, 32, 32)),
                 minion_2_image.subsurface((96, 64, 32, 32)),
                 minion_2_image.subsurface((128, 64, 32, 32))]