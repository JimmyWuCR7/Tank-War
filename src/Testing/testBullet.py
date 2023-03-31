## @file bulletTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Bullet Test Module
#  @date 04/04/2020

import sys
sys.path.append("../src")
import unittest
import pygame
from bullet import Bullet


## @brief Unit test for bullet module
#  @detail This class do the unit test cases for part of the functions in
#  the bullet module, and it passes once all the outputs are the same
#  as the expected ones.
class BulletTest(unittest.TestCase):

    ## @brief Test if the setBulletSpeed function in Bullet module works
    #  properly.
    def test_set_bullet_speed(self):
        bullet = Bullet()
        bullet.setBulletSpeed(6)
        self.assertEqual(bullet.speed, 6, "test_set_bullet_speed")
        bullet.setBulletSpeed(0)
        self.assertEqual(bullet.speed, 0, "test_set_bullet_speed")

    ## @brief Test if the setBulletLife function in Bullet module works
    #  properly.
    def test_set_bullet_life(self):
        bullet = Bullet()
        bullet.setBulletLife(True)
        self.assertEqual(bullet.life, True, "test_set_bullet_life")
        bullet.setBulletLife(False)
        self.assertEqual(bullet.life, False, "test_set_bullet_life")

    ## @brief Test if the setBulletStrong function in Bullet module works
    #  properly.
    def test_set_bullet_strong(self):
        bullet = Bullet()
        bullet.setBulletStrong(True)
        self.assertEqual(bullet.strong, True, "test_set_bullet_strong")
        bullet.setBulletStrong(False)
        self.assertEqual(bullet.strong, False, "test_set_bullet_strong")


# Run the tests
if __name__ == '__main__':
    unittest.main()
