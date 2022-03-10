from classes.bullets.bullet import Bullet


class PlayerBullet(Bullet):
    def __init__(self, image, pos, rotate_coef, size):
        self.size = size
        self.speed = 10
        self.damage = 2
        super().__init__(image, pos, rotate_coef, self.size, self.speed, self.damage)