import math
import pygame
import random
from pygame.math import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos, size, speed, damage, health, score):
        super().__init__()
        self.width, self.height = size
        self.image = pygame.transform.scale(self.choice_image(image).convert_alpha(),
                                            (self.width, self.height))
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.rotate_coef = random.uniform(-180, 180)
        self.current_health = health
        self.max_health = health
        self.health_bar_length = 100
        self.health_ratio = self.max_health / self.health_bar_length
        self.speed = speed
        self.damage = damage
        self.score = score
        self.bullet_size = 2, 20

    @staticmethod
    def choice_image(images):
        if isinstance(images, list):
            return random.choice(images)
        return images

    def health_bar(self, display):
        health_bar_width = int(self.current_health / self.health_ratio)
        r_x = self.rect.x
        r_y = self.rect.y
        health_bar = pygame.Rect(r_x - 10, r_y - 50, health_bar_width, 20)
        pygame.draw.rect(display, (255, 0, 0), (r_x - 10, r_y - 50, self.health_bar_length, 20))
        pygame.draw.rect(display, (0, 255, 0), health_bar)
        pygame.draw.rect(display, (255, 255, 255), (r_x - 10, r_y - 50, self.health_bar_length, 20), 4)

    def update(self, display, sprites):
        self.check_collide_with_bullet(sprites)
        self.check_die(sprites)
        self.move()
        self.shot(sprites)
        self.health_bar(display)

    def check_die(self, sprites):
        if self.current_health == 0:
            sprites.player.sprites()[0].set_score(self.score)
            self.kill()

    def check_collide_with_bullet(self, sprites):
        if pygame.sprite.spritecollide(self, sprites.player_bullets, False):
            self.current_health -= sprites.player_bullets.sprites()[-1].get_damage()
            pygame.sprite.spritecollide(self, sprites.player_bullets, True)

    def shot(self, sprites):
        n = random.random()
        if n >= 0.996:
            sprites.create_enemy_bullet(self.pos, self.rotate_bullet(sprites), self.bullet_size, self.damage)

    def rotate_bullet(self, sprites):
        direction = sprites.player.sprites()[0].get_pos() - self.pos
        radius, angle = direction.as_polar()
        correction_angle = 90
        rotate_coef = -angle - correction_angle
        return rotate_coef

    def move(self):
        value_y = self.speed * math.cos(math.radians(self.rotate_coef))
        value_x = self.speed * math.sin(math.radians(self.rotate_coef))
        if not (self.pos.x + value_x > SCREEN_WIDTH - self.width // 2 or self.pos.x + value_x < self.width // 2):
            self.pos.x += value_x
        else:
            self.rotate_coef += random.uniform(20, 40)
        if not (self.pos.y + value_y > SCREEN_HEIGHT - self.height // 2 or self.pos.y + value_y < self.height // 2):
            self.pos.y += value_y
        else:
            self.rotate_coef += random.uniform(20, 40)

        self.rect = self.image.get_rect(center=self.pos)
