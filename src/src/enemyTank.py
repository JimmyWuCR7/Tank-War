## @file bullet.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Enemy Tank Module
#  @date 03/24/2020

import pygame
import random
import bullet


## @brief EnemeyTank.
#  @details This class sets up enemy tank's properties include operations for
#  the tank. This class is able to initialize itself and make the enemytank
#  shoot and move.
class EnemyTank(pygame.sprite.Sprite):
    ## @brief Constructor for EnemyTank.
    #  @details Constructor initialize the EnemyTank, sets the default
    #  value for falsh, times, kind and loads different images for
    #  different kinds of tanks. The constructor also sets the value
    #  for speed, direction, and the enemy tank's bullet.
    def __init__(self, x=None, kind=None, isred=None, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.flash = False
        self.times = 90
        self.kind = kind

        # Random generate type of enemy tanks
        if not kind:
            self.kind = random.choice([1, 2, 3, 4])

        if self.kind == 1:
            self.enemy_x_0 = pygame.image.load("../image/enemy_1_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load("../image/enemy_1_3.png").convert_alpha()
        if self.kind == 2:
            self.enemy_x_0 = pygame.image.load("../image/enemy_2_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load("../image/enemy_2_3.png").convert_alpha()
        if self.kind == 3:
            self.enemy_x_0 = pygame.image.load("../image/enemy_3_1.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load("../image/enemy_3_0.png").convert_alpha()
        if self.kind == 4:
            self.enemy_x_0 = pygame.image.load("../image/enemy_4_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load("../image/enemy_4_3.png").convert_alpha()
        self.enemy_3_0 = pygame.image.load("../image/enemy_3_0.png").convert_alpha()
        self.enemy_3_2 = pygame.image.load("../image/enemy_3_2.png").convert_alpha()

        # Set up tanks with red color
        self.isred = isred
        if not None:
            self.isred = random.choice((True, False, False, False, False))
        if self.isred:
            self.tank = self.enemy_x_3
        else:
            self.tank = self.enemy_x_0

        # Set up x coordinate of generating enemy tanks
        self.x = x
        if not self.x:
            self.x = random.choice([1, 2, 3])
        self.x -= 1
        # Set up tank information
        self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.rect = self.tank_R0.get_rect()
        self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 3 + y * 24
        self.speed = 1
        self.dir_x, self.dir_y = 0, 1
        self.life = 1
        self.bulletNotCooling = True
        self.bullet = bullet.Bullet()
        self.dirChange = False

        if self.kind == 2:
            self.speed = 3
        if self.kind == 3:
            self.life = 3

    ## @brief Make the enemy tank shoot, load the bullet image depending on the
    #  direction.
    def shoot(self):
        self.bullet.life = True
        self.bullet.changeImage(self.dir_x, self.dir_y)

        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top + 1
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom - 1
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet.rect.left = self.rect.right + 1
            self.bullet.rect.top = self.rect.top + 20

    ## @brief Make the enemy tank move and load the subsurfaces of the tank during
    #  moving.
    #  @param tankGroup The sprite group in pygame for the tanks.
    #  @param brickGroup The sprite group in pygame for the brick walls.
    #  @param ironGroup The sprite group in pygame for the iron walls.
    def move(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * self.dir_x, self.speed * self.dir_y)

        # Move strategy of enemy tanks
        if self.dir_x == 0 and self.dir_y == -1:
            self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        elif self.dir_x == 0 and self.dir_y == 1:
            self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        elif self.dir_x == -1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        elif self.dir_x == 1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))

        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))

        # Collide avoid
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None) \
            or pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.dir_x, self.speed * -self.dir_y)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
