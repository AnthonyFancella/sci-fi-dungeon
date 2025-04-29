import pygame

station_image = pygame.image.load("assets/SpaceStation_tileset.png")

wall_bare = [station_image.subsurface((16, 23, 48, 41)),
             station_image.subsurface((80, 23, 48, 44)),
             station_image.subsurface((144, 23, 48, 41))]
             
floor = station_image.subsurface((208, 80, 32, 32))

wall_right = station_image.subsurface((80, 144, 16, 48))
wall_right_corner = station_image.subsurface((208, 18, 16, 46))

wall_left = station_image.subsurface((112, 144, 16, 48))
wall_left_corner = station_image.subsurface((240, 18, 16, 46))