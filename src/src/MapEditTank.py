## @file MapEditTank.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief MapEditTank class module.
#  @date 03/23/2020

import pygame
import bullet
from Map import CoordinateT

imagePath = "../image/HighSpeedTank.png"


## @brief MapEditTank.
#  @details This class sets up the properties of the map edit tank objects.
#  The tank speed, bullet, coordinates, and directions will be defined
#  after creating a map editing tank. Functions like moving the tank
#  and shooting can also be achieved in the map editing mode.
class MapEditTank(pygame.sprite.Sprite):
    ## @brief Constructor for map editing tank.
    #  @details Constructor initialize the map editing tank by
    #  initializing the life, level, speed, bullet, coordinate,
    #  and direction of the tank.
    def __init__(self, coordinate):
        pygame.sprite.Sprite.__init__(self)

        self.life = 1
        self.level = 0
        self.speed = 3

        self.bullet = bullet.Bullet()
        self.bulletNotCooling = True

        self.tank = pygame.image.load(imagePath).convert_alpha()
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))

        self.rect = self.tank_R0.get_rect()
        self.rect.left = 3 + 24 * coordinate.x
        self.rect.top = 3 + 24 * coordinate.y

        self.dir_x, self.dir_y = 0, -1

    ## @brief shooting.
    #  @details Shooting function allows the map editing tank
    #  to shoot a bullet in the map editing mode and break
    #  the brick and iron walls.
    def shoot(self):
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
            self.bullet.speed = 16
            self.bullet.strong = False
        if self.level == 2:
            self.bullet.speed = 16
            self.bullet.strong = True

    ## @brief move up.
    #  @details Moveup function allows the tank to move up
    #  in the map editing mode without colliding with other
    #  sprites.
    def moveUp(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))

        self.dir_x, self.dir_y = 0, -1
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True

        return False

    ## @brief move down.
    #  @details Moveup function allows the tank to move down
    #  in the map editing mode without colliding with other
    #  sprites.
    def moveDown(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.dir_x, self.dir_y = 0, 1
        if self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True

        return False

    ## @brief move left.
    #  @details Moveup function allows the tank to move left
    #  in the map editing mode without colliding with other
    #  sprites.
    def moveLeft(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        self.dir_x, self.dir_y = -1, 0
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True

        return False

    ## @brief move right.
    #  @details Moveup function allows the tank to move right
    #  in the map editing mode without colliding with other
    #  sprites.
    def moveRight(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))
        self.dir_x, self.dir_y = 1, 0
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True

        return False
