import pygame, random
from src.static import *
from src.minion_2_map import *

class Minion2(pygame.sprite.Sprite):
    def __init__(self, world, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.world = world
        
        self.animation  = minion_2_idle
        self.anim_timer = 0
        self.anim_time  = .75
        self.frame      = 0
        self.cooldown   = 0
        
        self.state     = IDLE
        self.new_state = IDLE
        self.bit       = False
        
        self.direction  = LEFT
        self.horizontal = None
        self.vertical   = None
        
        self.health = random.randint(150, self.world.player.level * 225)
        
        self.image  = self.animation[self.frame]
        self.rect   = self.image.get_rect()
        self.mask   = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.dx     = 0
        self.dy     = 0
        
    def change_state(self):
        if self.new_state == self.state:
            pass
        else:
            if self.new_state == WALKING:
                self.state      = WALKING
                self.animation  = minion_2_walk
                self.frame      = 0
                self.anim_time  = .5
                self.anim_timer = 0
            if self.new_state == BITING:
                self.state      = BITING
                self.animation  = minion_2_bite
                self.frame      = 0
                self.anim_time  = .3
                self.anim_timer = 0
            if self.new_state == IDLE:
                self.state      = IDLE
                self.animation  = minion_2_idle
                self.frame      = 0
                self.anim_time  = .75
                self.anim_timer = 0
        
    def animate(self, dt):
        frame_time = self.anim_time / len(self.animation)
        
        if self.state is not BITING:
            if self.anim_timer > self.anim_time:
                self.anim_timer = 0
                self.frame      = 0
                if self.direction is LEFT:
                    self.image  = pygame.transform.flip(self.animation[self.frame], True, False)
                else:
                    self.image  = self.animation[self.frame]
                self.mask       = pygame.mask.from_surface(self.image)
            elif self.anim_timer >= frame_time + (frame_time * self.frame):
                self.frame     += 1
                if self.direction is LEFT:
                    self.image  = pygame.transform.flip(self.animation[self.frame], True, False)
                else:
                    self.image  = self.animation[self.frame]
                self.mask       = pygame.mask.from_surface(self.image)
        else:
            if self.anim_timer > self.anim_time:
                self.anim_timer = 0
                self.frame      = 0
                if self.direction is LEFT:
                    self.image  = pygame.transform.flip(self.animation[self.frame], True, False)
                else:
                    self.image  = self.animation[self.frame]
                self.new_state  = IDLE
                self.bit        = False
                self.cooldown   = 1
                self.mask       = pygame.mask.from_surface(self.image)
            elif self.anim_timer >= frame_time + (frame_time * self.frame):
                self.frame     += 1
                if self.direction is LEFT:
                    self.image  = pygame.transform.flip(self.animation[self.frame], True, False)
                else:
                    self.image  = self.animation[self.frame]
                self.mask       = pygame.mask.from_surface(self.image)
                
        self.anim_timer += dt
    def control(self):
        if pygame.sprite.collide_mask(self, self.world.player) and self.state is not BITING:
            self.new_state = BITING
        elif abs(self.rect.x - self.world.player.rect.x) < 810 and abs(self.rect.y - self.world.player.rect.y) < 384 and self.state is not BITING:
            self.new_state = WALKING
            if abs(self.rect.x - self.world.player.rect.x) <= 5:
                self.horizontal = None
            elif self.world.player.rect.x > self.rect.x:
                self.direction = RIGHT
                self.horizontal = RIGHT
            elif self.world.player.rect.x < self.rect.x:
                self.direction = LEFT
                self.horizontal = LEFT
            if abs(self.rect.y - self.world.player.rect.y) <= 5:
                self.vertical = None
            elif self.world.player.rect.y > self.rect.y:
                self.vertical = DOWN
            elif self.world.player.rect.y < self.rect.y:
                self.vertical = UP
        else:
            if self.state is not BITING:
                self.new_state = IDLE
            
        
    def mid_update(self, dt):
        if self.horizontal is RIGHT:
            self.dx = 85 * dt
        if self.horizontal is LEFT:
            self.dx = -85 * dt
        if self.vertical is UP:
            self.dy = -70 * dt
        if self.vertical is DOWN:
            self.dy = 70 * dt
            
        
    def update(self, screen, dt):
        if self.cooldown <= 0:
            self.control()
            self.change_state()
            self.rect.x += self.dx
            self.rect.y += self.dy
            self.animate(dt)
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            self.change_state()
            self.animate(dt)
            screen.blit(self.image, (self.rect.x, self.rect.y))
            self.cooldown -= dt