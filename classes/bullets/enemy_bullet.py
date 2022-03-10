from classes.bullets.bullet import Bullet


class EnemyBullet(Bullet):
    def __init__(self, image, pos, rotate_coef, size, damage):
        self.size = size
        self.speed = 5
        self.damage = damage
        super().__init__(image, pos, rotate_coef, self.size, self.speed, self.damage)