import pygame
import math
from pygame.math import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, pos, rotate_coef, size, speed, damage):
        super().__init__()
        self.size = size
        self.rotate_coef = - rotate_coef - 90
        self.image = pygame.transform.scale(image.convert_alpha(), self.size)
        self.orig_image = self.image
        self.image = pygame.transform.rotate(self.orig_image, rotate_coef)
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.speed = speed
        self.damage = damage

    def check_out_display(self):
        if self.pos.x < 0 or self.pos.x > SCREEN_WIDTH or self.pos.y < 0 or self.pos.y > SCREEN_HEIGHT:
            return True
        return False

    def update(self):
        if self.check_out_display():
            self.kill()
        self.move()

    def move(self):
        self.pos.x += self.speed * math.cos(math.radians(self.rotate_coef))
        self.pos.y += self.speed * math.sin(math.radians(self.rotate_coef))
        self.rect = self.image.get_rect(center=self.pos)

    def get_damage(self):
        return self.damage
