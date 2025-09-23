import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, other_circle):
    #if distance between the centers of the two circles is less than or equal to the sum of the radii > return True
        return self.position.distance_to(other_circle.position) <= self.radius + other_circle.radius
         



#how does this class and asteroid inherit from screen on main
#and what actually is screen?