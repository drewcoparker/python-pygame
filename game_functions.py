import sys
from hero import Hero
import pygame
from settings import Settings


def check_events(hero, start_button, game_settings):
    for event in pygame.event.get():
        # The user clicks on the red x to close
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if start_button.rect.collidepoint(mouse_x, mouse_y):
                game_settings.game_active = True
                bg_music = pygame.mixer.Sound('faf.wav')
                bg_music.play()
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
