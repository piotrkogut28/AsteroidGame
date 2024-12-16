import constants
from player import Player
import pygame
from asteroid import Asteroid
import asteroidfield
from circleshape import CircleShape
import sys
from shot import Shot
import math
def main():
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable,drawable,shots)
    asteroidfield.AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)


    player1 = Player(x = constants.SCREEN_WIDTH / 2 ,y = constants.SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()
  
    
    pygame.init()
    clock1 = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill("black")
        for drawable_object in drawable:
            drawable_object.draw(screen)
      
        pygame.display.flip() 
        
        dt = clock1.tick(60)/1000
        for updatable_object in updatable:
            updatable_object.update(dt)

        for asteroid in asteroids:
            if asteroid.isColliding(player1):
                print("Game over!")
                print(f"Zniszczyłeś: {Asteroid.Asteroids_destroyed} asteroid!")
                print(f"Wystrzeliłeś: {Shot.shots_counter} naboi!")
                czas = pygame.time.get_ticks()/1000
                print(f"Przetrwałeś {round(czas,1)} sekund!")
                sys.exit()

            for shot in shots:
                if asteroid.isColliding(shot):
                    asteroid.split()
                    shot.kill()
        
            
        
        


if __name__ == "__main__":
    main()
