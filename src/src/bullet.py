## @file bullet.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Bullet Class Module
#  @date 03/23/2020

import pygame
from Map import CoordinateT
## @brief bullet Constant
#  @details EDGE_LENGTH represents the length of the edge in pixel.
#  GRID_LENGTH represents the length of one grid of the map in pixel.
#  BOUNDARY_SIZE represents the size of the boundary of the map
EDGE_LENGTH = 3
GRID_LENGTH = 24
BOUNDARY_SIZE = 630


## @brief Bullet.
#  @details This class sets up Bullet's properties include operations for the
#  bullet. This class is able to initialize itself, set the bullet's speed,
#  life, and make it to be strong or not. This class can also load image for
#  the bullet depends on the direction and make the bullet move in that
#  direction.
class Bullet(pygame.sprite.Sprite):
    ## @brief Constructor for Bullet.
    #  @details Constructor initialize the bullet, loads the images for it in 4
    #  different directions, and sets the default value for dir_x, dir_y, speed
    #  ,life, strong, image, and its position.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
#       Bullet image import
        self.bullet_up = pygame.image.load("../image/bullet_up.png")
        self.bullet_down = pygame.image.load("../image/bullet_down.png")
        self.bullet_left = pygame.image.load("../image/bullet_left.png")
        self.bullet_right = pygame.image.load("../image/bullet_right.png")

        self.coordinate = CoordinateT(12, 24)
        self.dir_x, self.dir_y = 0, 0
        self.speed = 6
        self.life = False
        self.strong = False

        self.bullet = self.bullet_up
        self.rect = self.bullet.get_rect()
        self.rect.left, self.rect.right =\
            EDGE_LENGTH + self.coordinate.x * GRID_LENGTH,\
            EDGE_LENGTH + self.coordinate.y * GRID_LENGTH

    ## @brief Mutator for Bullet Speed.
    #  @param speed represents the speed of the bullet.
    def setBulletSpeed(self, speed):
        self.speed = speed

    ## @brief Mutator for Bullet Life.
    #  @param life represents the life of the bullet.
    def setBulletLife(self, life):
        self.life = life

    ## @brief Mutator for Bullet Strong.
    #  @param strong represents that the bullet is strong or not.
    def setBulletStrong(self, strong):
        self.strong = strong

    ## @brief Change the image for the bullet depends on its direction.
    #  @param dir_x represents the horizontal direction of the bullet.
    #  @param dir_y represents the vertical direction of the bullet.
    def changeImage(self, dir_x, dir_y):
        self.dir_x, self.dir_y = dir_x, dir_y
        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet = self.bullet_up
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet = self.bullet_down
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet = self.bullet_left
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet = self.bullet_right

        if self.dir_x == 0 and self.dir_y == -1:
            self.rect.left = self.rect.left + 20
            self.rect.bottom = self.rect.top + 1
        elif self.dir_x == 0 and self.dir_y == 1:
            self.rect.left = self.rect.left + 20
            self.rect.top = self.rect.bottom - 1
        elif self.dir_x == -1 and self.dir_y == 0:
            self.rect.right = self.rect.left - 1
            self.rect.top = self.rect.top + 20
        elif self.dir_x == 1 and self.dir_y == 0:
            self.rect.left = self.rect.right + 1
            self.rect.top = self.rect.top + 20

    ## @brief Move the bullet in its direction and make it disappear when it
    #  hits the boundaries of the map.
    def move(self):
        self.rect = self.rect.move(self.speed * self.dir_x,
                                   self.speed * self.dir_y)

        if self.rect.top < EDGE_LENGTH:
            self.life = False
        if self.rect.bottom > BOUNDARY_SIZE - EDGE_LENGTH:
            self.life = False
        if self.rect.left < 3:
            self.life = False
        if self.rect.right > BOUNDARY_SIZE - EDGE_LENGTH:
            self.life = False
