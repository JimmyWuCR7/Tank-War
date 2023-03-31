## @file food.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Food module.
#  @date 03/24/2020

import pygame
import random


## @brief The food which can help the players.
#  @details This class sets up different kinds of food and define the way of
#  making the food appear.
class Food(pygame.sprite.Sprite):
    ## @brief Constructor for food.
    #  @details Constructor initialize the food, load images for different
    #  kinds of food and set a random value for kind.
    def __init__(self):

        self.food_boom = \
            pygame.image.load("../image/food_boom.png").convert_alpha()
        self.food_clock = \
            pygame.image.load("../image/food_clock.png").convert_alpha()
        self.food_gun = \
            pygame.image.load("../image/food_gun.png").convert_alpha()
        self.food_iron = \
            pygame.image.load("../image/food_iron.png").convert_alpha()
        self.food_star = \
            pygame.image.load("../image/food_star.png").convert_alpha()
        self.kind = \
            random.choice([1, 2, 3, 4, 5])
        if self.kind == 1:
            self.image = self.food_boom
        elif self.kind == 2:
            self.image = self.food_clock
        elif self.kind == 3:
            self.image = self.food_gun
        elif self.kind == 4:
            self.image = self.food_iron
        elif self.kind == 5:
            self.image = self.food_star

        self.rect = self.image.get_rect()
        self.rect.left = self.rect.top = random.randint(100, 500)

        self.life = False

    ## @brief Change the food's life to True and set the position and image for
    #  it.
    def change(self):
        self.kind = random.choice([1, 2, 3, 4, 5])
        if self.kind == 1:
            self.image = self.food_boom
        elif self.kind == 2:
            self.image = self.food_clock
        elif self.kind == 3:
            self.image = self.food_gun
        elif self.kind == 4:
            self.image = self.food_iron
        elif self.kind == 5:
            self.image = self.food_star

        self.rect.left = self.rect.top = random.randint(100, 500)
        self.life = True
