import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

background = pygame.transform.scale(pygame.image.load("images/space.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
new_game_img = pygame.image.load("images/new_game.jpg")
player_img = pygame.image.load("images/spaceship.jpg")
enemy_img = pygame.image.load("images/UFO.jpg")
bullet_img = pygame.image.load("images/bullet.jpg")
rocket_img = pygame.image.load("images/rocket.jpg")
boss_img = [pygame.image.load("images/boss_1.jpg"),
            pygame.image.load("images/boss_2.jpg"),
            pygame.image.load("images/boss_3.jpg"),
            pygame.image.load("images/boss_4.jpg")]
first_aid_kit_img = pygame.image.load("images/first_aid_kit.jpg")
