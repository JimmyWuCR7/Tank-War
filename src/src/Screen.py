## @file Screen.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Functions that can be used to show a particular process.
#  @date 03/25/2020

import pygame
from highSpeedTank import highSpeedTank
from doubleLifeTank import doubleLifeTank
from fastBulletTank import fastBulletTank
import sys


## @brief StartGame screen.
#  @details StartGame function will show a screen of
#  game starting process. In this gaming procedure,
#  users will be able to know the game starts and
#  return can be pressed to continue the game.
def StartGame():
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    start = pygame.image.load("../image/Start.png")
    screen.blit(start, (0, 0))

    confirm = False
    while True:
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break

        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)


## @brief Menue screen.
#  @details Menue function will show the selection of
#  gaming modes, including PVE, PVP, and Map Editing.
#  users  can select one of them by pressing the corresponding
#  key and press return to continue.
def Menue():
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    menue = pygame.image.load("../image/Menue.png")
    screen.blit(menue, (0, 0))
    mode = 1
    confirm = False
    keypress = pygame.key.get_pressed()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_1:
                    mode = 1
                elif event.key == pygame.K_2:
                    mode = 2
                elif event.key == pygame.K_3:
                    mode = 3

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break

        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)

    return mode


## @brief chooseTankScreen screen.
#  @details chooseTankScreen function will show the selection of
#  tanks, including double-life tank, fast-bullet tank, and
#  high-speed tank. Users can select one of them by pressing the
#  corresponding key and press return to continue.
def chooseTankScreen(coordinate_T1, coordinate_T2):
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    chooseTank = pygame.image.load("../image/chooseTank.png")
    screen.blit(chooseTank, (0, 0))

    c1 = coordinate_T1
    c2 = coordinate_T2

    myTank_T1 = doubleLifeTank(c1)
    myTank_T2 = highSpeedTank(c2)
    keypress = pygame.key.get_pressed()

    confirm = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_1:
                    myTank_T1 = doubleLifeTank(c1)
                if event.key == pygame.K_2:
                    myTank_T1 = highSpeedTank(c1)
                if event.key == pygame.K_3:
                    myTank_T1 = fastBulletTank(c1)

                if event.key == pygame.K_7:
                    myTank_T2 = doubleLifeTank(c2)
                if event.key == pygame.K_8:
                    myTank_T2 = highSpeedTank(c2)
                if event.key == pygame.K_9:
                    myTank_T2 = fastBulletTank(c2)

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break
        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)

    return myTank_T1, myTank_T2


## @brief loadingMapScreen screen.
#  @details loadingMapScreen function will show the selection of
#  maps. Users can select one of them by pressing the
#  corresponding key and press return to continue.
def loadingMapScreen(File):
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")

    image = pygame.image.load("../image/MapScreen.png")
    screen.blit(image, (0, 0))

    if ".DS_Store" in File:
        File.remove(".DS_Store")

    my_font = pygame.font.Font(None, 40)
    coor = 240
    countt = 1
    for i in File:
        string = str(countt) + ". " + str(i)
        screen.blit(my_font.render(string, True, (55, 100, 100)), (160, coor))
        coor += 30
        countt += 1

    confirm = False
    returnMap = 'Map1(default)'
    keypress = pygame.key.get_pressed()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_1:
                    returnMap = File[0]

                if event.key == pygame.K_2:
                    if len(File) >= 2:
                        returnMap = File[1]

                if event.key == pygame.K_3:
                    if len(File) >= 3:
                        returnMap = File[2]

                if event.key == pygame.K_4:
                    if len(File) >= 4:
                        returnMap = File[3]

                if event.key == pygame.K_5:
                    if len(File) >= 5:
                        returnMap = File[4]

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break
        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)
    return returnMap


## @brief Operation Instruction Screen for PVP and PVE.
#  @details Display operation instruction for users to
#  show how to control their tank for PVP and PVE.
def operationInstructPlay():
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    start = pygame.image.load("../image/operationPlay.png")
    screen.blit(start, (0, 0))

    confirm = False
    while True:
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break

        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)


## @brief Operation Instruction Screen for map editing.
#  @details Display operation instruction for users to
#  show how to control their tank for map editing.
def operationInstructMap():
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    start = pygame.image.load("../image/operationMap.png")
    screen.blit(start, (0, 0))

    confirm = False
    while True:
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break

        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)


## @brief loadingMapScreen screen.
#  @details loadingMapScreen function will show the selection of
#  maps. Users can select one of them by pressing the
#  corresponding key and press return to continue.
def ruleScreen(rule):
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")

    PVERule = pygame.image.load("../image/PVERule.png")
    PVPRule = pygame.image.load("../image/PVPRule.png")
    if rule == 0:
        image = PVERule
    if rule == 1:
        image = PVPRule
    screen.blit(image, (0, 0))

    confirm = False
    keypress = pygame.key.get_pressed()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break
        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)


## @brief endScreen_PVE screen.
#  @details endScreen_PVE function will show the result screen of
#  PVE game based on the input result. PVE has two possible
#  results: winning and losing. The endScreen_PVE will show the
#  corresponding result screen and show the result directly to
#  the players.
def endScreen_PVE(result):
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")

    PVEWin = pygame.image.load("../image/PVEWin.png")
    PVELose = pygame.image.load("../image/PVELose.png")
    if (result):
        image = PVEWin
    else:
        image = PVELose
    screen.blit(image, (0, 0))

    keypress = pygame.key.get_pressed()

    confirm = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break
        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)


## @brief endScreen_PVP screen.
#  @details endScreen_PVP function will show the result screen of
#  PVP game based on the input result. PVP has three possible
#  results: winning, losing, and draw. The endScreen_PVP will show the
#  corresponding result screen and show the result directly to
#  the players.
def endScreen_PVP(result):
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")

    PVPWin1 = pygame.image.load("../image/PVPWin1.png")
    PVPWin2 = pygame.image.load("../image/PVPWin2.png")
    PVPDraw = pygame.image.load("../image/PVPDraw.png")
    if (result == 1):
        image = PVPWin1
    elif (result == 2):
        image = PVPWin2
    else:
        image = PVPDraw
    screen.blit(image, (0, 0))

    keypress = pygame.key.get_pressed()

    confirm = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break

        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)


## @brief saveScreenME screen.
#  @details saveScreenME function will show the selection of
#  map names that are available for saving. Users can select
#  one of them by pressing the corresponding key and
#  press return to continue.
def saveScreenME(File):
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    chooseMap = pygame.image.load("../image/MapScreen.png")
    screen.blit(chooseMap, (0, 0))
    my_font = pygame.font.Font(None,40)
    coor = 240
    countt = 1
    if "Map1(default)" in File:
        File.remove("Map1(default)")
    if ".DS_Store" in File:
        File.remove(".DS_Store")
    for i in File:
        string = str(countt) + ". " + str(i)
        screen.blit(my_font.render(string, True, (55, 100, 100)), (160, coor))
        coor += 30
        countt += 1

    confirm = False
    returnMap = File[0]
    keypress = pygame.key.get_pressed()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_1:
                    returnMap = File[0]

                if event.key == pygame.K_2:
                    if len(File) >= 2:
                        returnMap = File[1]
                    else:
                        returnMap = File[0]

                if event.key == pygame.K_3:
                    if len(File) >= 3:
                        returnMap = File[2]
                    else:
                        returnMap = File[1]

                if event.key == pygame.K_4:
                    if len(File) >= 4:
                        returnMap = File[3]
                    else:
                        returnMap = File[2]

                if event.key == pygame.K_5:
                    if len(File) >= 5:
                        returnMap = File[4]
                    else:
                        returnMap = File[3]

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break
        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)
    return returnMap


## @brief chooseMapME screen.
#  @details chooseMapME function will show the selection of
#  map types that are available for editing, like PVP maps
#  and PVE maps. Users can select one of them by pressing
#  the corresponding key and press return to continue.
def chooseMapME():
    pygame.init()
    clock = pygame.time.Clock()
    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")
    chooseMap = pygame.image.load("../image/chooseMapME.png")
    screen.blit(chooseMap, (0, 0))

    selection = 0

    keypress = pygame.key.get_pressed()

    confirm = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_1:
                    selection = 0
                if event.key == pygame.K_2:
                    selection = 1

                if event.key == pygame.K_RETURN:
                    confirm = True
                    break
        if confirm:
            break
        pygame.display.flip()
        clock.tick(60)

    return selection
