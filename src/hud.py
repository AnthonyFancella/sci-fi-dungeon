import pygame
from src.deco_map import *

class HUD():
    def __init__(self, world):
        self.player = world.player
        self.max_health = world.player.max_health

    def update(self, screen):
        hearts = self.max_health // 2

        for i in range(hearts):
            screen.blit(health[2], (5 + (16 * i), 0))
            
        for i in range(self.player.health):
            if i == self.player.health - 1:
                if self.player.health % 2 == 0:
                    screen.blit(health[0], (5 + ((16 * (i / 2)) - 8), 0))
                else:
                    screen.blit(health[1], (5 + (16 * (i / 2)), 0))
            else:
                if i % 2 != 0:
                    screen.blit(health[0], (5 + ((16 * (i / 2)) - 8), 0))
                else:
                    pass