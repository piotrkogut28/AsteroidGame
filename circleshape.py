import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen,"white",self.triangle(),2)
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def isColliding(self,circle_object):
        distance = pygame.math.Vector2.distance_to(circle_object.position,self.position)
        if distance <= circle_object.radius+self.radius:
            return True
        else:
            return False