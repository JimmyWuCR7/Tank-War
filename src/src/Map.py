## @file Map.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Map class, PVEMap class, PVPMap class.
#  @date 03/23/2020

import pygame
from wall import Brick, Iron, Home
from typing import NamedTuple


## @brief Map Constant
#  @details EDGE_LENGTH represents the length of the edge in pixel.
#  GRID_LENGTH represents the length of one grid of the map in pixel.
EDGE_LENGTH = 3
GRID_LENGTH = 24


## @brief Map.
#  @details This class sets up the properties of the map objects.
#  The map object contains brick walls, iron walls, and home bases.
#  They can be saved in the corresponding group. After constructing
#  the map object, new brick, iron and home base can be added into
#  this map object. The properties of map can be loaded from a
#  local text file, and the changed version can also be saved in the
#  same format in a new local file.
class Map():
    ## @brief Constructor for Map.
    #  @details Constructor initialize the map by initializing the
    #  brick group, iron group, and home group.
    def __init__(self):
        self.brickGroup = pygame.sprite.Group()
        self.ironGroup = pygame.sprite.Group()
        self.homeGroup = pygame.sprite.Group()

    ## @brief add brick to the map object.
    #  @details Create a brick object using the input coordinate
    #  and add it into the brick group of the map object.
    def addBrick(self, coordinate):
        brick = Brick()
        brick.rect.left = EDGE_LENGTH + coordinate.x * GRID_LENGTH
        brick.rect.top = EDGE_LENGTH + coordinate.y * GRID_LENGTH
        self.brickGroup.add(brick)

    ## @brief add iron to the map object.
    #  @details Create a iron object using the input coordinate
    #  and add it into the iron group of the map object.
    def addIron(self, coordinate):
        iron = Iron()
        iron.rect.left = EDGE_LENGTH + coordinate.x * GRID_LENGTH
        iron.rect.top = EDGE_LENGTH + coordinate.y * GRID_LENGTH
        self.ironGroup.add(iron)

    ## @brief add home base to the map object.
    #  @details Create a home object using the input coordinate
    #  and home ID and add it into the home group of the map object.
    def addHome(self, coordinate, homeID=0):
        home = Home(homeID)
        home.rect.left = EDGE_LENGTH + coordinate.x * GRID_LENGTH
        home.rect.top = EDGE_LENGTH + coordinate.y * GRID_LENGTH
        self.homeGroup.add(home)

    ## @brief load the map.
    #  @details Load the map based on the given file path and
    #  add all the brick and iron wall saved in that file into
    #  the map object.
    def loadBrickIron(self, path):
        content = open(path, mode='r')
        lines = content.readlines()
        number_brick = int(lines[-EDGE_LENGTH])
        number_iron = int(lines[-1])

        for i in range(1, number_brick+1):
            xy = lines[i].split()
            coordinate = CoordinateT(int(xy[0]), int(xy[1]))
            self.addBrick(coordinate)

        for i in range(number_brick+2, number_brick+2+number_iron):
            xy = lines[i].split()
            coordinate = CoordinateT(int(xy[0]), int(xy[1]))
            self.addIron(coordinate)

    ## @brief save the map.
    #  @details Save the map to the given file path and
    #  add all the brick and iron wall saved in the map object
    #  into the corresponding file.
    def saveMap(self, path):
        content = open(path, mode='w')
        brick_count = 0
        iron_count = 0

        content.write("Brick:\n")
        for each in self.brickGroup:
            x = (each.rect.left-EDGE_LENGTH) // GRID_LENGTH
            y = (each.rect.top-EDGE_LENGTH) // GRID_LENGTH
            content.write(str(x)+" "+str(y)+"\n")
            brick_count += 1

        content.write("Iron:\n")
        for each in self.ironGroup:
            x = (each.rect.left-EDGE_LENGTH) // GRID_LENGTH
            y = (each.rect.top-EDGE_LENGTH) // GRID_LENGTH
            content.write(str(x)+" "+str(y)+"\n")
            iron_count += 1

        content.write("Number of Brick:\n" + str(brick_count) + "\n" + \
            "Number of Iron:\n" + str(iron_count))
        content.close()


## @brief PVE Map.
#  @details PVEMap is a subclass of Map class. PVEMap can
#  directly use the constructor of Map class and read from
#  the local file to add brick and irons into the corresponding
#  group. The corrdinate for PVE home base can also be defined
#  and add into the PVEMap object.
class PVEMap(Map):
    ## @brief Constructor for PVE map.
    #  @details Constructor initialize the PVE map by initializing the
    #  brick group, iron group, and home group.
    def __init__(self):
        super().__init__()

    ## @brief load PVE map.
    #  @details Load the PVE map from the give path, read the saved
    #  brick and iron walls and add into the corresponding group.
    #  Initialize a home base and add it into the home group.
    def loadPVEMap(self, path):
        super().loadBrickIron(path)

        coordinate = CoordinateT(12, 24)
        super().addHome(coordinate)


## @brief PVP Map.
#  @details PVPMap is a subclass of Map class. PVPMap can
#  directly use the constructor of Map class and read from
#  the local file to add brick and irons into the corresponding
#  group. The corrdinate for PVP home bases can also be defined
#  and add into the PVPMap object.
class PVPMap(Map):
    ## @brief Constructor for PVP map.
    #  @details Constructor initialize the PVP map by initializing the
    #  brick group, iron group, and home group.
    def __init__(self):
        super().__init__()

    ## @brief load PVP map.
    #  @details Load the PVP map from the give path, read the saved
    #  brick and iron walls and add into the corresponding group.
    #  Initialize two home bases and add them into the home group.
    def loadPVPMap(self, path):
        super().loadBrickIron(path)

        coordinate = CoordinateT(0, 12)
        super().addHome(coordinate, 1)

        coordinate = CoordinateT(24, 12)
        super().addHome(coordinate, 2)


## @brief position coordination format.
#  @details This class includes position information and set up its format.
class CoordinateT(NamedTuple):
    x: int
    y: int
