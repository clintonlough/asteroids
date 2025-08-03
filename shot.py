#Imports
import pygame
import sys
from constants import *
from player import Player

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius = SHOT_RADIUS


    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt    
