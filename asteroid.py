import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        #Generate a new random angle
        new_angle = random.uniform(20,50)

        #create 2 new velocities
        new_velocity_1 = self.velocity.rotate(new_angle)
        new_velocity_2 = self.velocity.rotate(-new_angle)

        self.radius -= ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid.velocity = new_velocity_1 * 1.2

        asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid.velocity = new_velocity_2 * 1.2

