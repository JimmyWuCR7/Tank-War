## @file mapEditingt.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Map Editing Module
#  @date 03/23/2020

import pygame
from myTankControl import operatePlayerME
from Screen import chooseMapME, saveScreenME
from display import drawME
from Map import CoordinateT
from MapEditTank import MapEditTank
from Map import PVEMap, PVPMap, CoordinateT
from os import listdir
from os.path import isfile, join


## @brief Starts the map editing mode
#  @details Starts the map editing mode to create PVE or PVP map.
#  User can control the tank to add bricks and iron, or delete walls.
#  Finally, saves the map to local storage.
def mapEditing():
    # let player to choose which kind of maps needs to be edited.
    selection = chooseMapME()
    if selection == 0:
        bgMap = PVEMap()
        bgMap.loadPVEMap("../map/PVEMap/Map1(default)")
        File = [
            f for f in listdir("../map/PVEMap") if 
            isfile(join("../map/PVEMap", f))
            ]

    if selection == 1:
        bgMap = PVPMap()
        bgMap.loadPVPMap("../map/PVPMap/Map1(default)")
        File = [
            f for f in listdir("../map/PVPMap") if 
            isfile(join("../map/PVPMap", f))
            ]

    # create map MapEditTank
    coordinate_T1 = CoordinateT(8, 24)
    myTank_T1 = MapEditTank(coordinate_T1)

    pygame.init()
    pygame.mixer.init()

    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")

    # loading image
    background_image = pygame.image.load('../image/background.png')

    # define groups for tanks, bullets, walls
    mytankGroup = pygame.sprite.Group()
    allTankGroup = pygame.sprite.Group()
    clock = pygame.time.Clock()

    allTankGroup.add(myTank_T1)
    mytankGroup.add(myTank_T1)
    running_T1 = True

    moving = 0
    deadCount1 = 0
    switch_R1_R2_image = True
    movdir = 0
    delay = 100
    deadCount1 = 0
    confirm2 = False

    while True:
        # check player's operations
        key_pressed = pygame.key.get_pressed()
        key_pressed, moving, movdir, myTank_T1,\
            allTankGroup, bgMap, running_T1 = \
            operatePlayerME(
                key_pressed, moving, movdir,
                myTank_T1, allTankGroup, bgMap, running_T1
                )

        # display game image on the screen
        bgMap, allTankGroup, mytankGroup,\
            switch_R1_R2_image, moving,\
            running_T1, myTank_T1.bullet.life,\
            myTank_T1.bullet.rect.left,\
            myTank_T1.bullet.rect.right, myTank_T1.rect.left,\
            myTank_T1.rect.top = \
            drawME(
                bgMap, deadCount1, mytankGroup,
                switch_R1_R2_image, moving,
                running_T1, background_image,
                screen, delay, myTank_T1, allTankGroup
                )

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    confirm2 = True
                    break

        if confirm2:
            break

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)

    # save map
    returnMap = saveScreenME(File)
    if selection == 0:
        returnMap = "../map/PVEMap/" + returnMap
    if selection == 1:
        returnMap = "../map/PVPMap/" + returnMap
    bgMap.saveMap(returnMap)
