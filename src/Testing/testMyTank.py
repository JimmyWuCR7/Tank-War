## @file myTankTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief My Tank Test Module
#  @date 04/04/2020

import sys
sys.path.append("../src")
import unittest
import pygame
from myTank import MyTank
from Map import CoordinateT


## @brief Unit test for myTank module
#  @detail This class do the unit test cases for part of the functions in
#  the myTank module, and it passes once all the outputs are the same
#  as the expected ones.
class MyTankTest(unittest.TestCase):

    ## @brief Test if the shoot function in myTank module works properly.
    def test_mytank_shoot(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        mytank = MyTank(CoordinateT(8, 24))
        mytank.shoot()
        self.assertEqual(mytank.bullet.life, True, "test_mytank_shoot")
        pygame.quit()

    ## @brief Test if the levelUp function in myTank module works properly.
    def test_mytank_levelup(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        mytank = MyTank(CoordinateT(8, 24))
        mytank.level = 0
        mytank.levelUp()
        self.assertEqual(mytank.level, 1, "test_mytank_levelup")
        mytank.levelUp()
        self.assertEqual(mytank.level, 2, "test_mytank_levelup")
        mytank.levelUp()
        self.assertEqual(mytank.level, 2, "test_mytank_levelup")
        pygame.quit()

    ## @brief Test if the levelDown function in myTank module works properly.
    def test_mytank_leveldown(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        mytank = MyTank(CoordinateT(8, 24))
        mytank.level = 2
        mytank.levelDown()
        self.assertEqual(mytank.level, 1, "test_mytank_levelDown")
        mytank.levelDown()
        self.assertEqual(mytank.level, 0, "test_mytank_levelDown")
        mytank.levelDown()
        self.assertEqual(mytank.level, 0, "test_mytank_levelDown")
        pygame.quit()

## @brief Test if the moveUp function in myTank module works properly.
    def test_mytank_moveUp(self):
        resolution = 630, 630
        tankGroup= pygame.sprite.Group()
        brickGroup = pygame.sprite.Group()
        ironGroup = pygame.sprite.Group()
        pygame.display.set_mode(resolution)
        mytank = MyTank(CoordinateT(8, 24))
        mytank.moveUp(tankGroup, brickGroup, ironGroup)
        self.assertEqual(mytank.dir_x, 0, "test_mytank_moveUp")
        self.assertEqual(mytank.dir_y, -1, "test_mytank_moveUp")
        pygame.quit()

## @brief Test if the moveDown function in myTank module works properly.
    def test_mytank_moveDown(self):
        resolution = 630, 630
        tankGroup= pygame.sprite.Group()
        brickGroup = pygame.sprite.Group()
        ironGroup = pygame.sprite.Group()
        pygame.display.set_mode(resolution)
        mytank = MyTank(CoordinateT(8, 8))
        mytank.moveDown(tankGroup, brickGroup, ironGroup)
        self.assertEqual(mytank.dir_x, 0, "test_mytank_moveDown")
        self.assertEqual(mytank.dir_y, 1, "test_mytank_moveDown")
        pygame.quit()

## @brief Test if the moveLeft function in myTank module works properly.
    def test_mytank_moveLeft(self):
        resolution = 630, 630
        tankGroup= pygame.sprite.Group()
        brickGroup = pygame.sprite.Group()
        ironGroup = pygame.sprite.Group()
        pygame.display.set_mode(resolution)
        mytank = MyTank(CoordinateT(8, 24))
        mytank.moveLeft(tankGroup, brickGroup, ironGroup)
        self.assertEqual(mytank.dir_x, -1, "test_mytank_moveLeft")
        self.assertEqual(mytank.dir_y, 0, "test_mytank_moveLeft")
        pygame.quit()

## @brief Test if the moveRight function in myTank module works properly.
    def test_mytank_moveRight(self):
        resolution = 630, 630
        tankGroup= pygame.sprite.Group()
        brickGroup = pygame.sprite.Group()
        ironGroup = pygame.sprite.Group()
        pygame.display.set_mode(resolution)
        mytank = MyTank(CoordinateT(8, 24))
        mytank.moveRight(tankGroup, brickGroup, ironGroup)
        self.assertEqual(mytank.dir_x, 1, "test_mytank_moveRight")
        self.assertEqual(mytank.dir_y, 0, "test_mytank_moveRight")
        pygame.quit()

# Run the tests
if __name__ == '__main__':
    unittest.main()
