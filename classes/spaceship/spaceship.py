import pygame
from pygame.math import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image, pos, size):
        super().__init__()
        self._width, self._height = size
        self._rotate_coef = None
        self.image = pygame.transform.scale(image.convert_alpha(), (self._width, self._height))
        self._orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self._pos = Vector2(pos)
        self._speed = 5

        self._current_health = 100
        self._max_health = 100
        self._health_bar_length = 100
        self._health_ratio = self._max_health / self._health_bar_length

        self._alive = True
        self._score = 0
        self._bullet_size = 10, 40

    def _move(self, sprites):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self._pos.y - self._speed > self._height // 2:
            self._pos.y -= self._speed
        if keys[pygame.K_a] and self._pos.x - self._speed > self._width // 2:
            self._pos.x -= self._speed
        if keys[pygame.K_s] and self._pos.y + self._speed < SCREEN_HEIGHT - self._height // 2:
            self._pos.y += self._speed
        if keys[pygame.K_d] and self._pos.x + self._speed < SCREEN_WIDTH - self._width // 2:
            self._pos.x += self._speed
        if pygame.mouse.get_pressed()[0]:
            self._create_bullet(sprites)

    def _create_bullet(self, sprites):
        sprites.create_player_bullet(self._pos, self._rotate_coef, self._bullet_size)

    def update(self, display, sprites):
        self._check_collide_with_enemy_bullet(sprites)
        self._check_die()
        self._rotate()
        self._move(sprites)
        self._health_bar(display)

    def _health_bar(self, display):
        health_bar_width = int(self._current_health / self._health_ratio)
        r_x = self.rect.x
        r_y = self.rect.y
        health_bar = pygame.Rect(r_x - 10, r_y - 50, health_bar_width, 20)
        pygame.draw.rect(display, (255, 0, 0), (r_x - 10, r_y - 50, self._health_bar_length, 20))
        pygame.draw.rect(display, (0, 255, 0), health_bar)
        pygame.draw.rect(display, (255, 255, 255), (r_x - 10, r_y - 50, self._health_bar_length, 20), 4)

    def _check_die(self):
        if self._current_health <= 0:
            self._alive = False

    def _check_collide_with_enemy_bullet(self, sprites):
        if pygame.sprite.spritecollide(self, sprites.enemy_bullets, False):
            self._current_health -= sprites.enemy_bullets.sprites()[-1].get_damage()
            if self._current_health < 0:
                self._current_health = 0
            pygame.sprite.spritecollide(self, sprites.enemy_bullets, True)

    def get_pos(self):
        return self._pos

    def get_health(self):
        return self._current_health

    def get_score(self):
        return self._score

    def set_score(self, value):
        self._score += value

    def is_alive(self):
        return self._alive

    def _rotate(self):
        direction = pygame.mouse.get_pos() - self._pos
        radius, angle = direction.as_polar()
        correction_angle = 90
        self._rotate_coef = -angle - correction_angle
        self.image = pygame.transform.rotate(self._orig_image, self._rotate_coef)
        self.rect = self.image.get_rect(center=self._pos)

    def get_heal(self, value):
        self._current_health += value
        if self._current_health > self._max_health:
            self._current_health = self._max_health
