import pygame
from pygame.math import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT



class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image, pos, size):
        super().__init__()
        self.width, self.height = size
        self.rotate_coef = None
        self.image = pygame.transform.scale(image.convert_alpha(),
                                            (self.width, self.height))
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.speed = 5

        self.current_health = 100
        self.max_health = 100
        self.health_bar_length = 100
        self.health_ratio = self.max_health / self.health_bar_length

        self.alive = True
        self.score = 0
        self.bullet_size = 10, 40

    def move(self, sprites):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pos.y - self.speed > self.height // 2:
            self.pos.y -= self.speed
        if keys[pygame.K_a] and self.pos.x - self.speed > self.width // 2:
            self.pos.x -= self.speed
        if keys[pygame.K_s] and self.pos.y + self.speed < SCREEN_HEIGHT - self.height // 2:
            self.pos.y += self.speed
        if keys[pygame.K_d] and self.pos.x + self.speed < SCREEN_WIDTH - self.width // 2:
            self.pos.x += self.speed
        if pygame.mouse.get_pressed()[0]:
            self.create_bullet(sprites)

    def create_bullet(self, sprites):
        sprites.create_player_bullet(self.pos, self.rotate_coef, self.bullet_size)

    def update(self, display, sprites):
        self.check_collide_with_enemy_bullet(sprites)
        self.check_die()
        self.rotate()
        self.move(sprites)
        self.health_bar(display)

    def health_bar(self, display):
        health_bar_width = int(self.current_health / self.health_ratio)
        r_x = self.rect.x
        r_y = self.rect.y
        health_bar = pygame.Rect(r_x - 10, r_y - 50, health_bar_width, 20)
        pygame.draw.rect(display, (255, 0, 0), (r_x - 10, r_y - 50, self.health_bar_length, 20))
        pygame.draw.rect(display, (0, 255, 0), health_bar)
        pygame.draw.rect(display, (255, 255, 255), (r_x - 10, r_y - 50, self.health_bar_length, 20), 4)

    def check_die(self):
        if self.current_health <= 0:
            self.alive = False

    def check_collide_with_enemy_bullet(self, sprites):
        if pygame.sprite.spritecollide(self, sprites.enemy_bullets, False):
            self.current_health -= sprites.enemy_bullets.sprites()[-1].get_damage()
            if self.current_health < 0:
                self.current_health = 0
            pygame.sprite.spritecollide(self, sprites.enemy_bullets, True)

    def get_pos(self):
        return self.pos

    def get_health(self):
        return self.current_health

    def get_score(self):
        return self.score

    def set_score(self, value):
        self.score += value

    def is_alive(self):
        return self.alive

    def rotate(self):
        direction = pygame.mouse.get_pos() - self.pos
        radius, angle = direction.as_polar()
        correction_angle = 90
        self.rotate_coef = -angle - correction_angle
        self.image = pygame.transform.rotate(self.orig_image, self.rotate_coef)
        self.rect = self.image.get_rect(center=self.pos)

    def get_heal(self, value):
        self.current_health += value
        if self.current_health > self.max_health:
            self.current_health = self.max_health
