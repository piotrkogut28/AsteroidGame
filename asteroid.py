import circleshape
import pygame
from constants import *
import random


class Asteroid(circleshape.CircleShape):
    Asteroids_destroyed = 0
    def __init__(self, x, y, radius):
          super().__init__(x,y,radius)
    
        
          
    def draw(self, screen):
         pygame.draw.circle(screen,"white",self.position,self.radius,2)
         
    def update(self, dt):
         self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            Asteroid.Asteroids_destroyed += 1
              
            return
        else:
            random_angle = random.uniform(20,50)
           
            new_radius = self.radius - ASTEROID_MIN_RADIUS
              
            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)

            asteroid1= Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = a * 1.2

            asteroid2= Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2.velocity = b * 1.2

             