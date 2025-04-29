import pygame

deco_image = pygame.image.load("assets/dungeon Crawlermkup.png")

bullet = [deco_image.subsurface((80, 304, 16, 16)),
          deco_image.subsurface((96, 304, 16, 16)),
          deco_image.subsurface((112, 304, 16, 16)),
          deco_image.subsurface((128, 304, 16, 16))]
          
shell = [deco_image.subsurface((80, 288, 16, 16)),
         deco_image.subsurface((96, 288, 16, 16)),
         deco_image.subsurface((112, 288, 16, 16)),
         deco_image.subsurface((128, 288, 16, 16))]

health = [deco_image.subsurface((16, 256, 16, 16)),
          deco_image.subsurface((32, 256, 16, 16)),
          deco_image.subsurface((48, 256, 16, 16))]