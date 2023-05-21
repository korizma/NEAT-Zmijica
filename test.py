import pygame
import time

pygame.init()

gw = pygame.display.set_mode((400,400))
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)

gw.fill(red)
pygame.draw.rect(gw, green, pygame.Rect(20, 20, 20, 20))

pygame.display.update()

time.sleep(5)