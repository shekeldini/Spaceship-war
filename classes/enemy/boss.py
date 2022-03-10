import random
import pygame
from classes.enemy.enemy import Enemy


class Boss(Enemy):
    def __init__(self, image, pos, size):
        self._speed = 5
        self._damage = 5
        self._health = 200
        self._score = 50
        super().__init__(image, pos, size, self._speed, self._damage, self._health, self._score)

    def _shot(self, sprites):
        n = random.random()
        if n >= 0.9:
            sprites.create_enemy_bullet(self._pos, self._rotate_bullet(sprites), self._bullet_size, self._damage)

    def update(self, display, sprites):
        super().update(display, sprites)
        self._rotate(sprites)

    def _rotate(self, sprites):
        direction = sprites.player.sprite.get_pos() - self._pos
        radius, angle = direction.as_polar()
        correction_angle = 90
        rotate_coef = -angle - correction_angle
        self.image = pygame.transform.rotate(self._orig_image, rotate_coef)
        self.rect = self.image.get_rect(center=self._pos)
