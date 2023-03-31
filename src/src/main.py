## @file main.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Main Module
#  @date 03/23/2020
import PvsE
import PvsP
import mapEditing
from Screen import StartGame, Menue

# display game start screen
StartGame()

# provide menue screen to choose mode
while True:
    mode = Menue()
    if mode == 1:
        PvsE.PvsE()
    elif mode == 2:
        PvsP.PvsP()
    elif mode == 3:
        mapEditing.mapEditing()
