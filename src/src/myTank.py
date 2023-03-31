## @file myTank.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief My Tank module.
#  @date 03/24/2020

import pygame
import bullet

imagePath = "../image/HighSpeedTank.png"


## @brief My Tank.
#  @details This class sets up player's tank's properties include operations
#  for the tank. This class is able to initialize itself, make the tank shoot,
#  move, and change the level of the tank.
class MyTank(pygame.sprite.Sprite):
    ## @brief Constructor for myTank.
    #  @details Constructor initialize the player's tank, load the images for
    #  it and set the default value for life, level, speed, position and direction.
    #  @param coordinate represents the position of the tank.
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

    ## @brief Make the players' tank shoot, set the bullet life to True and load
    #   the bullet image depending on the direction.
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

    ## @brief Increase the tank's level by 1 when it was less than 2.
    def levelUp(self):
        if self.level < 2:
            self.level += 1

    ## @brief Decrease the tank's level by 1 when it was higher than 0 and set
    #  the property for the corresponding level.
    def levelDown(self):
        if self.level > 0:
            self.level -= 1
        if self.level == 0:
            self.bullet.speed = 6
            self.bullet.strong = False

    ## @brief Move the tank upward.
    #  @param tankGroup The sprite group in pygame for tanks.
    #  @param brickGroup The sprite group in pygame for brick walls.
    #  @param ironGroup The sprite group in pygame for iron walls.
    #  @return True means the tank is blocked by the walls or boundaries.
    #  @return False means the tank can move.
    def moveUp(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))

        self.dir_x, self.dir_y = 0, -1
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
                self.rect = self.rect.move(self.speed * 0, self.speed * 1)
                return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        return False

    ## @brief Move the tank downward.
    #  @param tankGroup The sprite group in pygame for tanks.
    #  @param brickGroup The sprite group in pygame for brick walls.
    #  @param ironGroup The sprite group in pygame for iron walls.
    #  @return True means the tank is blocked by the walls or boundaries.
    #  @return False means the tank can move.
    def moveDown(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.dir_x, self.dir_y = 0, 1
        if self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
                self.rect = self.rect.move(self.speed * 0, self.speed * -1)
                return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        return False

    ## @brief Move the tank to the left.
    #  @param tankGroup The sprite group in pygame for tanks.
    #  @param brickGroup The sprite group in pygame for brick walls.
    #  @param ironGroup The sprite group in pygame for iron walls.
    #  @return True means the tank is blocked by the walls or boundaries.
    #  @return False means the tank can move.
    def moveLeft(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        self.dir_x, self.dir_y = -1, 0
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
                self.rect = self.rect.move(self.speed * 1, self.speed * 0)
                return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        return False

    ## @brief Move the tank to the right.
    #  @param tankGroup The sprite group in pygame for tanks.
    #  @param brickGroup The sprite group in pygame for brick walls.
    #  @param ironGroup The sprite group in pygame for iron walls.
    #  @return True means the tank is blocked by the walls or boundaries.
    #  @return False means the tank can move.
    def moveRight(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))
        self.dir_x, self.dir_y = 1, 0
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
            or pygame.sprite.spritecollide(self, ironGroup, False, None):
                self.rect = self.rect.move(self.speed * -1, self.speed * 0)
                return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        return False
