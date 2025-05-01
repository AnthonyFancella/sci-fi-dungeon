import pygame
from src.static import *
from src.world import World
from src.level_up import *

pygame.init()

flags = pygame.RESIZABLE | pygame.SCALED
screen = pygame.display.set_mode(RES, flags)
world = World()
levelup = LevelUp(world.player)
world.build()
running = True
font = pygame.font.SysFont("Noto Sans", 40)
game_over = font.render("Game Over", True, BLACK)
level_beat = font.render("Level Cleared!", True, BLACK)
yes       = font.render("YES", True, GREEN)
no        = font.render("NO", True, RED)
retry     = font.render("Again?", True, BLACK)
yes_rect = yes.get_rect()
no_rect  = no.get_rect()
yes_rect.x = RES[0] / 4
no_rect.x  = (RES[0] / 4 * 3)
yes_rect.y = RES[1] - 100
no_rect.y  = RES[1] - 100

game_over_coords = (screen.get_rect().width / 2 - game_over.get_rect().width / 2, screen.get_rect().height / 2 - game_over.get_rect().height / 2)
level_beat_coords = (screen.get_rect().width / 2 - level_beat.get_rect().width / 2, screen.get_rect().height / 2 - level_beat.get_rect().height / 2)
retry_coords = (screen.get_rect().width / 2 - retry.get_rect().width / 2, (screen.get_rect().height / 2 - retry.get_rect().height / 2) + 45)

while running:
    if world.player.health > 0 or len(world.enemies) > 0:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and world.player.state is not SHOOTING:
                    if world.player.state is not WALKING:
                        world.player.new_state = WALKING
                    world.player.direction = RIGHT
                    world.player.horizontal = RIGHT
                if event.key == pygame.K_LEFT:
                    if world.player.state is not WALKING:
                        world.player.new_state = WALKING
                    world.player.direction = LEFT
                    world.player.horizontal = LEFT
                if event.key == pygame.K_UP:
                    if world.player.state is not WALKING:
                        world.player.new_state = WALKING
                    world.player.vertical = UP
                if event.key == pygame.K_DOWN:
                    if world.player.state is not WALKING:
                        world.player.new_state = WALKING
                    world.player.vertical = DOWN
                if event.key == pygame.K_LCTRL and world.player.state is not SHOOTING and world.player.cooldown <= 0:
                    world.player.new_state = SHOOTING
                    if world.player.current_gun is SHOTGUN:
                        world.player.cooldown = 1.5
                    else:
                        world.player.cooldown = .15
                if event.key == pygame.K_r and world.player.state is not SHOOTING:
                    world.player.change_gun()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    if not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
                        if event.key == pygame.K_RIGHT and not keys[pygame.K_LEFT]:
                            world.player.new_state = IDLE
                            world.player.horizontal = None
                        elif event.key == pygame.K_RIGHT and keys[pygame.K_LEFT]:
                            world.player.direction = LEFT
                            world.player.horizontal = LEFT
                        if event.key == pygame.K_LEFT and not keys[pygame.K_RIGHT]:
                            world.player.new_state = IDLE
                            world.player.horizontal = None
                        elif event.key == pygame.K_LEFT and keys[pygame.K_RIGHT]:
                            world.player.direction = RIGHT
                            world.player.horizontal = RIGHT
                    elif keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                        if event.key == pygame.K_RIGHT and not keys[pygame.K_LEFT]:
                            world.player.horizontal = None
                        elif event.key == pygame.K_RIGHT and keys[pygame.K_LEFT]:
                            world.player.horizontal = LEFT
                            world.player.direction  = LEFT
                        if event.key == pygame.K_LEFT and not keys[pygame.K_RIGHT]:
                            world.player.horizontal = None
                        elif event.key == pygame.K_LEFT and keys[pygame.K_RIGHT]:
                            world.player.horizontal = UP
                            world.player.direction = RIGHT
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
                        if event.key == pygame.K_UP and not keys[pygame.K_DOWN]:
                            world.player.new_state = IDLE
                            world.player.vertical = None
                        elif event.key == pygame.K_UP and keys[pygame.K_DOWN]:
                            world.player.vertical = DOWN
                        if event.key == pygame.K_DOWN and not keys[pygame.K_UP]:
                            world.player.new_state = IDLE
                            world.player.vertical = None
                        elif event.key == pygame.K_DOWN and keys[pygame.K_UP]:
                            world.player.vertical = UP
                    elif keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                        if event.key == pygame.K_UP and not keys[pygame.K_DOWN]:
                            world.player.vertical = None
                        elif event.key == pygame.K_UP and keys[pygame.K_DOWN]:
                            world.player.vertical = DOWN
                        if event.key == pygame.K_DOWN and not keys[pygame.K_UP]:
                            world.player.vertical = None
                        elif event.key == pygame.K_DOWN and keys[pygame.K_UP]:
                            world.player.vertical = UP
                if event.key == pygame.K_LCTRL and world.player.state is SHOOTING and world.player.current_gun is RIFLE:
                    world.player.new_state = world.player.old_state
        
        dt = pygame.time.Clock().tick(60) / 1000
        

        world.update(screen, dt)

        pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yes_rect.collidepoint(event.pos):
                        if world.player.leveled:
                            screen.blit(world.surface, (0, 0), (world.player.rect.x - RES[0] / 2 + 32, world.player.rect.y - RES[1] / 2 + 32, RES[0], RES[1]))
                            levelup.level_up(screen)
                        world.build()
                        world.player.rect.x, world.player.rect.y = PLAYER_START_POS
                        world.player.health = world.player.max_health
                    elif no_rect.collidepoint(event.pos):
                        running = False
        if world.player.health <= 0:
            screen.blit(game_over, game_over_coords)
        else:
            screen.blit(level_beat, level_beat_coords)
        screen.blit(retry, retry_coords)
        screen.blit(yes, yes_rect)
        screen.blit(no, no_rect)
        pygame.display.flip()