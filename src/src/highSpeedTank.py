## @file highSpeedTank.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief High Speed Tank module.
#  @date 03/24/2020

import pygame
import myTank

imagePath = "../image/HighSpeedTank.png"


## @brief High Spped Tank.
#  @details This class sets up high speed tank's properties include operations
#  for the tank. This class is able to initialize itself,
#  start and end the skill leap.
class highSpeedTank(myTank.MyTank):
    ## @brief Constructor for highSpeedTank.
    #  @details Constructor initialize the high speed tank, load the images for
    #  for it and set the default value for speed, ID, and position.
    #  @param coordinate represents the position of the tank.
    def __init__(self, coordinate):
        super().__init__(coordinate)
        self.speed = 3
        self.ID = 2

        self.tank = pygame.image.load(imagePath).convert_alpha()
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))

        self.rect = self.tank_R0.get_rect()
        self.rect.left = 3 + 24 * coordinate.x
        self.rect.top = 3 + 24 * coordinate.y

    ## @brief Activate the skill leap.

    def leap_start(self):
        self.speed += 3

    ## @brief End the skill leap.

    def leap_end(self):
        self.speed = 3
