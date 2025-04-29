import pygame

player_image = pygame.image.load("assets/ROBO WITH HANDS.png")

player_idle = [player_image.subsurface((0, 0, 32, 32)),
               player_image.subsurface((32, 0, 32, 32)),
               player_image.subsurface((64, 0, 32, 32)),
               player_image.subsurface((96, 0, 32, 32))]
               
player_unarmed_walking = [player_image.subsurface((0, 32, 32, 32)),
                          player_image.subsurface((32, 32, 32, 32)),
                          player_image.subsurface((64, 32, 32, 32)),
                          player_image.subsurface((96, 32, 32, 32))]
                          
player_rolling = [player_image.subsurface((0, 64, 32, 32)),
                  player_image.subsurface((32, 64, 32, 32)),
                  player_image.subsurface((64, 64, 32, 32)),
                  player_image.subsurface((96, 64, 32, 32)),
                  player_image.subsurface((128, 64, 32, 32)),
                  player_image.subsurface((160, 64, 32, 32)),
                  player_image.subsurface((192, 64, 32, 32)),
                  player_image.subsurface((224, 64, 32, 32))]
                  
player_pistol_fire = [player_image.subsurface((0, 96, 32, 32)),
                      player_image.subsurface((32, 96, 32, 32)),
                      player_image.subsurface((64, 96, 32, 32))]
                      
player_rifle_fire = [player_image.subsurface((0, 128, 32, 32)),
                     player_image.subsurface((32, 128, 32, 32))]

player_shotgun_fire = [player_image.subsurface((0, 160, 32, 32)),
                       player_image.subsurface((32, 160, 32, 32)),
                       player_image.subsurface((64, 160, 32, 32))]
                       
player_dying = [player_image.subsurface((0, 192, 32, 32)),
                player_image.subsurface((32, 192, 32, 32)),
                player_image.subsurface((0, 192, 32, 32)),
                player_image.subsurface((32, 192, 32, 32)),
                player_image.subsurface((0, 192, 32, 32)),
                player_image.subsurface((32, 192, 32, 32)),
                player_image.subsurface((0, 192, 32, 32))]
                
player_death = [player_image.subsurface((0, 224, 32, 32)),
                player_image.subsurface((32, 224, 32, 32)),
                player_image.subsurface((64, 224, 32, 32)),
                player_image.subsurface((128, 224, 32, 32)),
                player_image.subsurface((160, 224, 32, 32))]
                
player_pistol_walking = [player_image.subsurface((0, 256, 32, 32)),
                         player_image.subsurface((32, 256, 32, 32)),
                         player_image.subsurface((64, 256, 32, 32)),
                         player_image.subsurface((96, 256, 32, 32))]
                         
player_rifle_walking = [player_image.subsurface((0, 288, 32, 32)),
                        player_image.subsurface((32, 288, 32, 32)),
                        player_image.subsurface((64, 288, 32, 32)),
                        player_image.subsurface((96, 288, 32, 32))]
                        
player_shotgun_walking = [player_image.subsurface((0, 320, 32, 32)),
                          player_image.subsurface((32, 320, 32, 32)),
                          player_image.subsurface((64, 320, 32, 32)),
                          player_image.subsurface((96, 320, 32, 32))]
                          