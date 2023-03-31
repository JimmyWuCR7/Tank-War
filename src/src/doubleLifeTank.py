## @file doubleLifeTank.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Double Life Tank module.
#  @date 03/23/2020

import pygame
import myTank

imagePath = "../image/DoubleLifeTank.png"


## @brief Double Life Tank.
#  @details This class sets up double life tank's properties include operations
#  for the tank. This class is able to initialize itself, start and
#   end the skill bullet proof and return the value of bulletProof.
class doubleLifeTank(myTank.MyTank):
    ## @brief Constructor for doubleLifeTank.
    #  @details Constructor initialize the double life tank, load the images for
    #  it and set the default value for life, bulletProof, ID, and position.
    #  @param coordinate represents the position of the tank.
    def __init__(self, coordinate):
        super().__init__(coordinate)
        self.life = 2
        self.bulletProof = False
        self.ID = 1

        self.tank = pygame.image.load(imagePath).convert_alpha()
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))

        self.rect = self.tank_R0.get_rect()
        self.rect.left = 3 + 24 * coordinate.x
        self.rect.top = 3 + 24 * coordinate.y

    ## @brief Change the value of bulletproof to True
    #  which means start the skill.
    def bulletproof_start(self):
        self.bulletProof = True

    ## @brief Change the value of bulletproof to False
    #  which means end the skill.
    def bulletproof_end(self):
        self.bulletProof = False

    ## @brief Accessor for bulletProof.
    #  @return bulletProof represents the
    #  condition of the skill bullet proof.
    def getBulletProof(self):
        return self.bulletProof
