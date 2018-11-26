import pygame as p
from pygame.locals import *
import os
p.init()
screen=p.display.set_mode((800, 600))
p.display.pygame.display.set_caption("Slither")
while True:
	for event in pygame.event.pygame.event.get():
		print(event)