import pygame
from src.static import *
from src.player_map import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.level      = 1
        self.damage     = 1
        self.xp         = 0
        self.max_health = 6
        self.leveled    = False
        self.xp_points  = 0
        
        self.anim_timer = 0
        self.anim_time  = .75
        self.frame      = 0
        self.animation  = player_idle
        self.state      = IDLE
        self.new_state  = IDLE
        self.old_state  = IDLE
        
        self.direction  = RIGHT
        self.horizontal = None
        self.vertical   = None
        
        self.current_gun = PISTOL
        self.cooldown    = 0
        
        self.image     = self.animation[self.frame]
        self.rect      = self.image.get_rect()
        self.mask      = pygame.mask.from_surface(self.image)
        self.rect.x    = 2448
        self.rect.y    = 1152
        self.dx        = 0
        self.dy        = 0
        
        self.health = 6
        
    def animate(self, dt):
        frame_time = self.anim_time / len(self.animation)
        
        if self.state is not SHOOTING:
            if self.state is DYING:
                if self.anim_timer > self.anim_time:
                    self.new_state = DEAD
                    self.anim_timer = 0
                    self.frame      = 0
                    if self.direction == LEFT:
                        self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                    else:
                        self.image = self.animation[self.frame]
                    self.mask  = pygame.mask.from_surface(self.image)
                elif self.anim_timer > frame_time + (frame_time * self.frame):
                    self.frame += 1
                    if self.direction == LEFT:
                        self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                    else:
                        self.image = self.animation[self.frame]
                    self.mask  = pygame.mask.from_surface(self.image)
            else:
                if self.anim_timer > self.anim_time:
                    self.anim_timer = 0
                    self.frame      = 0
                    if self.direction == LEFT:
                        self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                    else:
                        self.image = self.animation[self.frame]
                    self.mask  = pygame.mask.from_surface(self.image)
                elif self.anim_timer > frame_time + (frame_time * self.frame):
                    self.frame += 1
                    if self.direction == LEFT:
                        self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                    else:
                        self.image = self.animation[self.frame]
                    self.mask  = pygame.mask.from_surface(self.image)
        else:
            if self.current_gun is RIFLE:
                if self.anim_timer > self.anim_time:
                    self.anim_timer = 0
                    self.frame      = 0
                    if self.direction == LEFT:
                        self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                    else:
                        self.image = self.animation[self.frame]
                    self.mask       = pygame.mask.from_surface(self.image)
                elif self.anim_timer > frame_time + (frame_time * self.frame):
                    self.frame += 1
                    if self.direction == LEFT:
                        self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                    else:
                        self.image = self.animation[self.frame]
                    self.mask   = pygame.mask.from_surface(self.image)
            else:
                if self.anim_timer > self.anim_time:
                    self.new_state = self.old_state
                    self.anim_timer = 0
                    self.frame = 0
                    if self.direction == LEFT:
                        self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                    else:
                        self.image = self.animation[self.frame]
                    self.mask  = pygame.mask.from_surface(self.image)
                elif self.anim_timer > frame_time + (frame_time * self.frame):
                    self.frame += 1
                    if self.direction == LEFT:
                        self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                    else:
                        self.image = self.animation[self.frame]
                    self.mask  = pygame.mask.from_surface(self.image)
        
        self.anim_timer += dt
    
    def change_state(self):
        if self.state == self.new_state:
            pass
        else:
            self.old_state = self.state
            
            if self.new_state == WALKING and self.current_gun is UNARMED:
                self.animation  = player_unarmed_walking
                self.anim_time  = .5
                self.frame      = 0
                self.anim_timer = 0
                self.state      = WALKING
            elif self.new_state == WALKING and self.current_gun is not UNARMED:
                if self.current_gun is PISTOL:
                    self.animation  = player_pistol_walking
                    self.anim_time  = .5
                    self.frame      = 0
                    self.anim_timer = 0
                    self.state      = WALKING
                if self.current_gun is SHOTGUN:
                    self.animation  = player_shotgun_walking
                    self.anim_time  = .5
                    self.frame      = 0
                    self.anim_timer = 0
                    self.state      = WALKING
                if self.current_gun is RIFLE:
                    self.animation  = player_rifle_walking
                    self.anim_time  = .5
                    self.frame      = 0
                    self.anim_timer = 0
                    self.state      = WALKING
            elif self.new_state == IDLE:
                self.animation  = player_idle
                self.anim_time  = .75
                self.frame      = 0
                self.anim_timer = 0
                self.state      = IDLE
            elif self.new_state == SHOOTING:
                if self.current_gun == PISTOL:
                    self.animation  = player_pistol_fire
                    self.anim_time  = .2
                    self.frame      = 0
                    self.anim_timer = 0
                    self.state      = SHOOTING
                if self.current_gun == SHOTGUN:
                    self.animation  = player_shotgun_fire
                    self.anim_time  = .2
                    self.frame      = 0
                    self.anim_timer = 0
                    self.state      = SHOOTING
                if self.current_gun == RIFLE:
                    self.animation  = player_rifle_fire
                    self.anim_time  = .2
                    self.frame      = 0
                    self.anim_timer = 0
                    self.state      = SHOOTING
            elif self.new_state == DYING:
                self.animation  = player_dying
                self.anim_time  = 3
                self.frame      = 0
                self.anim_timer = 0
                self.state      = DYING
            elif self.new_state == DEAD:
                self.animation  = player_death
                self.anim_time  = 1
                self.frame      = 0
                self.anim_timer = 0
                self.state      = DEAD
    
    def change_gun(self):
        if self.current_gun is PISTOL and self.level >= 5:
            if self.state is WALKING:
                self.animation = player_shotgun_walking
            self.current_gun = SHOTGUN
        elif self.current_gun is SHOTGUN and self.level >= 20:
            if self.state is WALKING:
                self.animation = player_rifle_walking
            self.current_gun = RIFLE
        elif self.current_gun is RIFLE:
            if self.state is WALKING:
                self.animation = player_unarmed_walking
            self.current_gun = UNARMED
        elif self.current_gun is UNARMED:
            if self.state is WALKING:
                self.animation = player_pistol_walking
            self.current_gun = PISTOL
        else:
            if self.state is WALKING:
                self.animation = player_unarmed_walking
            self.current_gun = UNARMED
    
    def mid_update(self, dt):
        if self.horizontal is RIGHT:
            self.dx = 95 * dt
        if self.horizontal is LEFT:
            self.dx = -95 * dt
        if self.vertical is UP:
            self.dy = -90 * dt
        if self.vertical is DOWN:
            self.dy = 90 * dt
    
    def update(self, screen, dt):
        self.change_state()
        if self.xp >= (1000 * self.level * .6):
            self.level += 1
            self.xp_points += 1
            self.leveled = True
        if self.state is WALKING:
            if self.horizontal is RIGHT:
                self.rect.x += self.dx
            if self.horizontal is LEFT:
                self.rect.x += self.dx
            if self.vertical is UP:
                self.rect.y += self.dy
            if self.vertical is DOWN:
                self.rect.y += self.dy
        self.animate(dt)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        if self.cooldown > 0:
            self.cooldown -= dt