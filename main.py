import pygame
from settings import Settings
from hero import Hero
from game_functions import check_events
from pygame.sprite import Group, groupcollide
from enemy import Enemy
from button import Start_Button

# initialize all of the pygame modules
pygame.init()

# Create an object out of our settings class and assign its properties to pygame
game_settings = Settings()
screen = pygame.display.set_mode(game_settings.screen_size)
hero_group = Group()
hero = Hero(screen, game_settings)
hero_group.add(hero)
enemies = Group()
enemies.add(Enemy(screen, game_settings))

start_button = Start_Button(screen)

# Put a message on the status bar, so the player knows the game is initialized
pygame.display.set_caption("Monster Attack!")


while 1:
    # Check for key presses
    check_events(hero, start_button, game_settings)

    screen.fill(game_settings.bg_color)

    for hero in hero_group.sprites():
        hero.update_me()
        hero.draw_me()

    for enemy in enemies.sprites():
        enemy.update_me(hero)
        enemy.draw_me()

    hero_died = groupcollide(hero_group, enemies, True, True)
    if hero_died:
        print 'You lost!'
        game_settings.game_active = False

    if game_settings.game_active == False:
        start_button.draw_button()

    start_button.draw_button()
    # Flip = wipe it out
    pygame.display.flip()
