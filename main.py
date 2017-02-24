import pygame
import sys
from settings import Settings
from hero import Hero

# initialize all of the pygame modules
pygame.init()

# Create an object out of our settings class and assign its properties to pygame
game_settings = Settings()
screen = pygame.display.set_mode(game_settings.screen_size)
hero = Hero(screen, game_settings)

# Put a message on the status bar, so the player knows the game is initialized
pygame.display.set_caption("Monster Attack!")
while 1:
    for event in pygame.event.get():
        # The user clicks on the red x to close
        if event.type == pygame.QUIT:
            sys.exit()
        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = True
            elif event.key == pygame.K_LEFT:
                hero.moving_left = True
            elif event.key == pygame.K_UP:
                hero.moving_up = True
            elif event.key == pygame.K_DOWN:
                hero.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = False
            elif event.key == pygame.K_LEFT:
                hero.moving_left = False
            elif event.key == pygame.K_UP:
                hero.moving_up = False
            elif event.key == pygame.K_DOWN:
                hero.moving_down = False

    screen.fill(game_settings.bg_color)
    hero.update_me(game_settings)
    hero.draw_me()
    # Flip = wipe it out
    pygame.display.flip()
