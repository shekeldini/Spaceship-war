import math
import pygame
import random
from pygame.math import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos, size, speed, damage, health, score):
        super().__init__()
        self._width, self._height = size
        self.image = pygame.transform.scale(self._choice_image(image).convert_alpha(), (self._width, self._height))
        self._orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self._pos = Vector2(pos)
        self._rotate_coef = random.uniform(-180, 180)
        self._current_health = health
        self._max_health = health
        self._health_bar_length = 100
        self._health_ratio = self._max_health / self._health_bar_length
        self._speed = speed
        self._damage = damage
        self._score = score
        self._bullet_size = 2, 20

    @staticmethod
    def _choice_image(images):
        if isinstance(images, list):
            return random.choice(images)
        return images

    def _health_bar(self, display):
        health_bar_width = int(self._current_health / self._health_ratio)
        r_x = self.rect.x
        r_y = self.rect.y
        health_bar = pygame.Rect(r_x - 10, r_y - 50, health_bar_width, 20)
        pygame.draw.rect(display, (255, 0, 0), (r_x - 10, r_y - 50, self._health_bar_length, 20))
        pygame.draw.rect(display, (0, 255, 0), health_bar)
        pygame.draw.rect(display, (255, 255, 255), (r_x - 10, r_y - 50, self._health_bar_length, 20), 4)

    def update(self, display, sprites):
        self._check_collide_with_bullet(sprites)
        self._check_die(sprites)
        self._move()
        self._shot(sprites)
        self._health_bar(display)

    def _check_die(self, sprites):
        if self._current_health == 0:
            sprites.player.sprites()[0].set_score(self._score)
            self.kill()

    def _check_collide_with_bullet(self, sprites):
        if pygame.sprite.spritecollide(self, sprites.player_bullets, False):
            self._current_health -= sprites.player_bullets.sprites()[-1].get_damage()
            pygame.sprite.spritecollide(self, sprites.player_bullets, True)

    def _shot(self, sprites):
        n = random.random()
        if n >= 0.996:
            sprites.create_enemy_bullet(self._pos, self._rotate_bullet(sprites), self._bullet_size, self._damage)

    def _rotate_bullet(self, sprites):
        direction = sprites.player.sprites()[0].get_pos() - self._pos
        radius, angle = direction.as_polar()
        correction_angle = 90
        rotate_coef = -angle - correction_angle
        return rotate_coef

    def _move(self):
        value_y = self._speed * math.cos(math.radians(self._rotate_coef))
        value_x = self._speed * math.sin(math.radians(self._rotate_coef))
        if not (self._pos.x + value_x > SCREEN_WIDTH - self._width // 2 or self._pos.x + value_x < self._width // 2):
            self._pos.x += value_x
        else:
            self._rotate_coef += random.uniform(20, 40)
        if not (self._pos.y + value_y > SCREEN_HEIGHT - self._height // 2 or self._pos.y + value_y < self._height // 2):
            self._pos.y += value_y
        else:
            self._rotate_coef += random.uniform(20, 40)

        self.rect = self.image.get_rect(center=self._pos)
