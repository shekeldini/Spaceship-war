import random
import pygame
from classes.enemy.enemy import Enemy


class Boss(Enemy):
    def __init__(self, image, pos, size):
        self.speed = 5
        self.damage = 5
        self.health = 200
        self.score = 50
        super().__init__(image, pos, size, self.speed, self.damage, self.health, self.score)

    def shot(self, sprites):
        n = random.random()
        if n >= 0.9:
            sprites.create_enemy_bullet(self.pos, self.rotate_bullet(sprites), self.bullet_size, self.damage)

    def update(self, display, sprites):
        super().update(display, sprites)
        self.rotate(sprites)

    def rotate(self, sprites):
        direction = sprites.player.sprites()[0].get_pos() - self.pos
        radius, angle = direction.as_polar()
        correction_angle = 90
        rotate_coef = -angle - correction_angle
        self.image = pygame.transform.rotate(self.orig_image, rotate_coef)
        self.rect = self.image.get_rect(center=self.pos)


