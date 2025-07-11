from src.space_station_map import *
from src.level import Level
from src.player import Player
from src.static import *
from src.minion_1 import Minion1
from src.minion_2 import Minion2
from src.minion_3 import Minion3
from src.minion_4 import Minion4
from src.deco_map import *
from src.hud import *
import pygame
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self, t, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.b_type = t
        
        if self.b_type == SHOTGUN:
            self.animation = shell
        else:
            self.animation  = bullet
        self.frame      = 0
        self.anim_time  = .3
        self.anim_timer = 0
        self.frame_time = self.anim_time / len(self.animation)
        
        self.direction = direction
        self.timer     = 5
        
        if self.direction == RIGHT:
            self.image = self.animation[self.frame]
        else:
            self.image = pygame.transform.flip(self.animation[self.frame], True, False)
        self.rect   = self.image.get_rect()
        self.mask   = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
    
    def update(self, screen, dt):
        if self.anim_timer > self.anim_time:
            self.frame = 0
            self.anim_timer = 0
            if self.direction == RIGHT:
                self.image = self.animation[self.frame]
            else:
                self.image = pygame.transform.flip(self.animation[self.frame], True, False)
        elif self.anim_timer > self.frame_time + (self.frame_time * self.frame):
            self.frame += 1
            if self.direction == RIGHT:
                self.image = self.animation[self.frame]
            else:
                self.image = pygame.transform.flip(self.animation[self.frame], True, False)
                
        self.anim_time += dt
            
        if self.direction is RIGHT:
            self.rect.x += 300 * dt
        if self.direction is LEFT:
            self.rect.x -= 300 * dt
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        self.timer -= dt

class World:
    def __init__(self):
        self.level = Level(1)
        self.enemies = []
        self.bullets = []
        self.walls = []
        self.player = Player()
        self.hud = HUD(self)
        self.plaer_shot = False
        
        self.surface = pygame.Surface((4896, 2304))
        self.background = pygame.Surface((4896, 2304))
        
    def spawn_enemy(self):
        num_enemies = 0
        req_enemies = random.randint((len(self.level.rooms)), (len(self.level.rooms) * 4))
        
        
        while num_enemies <= req_enemies:
            x, y = 0, 0
            for i in range(len(self.level.rooms)):
                for j in range(len(self.level.rooms[i])):
                    if self.level.rooms[i][j] == 1 and random.randint(0, 1000) < 100 and (i != 4 and j != 4):
                        e_x = random.randint(50, 494) + x
                        e_y = random.randint(50, 206) + y
                        e = random.randint(0, 1000)
                        if e > 900:
                            self.enemies.append(Minion4(self, e_x, e_y))
                        elif e > 800:
                            self.enemies.append(Minion3(self, e_x, e_y))
                        elif e > 500:
                            self.enemies.append(Minion2(self, e_x, e_y))
                        else:
                            self.enemies.append(Minion1(self, e_x, e_y))
                        num_enemies += 1
                        spawned = True
                    x += 540
                x = 0
                y += 256
                    

    def build(self):
        x, y = 0, 0
        self.level = Level(1)
        self.enemies = []
        self.bullets = []
        self.walls = []
        self.plaer_shot = False
        self.level.build()
        self.background.fill(BLACK)
        self.surface.fill(BLACK)
        
        for i in range(len(self.level.rooms)):
            for j in range(len(self.level.rooms[i])):
                
                u, d, l, r = 0, 0, 0, 0
                if self.level.rooms[i][j] == 1:
                    for k in range(8):
                        for q in range(17):
                            self.background.blit(floor, ((32 * q) + x, (32 * k) + y)) 
                    if self.level.rooms[i - 1][j] == 1:
                        u = 1
                    if self.level.rooms[i + 1][j] == 1:
                        d = 1
                    if self.level.rooms[i][j - 1] == 1:
                        l = 1
                    if self.level.rooms[i][j + 1] == 1:
                        r = 1
                    
                    
                    if r == 0:
                        wall = pygame.Rect(x + 539, y, 5, 226)
                        self.walls.append(wall)
                        
                        for o in range(6):
                            if u == 0 and o == 0:
                                self.background.blit(wall_right_corner, (x + 537, y - 41))
                            self.background.blit(wall_right, (x + 537, y + (48 * o)))
                    if u == 0:
                        wall = pygame.Rect(x, y - 30, 544, 5)
                        self.walls.append(wall)
                        for o in range(12):
                            if o == 11:
                                w = random.choice((wall_bare[0], wall_bare[1]))
                                self.background.blit(w, (x + (48 * o), y - 41), (0, 0, 16, w.get_rect().height)) 
                            else:
                                self.background.blit(random.choice(wall_bare), (x + (48 * o), y - 41))
                    if l == 0:
                        wall = pygame.Rect(x, y, 5, 226)
                        self.walls.append(wall)
                        for o in range(6):
                            if u == 0 and o == 0:
                                self.background.blit(wall_left_corner, (x, y - 41))
                            self.background.blit(wall_left, (x, y + (48 * o)))
                    if d == 0:
                        wall = pygame.Rect(x, y + 251, 544, 5)
                        self.walls.append(wall)
                        for o in range(12):
                            if o == 11:
                                w = random.choice((wall_bare[0], wall_bare[1]))
                                self.background.blit(w, (x + (48 * o), y + 251), (0, 0, 16, w.get_rect().height)) 
                            else:
                                self.background.blit(random.choice(wall_bare), (x + (48 * o), y + 251))
                    
                    
                x += 544
            x = 0
            y += 256
        
        self.spawn_enemy()
        self.surface.blit(self.background, (0, 0))
    
    def update(self, screen, dt):
        if self.player.state is SHOOTING and self.player.frame == 1 and not self.player_shot:
            if self.player.direction is RIGHT:
                self.bullets.append(Bullet(self.player.current_gun, self.player.rect.x + 27, self.player.rect.y + 14, self.player.direction))
            if self.player.direction is LEFT:
                self.bullets.append(Bullet(self.player.current_gun, self.player.rect.x, self.player.rect.y + 14, self.player.direction))
            self.player_shot = True
        if self.player.frame == 0:
            self.player_shot = False
        
        for b in self.bullets:
            self.surface.blit(self.background, (b.rect.x, b.rect.y), b.rect)
        for e in self.enemies:
            self.surface.blit(self.background, (e.rect.x - 5, e.rect.y - 5), (e.rect.x - 5, e.rect.y - 5, e.rect.width + 10, e.rect.height + 10))
            if e.state is BITING:
                if e.frame >= 3 and pygame.sprite.collide_mask(self.player, e) and not e.bit:
                    if type(e) is Minion4:
                        self.player.health -= 2
                    else:
                        self.player.health -= 1
                    e.bit = True
        self.surface.blit(self.background, (self.player.rect.x, self.player.rect.y), self.player.rect)
        
        self.player.mid_update(dt)
        
        col_rect = pygame.Rect(self.player.rect.x + self.player.dx, self.player.rect.y + self.player.dy, self.player.rect.width, self.player.rect.height)
        for wall in self.walls:
            if col_rect.colliderect(wall):
                was_touching = True
                if col_rect.bottom <= wall.top + 3:
                    self.player.dy = 0
                    self.player.rect.bottom = wall.top
                if col_rect.top >= wall.bottom - 3:
                    self.player.dy = 0
                    col_rect.top = wall.bottom
                if col_rect.right <= wall.left + 3:
                    self.player.dx = 0
                    self.player.rect.right = wall.left
                if col_rect.left >= wall.right - 3:
                    self.player.dx = 0
                    self.player.rect.left = wall.right
                
        self.player.update(self.surface, dt)
        for e in self.enemies:
            if e.state is BITING:
                self.player.new_state = IDLE
            e.mid_update(dt)    
            col_rect = pygame.Rect(e.rect.x + e.dx, e.rect.y + e.dy, e.rect.width, e.rect.height)
            for wall in self.walls:
                if col_rect.colliderect(wall):
                    if col_rect.bottom <= wall.top + 3:
                        e.dy = 0
                        e.rect.bottom = wall.top
                    if col_rect.top >= wall.bottom - 3:
                        e.dy = 0
                        col_rect.top = wall.bottom
                    if col_rect.right <= wall.left + 3:
                        e.dx = 0
                        e.rect.right = wall.left
                    if col_rect.left >= wall.right - 3:
                        e.dx = 0
                        e.rect.left = wall.right
            e.update(self.surface, dt)
            if e.health <= 0:
                self.player.xp += int(random.uniform(0, 1) * 100 * self.player.level)
                self.surface.blit(self.background, (e.rect.x, e.rect.y), e.rect)
                self.enemies.remove(e)
        for b in self.bullets:
            b.update(self.surface, dt)
            if b.timer <= 0:
                self.bullets.remove(b)
                self.surface.blit(self.background, (b.rect.x, b.rect.y), b.rect)
            for w in self.walls:
                if w.colliderect(b.rect):
                    self.bullets.remove(b)
                    self.surface.blit(self.background, (b.rect.x, b.rect.y), b.rect)
            for e in self.enemies:
                if pygame.sprite.collide_mask(b, e):
                    self.surface.blit(self.background, (e.rect.x, e.rect.y), e.rect)
                    if b.b_type is SHOTGUN:
                        e.health -= 75 * self.player.damage
                    if b.b_type is PISTOL:
                        e.health -= 10 * self.player.damage
                    if b.b_type is RIFLE:
                        e.health -= 20 * self.player.damage
                    self.bullets.remove(b)
                    print((e.health / e.max_health) * 32)
                    break
        
        screen.blit(self.surface, (0, 0), (self.player.rect.x - screen.get_rect().width / 2 + 32, self.player.rect.y - screen.get_rect().height / 2 + 32, screen.get_rect().width, screen.get_rect().height))
        
        pygame.draw.rect(screen, GREEN, (5, 20, (self.player.xp / (1000 * self.player.level * .6)) * 48, 6))
        pygame.draw.rect(screen, BLACK, (5, 20, 48, 6), width=2)
        xps = FONT.render(f"{self.player.xp} / {1000 * self.player.level * .6}", True, RED)
        screen.blit(xps, (5, 30))
        
        self.hud.update(screen)
        if self.player.health <= 0:
            self.player.new_state = DYING
            self.player.change_state()
            while self.player.state is DYING:
                dt = pygame.time.Clock().tick(60) / 1000
                self.surface.blit(self.background, (self.player.rect.x, self.player.rect.y), self.player.rect)
                self.player.update(self.surface, dt)
                screen.blit(self.surface, (0, 0), (self.player.rect.x - screen.get_rect().width / 2 + 32, self.player.rect.y - screen.get_rect().height / 2 + 32, screen.get_rect().width, screen.get_rect().height))
                pygame.display.update()
            
            while self.player.frame < 4:
                dt = pygame.time.Clock().tick(60) / 1000
                self.surface.blit(self.background, (self.player.rect.x, self.player.rect.y), self.player.rect)
                self.player.update(self.surface, dt)
                screen.blit(self.surface, (0, 0), (self.player.rect.x - screen.get_rect().width / 2 + 32, self.player.rect.y - screen.get_rect().height / 2 + 32, screen.get_rect().width, screen.get_rect().height))
                pygame.display.update()