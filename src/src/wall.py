## @file wall.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Brick class, Iron class, and Home class.
#  @date 03/23/2020

import pygame

brickImage = "../image/brick.png"
ironImage = "../image/iron.png"
homeImage = "../image/home.png"


## @brief Brick.
#  @details This class sets up the properties of the brick wall.
#  This class constructs a brick wall and sets the image path so
#  that the image can be loaded on the screen. Also, the coordinate
#  of the brick can be stored in the self.rect
class Brick(pygame.sprite.Sprite):
    ## @brief Constructor for Brick.
    #  @details Constructor initialize the brick wall, set the path
    #  for brick Image and stored in the brick objects. Also a self.rect
    #  is defined and can be used to store the coordinate of the brick wall.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(brickImage)
        self.rect = self.image.get_rect()


## @brief Iron.
#  @details This class sets up the properties of the iron wall.
#  This class constructs a iron wall and sets the image path so
#  that the image can be loaded on the screen. Also, the coordinate
#  of the iron can be stored in the self.rect
class Iron(pygame.sprite.Sprite):
    ## @brief Constructor for Iron.
    #  @details Constructor initialize the iron wall, set the path
    #  for iron Image and stored in the iron objects. Also a self.rect
    #  is defined and can be used to store the coordinate of the iron wall.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(ironImage)
        self.rect = self.image.get_rect()


## @brief Home.
#  @details This class sets up the properties of the Home Base.
#  This class constructs a iron wall and sets the image path so
#  that the image can be loaded on the screen. The home ID is also
#  identified in order to verify different home in PVP mode. The
#  coordinate of the home base can be stored in the self.rect
class Home(pygame.sprite.Sprite):
    ## @brief Constructor for Home.
    #  @details Constructor initialize the home base, set the path
    #  for home Image and stored in the iron objects. Also a home ID
    #  is defined and saved in the home object. Moreover, The self.rect
    #  is defined and can be used to store the coordinate of the home base.
    def __init__(self, homeID=0):
        pygame.sprite.Sprite.__init__(self)
        self.homeID = homeID
        self.image = pygame.image.load(homeImage)
        self.rect = self.image.get_rect()
