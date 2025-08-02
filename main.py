#Imports
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #intialise clock variables to set FPS to 60
    clock = pygame.time.Clock()
    dt = 0

    #Setup groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    #Instantiate Player Object
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))


    #Main Game Loop
    while True:
        #Exit Criteria
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")

        updatable.update(dt)

        for object in drawable:
            object.draw(screen)
        
        
        #Screen Refresh Loop - uses dt to set 60 fps
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

    


if __name__ == "__main__":
    main()
