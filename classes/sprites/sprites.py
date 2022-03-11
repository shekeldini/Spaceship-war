import pygame
import random

from classes.buffs.first_aid_kit import FirstAidKit
from classes.bullets.enemy_bullet import EnemyBullet
from classes.bullets.player_bullet import PlayerBullet
from classes.enemy.boss import Boss
from classes.enemy.ufo import UFO
from classes.spaceship.spaceship import Spaceship

from load_images import player_img, enemy_img, boss_img, first_aid_kit_img, bullet_img, rocket_img
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SIZE, UFO_SIZE, BOSS_SIZE, FIRST_AID_KIT_SIZE


class Sprites:
    def __init__(self):
        self.player = pygame.sprite.GroupSingle()
        self.player_bullets = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.buffs = pygame.sprite.Group()

    def create_player(self):
        self.player.add(
            Spaceship(
                image=player_img,
                pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                size=PLAYER_SIZE
            )
        )

    def create_ufo(self):
        width, height = UFO_SIZE
        pos = random.randint(width, SCREEN_WIDTH - width), random.randint(height, SCREEN_HEIGHT - height)
        self.enemy.add(
            UFO(
                image=enemy_img,
                pos=pos,
                size=UFO_SIZE
            )
        )

    def create_boss(self):
        width, height = BOSS_SIZE
        pos = random.randint(width, SCREEN_WIDTH - width), random.randint(height, SCREEN_HEIGHT - height)
        self.enemy.add(
            Boss(
                image=boss_img,
                pos=pos,
                size=BOSS_SIZE
            )
        )

    def create_first_aid_kit(self):
        width, height = FIRST_AID_KIT_SIZE
        pos = random.randint(width, SCREEN_WIDTH - width), random.randint(height, SCREEN_HEIGHT - height)
        self.buffs.add(
            FirstAidKit(
                image=first_aid_kit_img,
                pos=pos,
                size=FIRST_AID_KIT_SIZE
            )
        )

    def create_player_bullet(self, pos, rotate_coef, bullet_size):
        self.player_bullets.add(
            PlayerBullet(
                image=bullet_img,
                pos=pos,
                rotate_coef=rotate_coef,
                size=bullet_size
            )
        )

    def create_enemy_bullet(self, pos, rotate_bullet, bullet_size, damage):
        self.enemy_bullets.add(
            EnemyBullet(
                image=rocket_img,
                pos=pos,
                rotate_coef=rotate_bullet,
                size=bullet_size,
                damage=damage
            )
        )

    def has_boss(self):
        for i in self.enemy:
            if issubclass(i.__class__, Boss):
                return True
        return False

    def has_first_aid_kit(self):
        for i in self.buffs:
            if issubclass(i.__class__, FirstAidKit):
                return True
        return False

    def clear_sprites(self):
        self.player.empty()
        self.enemy.empty()
        self.enemy_bullets.empty()
        self.player_bullets.empty()

    def get_hero_score(self):
        return self.player.sprite.get_score()

    def get_hero_health(self):
        return int(self.player.sprite.get_health())

    def check_alive_hero(self):
        return self.player.sprite.is_alive()



