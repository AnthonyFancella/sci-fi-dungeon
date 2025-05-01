import pygame
pygame.init()

RES = (720, 400)
PLAYER_START_POS = (2448, 1152)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)

FONT = pygame.font.SysFont("Noto Sans", 8)
UI_FONT = pygame.font.SysFont("Noto Sans", 16)

minion_one = "minion1"
minion_two = "minion2"

RIFLE    = "rifle"
PISTOL   = "pistol"
SHOTGUN  = "shotgun"
UNARMED  = "unarmed"
IDLE     = "idle"
WALKING  = "walking"
SHOOTING = "shooting"
RIGHT    = "right"
LEFT     = "left"
UP       = "up"
DOWN     = "down"
BITING   = "biting"
DYING    = "dying"
DEAD     = "dead"