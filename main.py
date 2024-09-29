import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #creating empty groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #declaring object container gorups
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Player.containers = updatable, drawable
    Shot.containers = updatable, drawable, shots
    
    #create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update objects's position
        for obj in updatable:
            obj.update(dt)

        #collision check
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
                    

        #rendering
        screen.fill("black") 

        #draw object
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
    
        dt = clock.tick(60) / 1000 #limit frame rate to 60 FPS

    

if __name__ == "__main__":
    main()