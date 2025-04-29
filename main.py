import pygame
from src.static import *
from src.world import World

pygame.init()

flags = pygame.RESIZABLE | pygame.SCALED
screen = pygame.display.set_mode(RES, flags)
world = World()
world.build()
running = True
font = pygame.font.SysFont("Noto Sans", 40)
game_over = font.render("Game Over", True, RED)

game_over_coords = (screen.get_rect().width / 2 - game_over.get_rect().width / 2, screen.get_rect().height / 2 - game_over.get_rect().height / 2)

while running:
    if world.player.health > 0:
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
        screen.blit(game_over, game_over_coords)
        pygame.display.flip()