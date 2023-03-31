## @file foodTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Food Test Module
#  @date 04/04/2020

import sys
sys.path.append("../src")
import unittest
import pygame
from food import Food


## @brief Unit test for food module.
#  @detail This class do the unit test cases for part of the functions in
#  the food module, and it passes once all the outputs are the same
#  as the expected ones.
class FoodTest(unittest.TestCase):

    ## @brief Test if the change function in food module works properly.
    def test_food_change(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        for i in range(100):
            food = Food()
            food.change()
            self.assertEqual(food.life, True, "test_food_change")
            if food.kind == 1:
                self.assertEqual(food.image, food.food_boom, "test_food_change")
            if food.kind == 2:
                self.assertEqual(food.image, food.food_clock, "test_food_change")
            if food.kind == 3:
                self.assertEqual(food.image, food.food_gun, "test_food_change")
            if food.kind == 4:
                self.assertEqual(food.image, food.food_iron, "test_food_change")
            if food.kind == 5:
                self.assertEqual(food.image, food.food_star, "test_food_change")
        pygame.quit()


# Run the tests
if __name__ == '__main__':
    unittest.main()
