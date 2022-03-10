import pygame
from pygame.math import Vector2


class FirstAidKit(pygame.sprite.Sprite):
    def __init__(self, image, pos, size):
        super().__init__()
        self._width, self._height = size
        self.image = pygame.transform.scale(image, (self._width, self._height))
        self._orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self._pos = Vector2(pos)
        self._health = 20

    def _check_collide_with_player(self, sprites):
        if pygame.sprite.spritecollide(self, sprites.player, False):
            sprites.player.sprite.get_heal(self._health)
            self.kill()

    def update(self, sprites):
        self._check_collide_with_player(sprites)
