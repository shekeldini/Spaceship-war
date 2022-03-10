import random
import pygame
from classes.buttons.button import Button
from load_images import background, new_game_img
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from classes.sprites.sprites import Sprites


class Game:
    def __init__(self):
        self._sprites = Sprites()
        self._display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()
        self._run = True
        self._max_score = 0
        self._my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self._game_over_font = pygame.font.SysFont('Comic Sans MS', 50)
        self._new_game_btn = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 300, new_game_img, 0.5)

    def play(self):
        self._new_game()
        while self._run:
            self._clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._run = False

            if not self._sprites.check_alive_hero():
                if self._max_score < self._sprites.get_hero_score():
                    self._max_score = self._sprites.get_hero_score()

                self._draw_end(self._max_score, self._sprites.get_hero_score())

                if self._new_game_btn.check_click():
                    self._new_game()
                    self._new_game_btn.clicked = False

            else:
                if len(self._sprites.enemy.sprites()) < 6:
                    self._sprites.create_ufo()
                if self._sprites.get_hero_score() >= 20:
                    if not self._sprites.has_boss():
                        self._sprites.create_boss()
                if random.random() > 0.995 and not self._sprites.has_first_aid_kit():
                    self._sprites.create_first_aid_kit()
                self._draw_window()

    def _new_game(self):
        self._sprites.clear_sprites()
        self._sprites.create_player()

    def get_display(self):
        return self._display

    def get_sprites(self):
        return self._sprites

    def _draw_end(self, max_score, current_score):

        text = self._game_over_font.render("Game Over", True, (255, 255, 255))
        self._display.blit(text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 100))

        max_score_text = self._my_font.render("Max Score: " + str(max_score), True, (255, 255, 255))
        self._display.blit(max_score_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 165))

        current_score_text = self._my_font.render("Your Score: " + str(current_score), True, (255, 255, 255))
        self._display.blit(current_score_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 205))

        self._new_game_btn.update()
        self._new_game_btn.draw(self._display)
        pygame.display.update()

    def _blit_health(self):
        text = self._my_font.render("Health: " + str(self._sprites.get_hero_health()), False, (255, 255, 255))
        self._display.blit(text, (SCREEN_WIDTH - 165, 20))

    def _blit_score(self):
        text = self._my_font.render("Score: " + str(self._sprites.get_hero_score()), False, (255, 255, 255))
        self._display.blit(text, (20, 20))

    def _draw_window(self):
        self._display.fill((30, 30, 30))
        self._display.blit(background, (0, 0))

        self._sprites.player.update(self._display, self._sprites)
        self._sprites.player_bullets.update()

        self._sprites.enemy.update(self._display, self._sprites)
        self._sprites.enemy_bullets.update()

        self._sprites.buffs.update(self._sprites)

        self._sprites.player.draw(self._display)
        self._sprites.player_bullets.draw(self._display)

        self._sprites.enemy.draw(self._display)
        self._sprites.enemy_bullets.draw(self._display)

        self._sprites.buffs.draw(self._display)
        self._blit_health()
        self._blit_score()

        pygame.display.update()
