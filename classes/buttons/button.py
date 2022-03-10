import pygame


class Button:
    def __init__(self, x, y, image, scale):
        self._image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self._rect = self._image.get_rect(center=(x, y))
        self._clicked = False

    def draw(self, display):
        display.blit(self._image, (self._rect.x, self._rect.y))

    def update(self):
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self._clicked:
                self._clicked = True

        return self._clicked
