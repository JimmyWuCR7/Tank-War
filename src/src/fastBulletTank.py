## @file fastBulletTank.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Fast Bullet Tank module.
#  @date 03/24/2020

import pygame
import myTank
import bullet

imagePath = "../image/FastBulletTank.png"


## @brief Fast Bullet Tank,
#  @details This class sets up fast bullet tank's properties include operations
#  for the tank. This class is able to initialize itself and create the second
#  bullet for the tank
class fastBulletTank(myTank.MyTank):

    ## @brief Constructor for fastBulletTank.
    #  @details Constructor initialize the fast bullet tank, create the second
    #  bullet and set default value for the tank's ID, it also load the image
    #  for the fast bullet tank.
    #  @param coordinate represents the position of the tank.
    def __init__(self, coordinate):
        super().__init__(coordinate)
        self.bullet2 = bullet.Bullet()
        self.bullet.setBulletSpeed(10)
        self.bullet2.setBulletSpeed(8)
        self.ID = 3

        self.tank = pygame.image.load(imagePath).convert_alpha()
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))

        self.rect = self.tank_R0.get_rect()
        self.rect.left = 3 + 24 * coordinate.x
        self.rect.top = 3 + 24 * coordinate.y

    ## @brief Activate the second bullte for the tank.
    def doubleBullet(self):
        self.bullet.setBulletLife(True)
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

        if self.level == 1:
            self.bullet.setBulletSpeed(20)
            self.bullet.setBulletStrong(False)
        if self.level == 2:
            self.bullet.setBulletSpeed(20)
            self.bullet.setBulletStrong(True)
        if self.level == 3:
            self.bullet.setBulletSpeed(48)
            self.bullet.setBulletStrong(True)

        self.bullet2.setBulletLife(True)
        self.bullet2.changeImage(self.dir_x, self.dir_y)

        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet2.rect.left = self.rect.left + 20
            self.bullet2.rect.bottom = self.rect.top + 1
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet2.rect.left = self.rect.left + 20
            self.bullet2.rect.top = self.rect.bottom - 1
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet2.rect.right = self.rect.left - 1
            self.bullet2.rect.top = self.rect.top + 20
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet2.rect.left = self.rect.right + 1
            self.bullet2.rect.top = self.rect.top + 20

        if self.level == 1:
            self.bullet2.setBulletSpeed(20)
            self.bullet2.setBulletStrong(False)
        if self.level == 2:
            self.bullet2.setBulletSpeed(20)
            self.bullet2.setBulletStrong(True)
        if self.level == 3:
            self.bullet2.setBulletSpeed(48)
            self.bullet2.setBulletStrong(True)
