import pygame
import math
from pygame.math import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, pos, rotate_coef, size, speed, damage):
        super().__init__()
        self._size = size
        self._rotate_coef = - rotate_coef - 90
        self.image = pygame.transform.scale(image.convert_alpha(), self._size)
        self._orig_image = self.image
        self.image = pygame.transform.rotate(self._orig_image, rotate_coef)
        self.rect = self.image.get_rect(center=pos)
        self._pos = Vector2(pos)
        self._speed = speed
        self._damage = damage

    def _check_out_display(self):
        if self._pos.x < 0 or self._pos.x > SCREEN_WIDTH or self._pos.y < 0 or self._pos.y > SCREEN_HEIGHT:
            return True
        return False

    def update(self):
        if self._check_out_display():
            self.kill()
        self._move()

    def _move(self):
        self._pos.x += self._speed * math.cos(math.radians(self._rotate_coef))
        self._pos.y += self._speed * math.sin(math.radians(self._rotate_coef))
        self.rect = self.image.get_rect(center=self._pos)

    def get_damage(self):
        return self._damage
