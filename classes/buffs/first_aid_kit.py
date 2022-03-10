import pygame
from pygame.math import Vector2


class FirstAidKit(pygame.sprite.Sprite):
    def __init__(self, image, pos, size):
        super().__init__()
        self.width, self.height = size
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.health = 20

    def check_collide_with_player(self, sprites):
        if pygame.sprite.spritecollide(self, sprites.player, False):
            sprites.player.sprite.get_heal(self.health)
            self.kill()

    def update(self, sprites):
        self.check_collide_with_player(sprites)
