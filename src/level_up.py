import pygame
from src.static import *

pygame.init()

class LevelUp():
    def __init__(self, player):
        self.player = player
        self.button_image = pygame.image.load("assets/Sci-fi UI 16x16.png")
        self.add_button = self.button_image.subsurface((0, 208, 16, 16))
        self.points = self.player.xp_points
        
        self.health_button_rect = pygame.Rect(364, 180, 16, 16)
        self.damage_button_rect = pygame.Rect(364, 204, 16, 16)
        self.health = UI_FONT.render("Health", True, GREEN)
        self.damage = UI_FONT.render("Damage", True, RED)

    def level_up(self, screen):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.player.xp_points = self.points
                    self.player.leveled = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.health_button_rect.collidepoint(event.pos):
                            self.player.health += 2
                        if self.damage_button_rect.collidepoint(event.pos):
                            self.player.damage += 1
            
            current_health = UI_FONT.render(str(self.player.max_health), True, GREEN)
            current_damage = UI_FONT.render(str(self.player.damage), True, RED)
            
            screen.blit(self.add_button, self.damage_button_rect)
            screen.blit(self.add_button, self.health_button_rect)
            screen.blit(self.health, ((RES[0] / 2) - self.health.get_rect().width - 4, 176))
            screen.blit(self.damage, ((RES[0] / 2) - self.damage.get_rect().width - 4, 200))
            screen.blit(current_health, (RES[0] / 2 - self.health.get_rect().width - 4 - current_health.get_rect().width - 4, 176))
            screen.blit(current_damage, (RES[0] / 2 - self.damage.get_rect().width - 4 - current_damage.get_rect().width - 4, 200))
            pygame.display.flip()