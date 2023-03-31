## @file PvsP.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief PvsP Module
#  @date 03/23/2020

import pygame
from myTankControl import operatePlayer1, operatePlayer2
from Screen import chooseTankScreen, loadingMapScreen,\
    operationInstructPlay, ruleScreen, endScreen_PVP
from display import drawPVP
import Map
from Map import CoordinateT
import sys
import datetime
from decTime import decTime
from os import listdir
from os.path import isfile, join

## @brief Starts the PvsP mode
#  @details Starts the PvsP mode. Two players can control their tanks to
#  have a battle against each other.
def PvsP():
    game_result = 1

    # let players choose their tanks
    coordinate_T1 = CoordinateT(8, 24)
    coordinate_T2 = CoordinateT(16, 24)
    myTank_T1, myTank_T2 = chooseTankScreen(coordinate_T1, coordinate_T2)

    # let players to choose map
    File = [f for f in listdir("../map/PVPMap") if
        isfile(join("../map/PVPMap", f))]
    #File.remove(".DS_Store")
    returnMap = loadingMapScreen(File)
    returnMap = "../map/PVPMap/" + returnMap
    operationInstructPlay()
    ruleScreen(1)

    pygame.init()
    pygame.mixer.init()

    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")

    # loading images and audio
    background_image = pygame.image.load('../image/background.png')

    fire_sound = pygame.mixer.Sound("../music/Gunfire.wav")
    start_sound = pygame.mixer.Sound("../music/start.wav")
    start_sound.play()

    # define groups for tanks
    allTankGroup = pygame.sprite.Group()
    mytankGroup = pygame.sprite.Group()

    # create map
    bgMap = Map.PVPMap()
    bgMap.loadPVPMap(returnMap)

    # Tank death count
    deadCount1 = 0
    deadCount2 = 0

    strtime1 = '1999-9-4 00:00:00'
    strtime2 = '1999-9-4 00:03:00'
    deadline = datetime.datetime.strptime(strtime2, '%Y-%m-%d %H:%M:%S')
    now = datetime.datetime.strptime(strtime1, '%Y-%m-%d %H:%M:%S')
    subtime = (deadline - now).seconds
    ttime = decTime(subtime)

    # add tanks into groups
    allTankGroup.add(myTank_T1)
    mytankGroup.add(myTank_T1)

    allTankGroup.add(myTank_T2)
    mytankGroup.add(myTank_T2)

    # define events
    # create enemy tank events
    MYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 2
    pygame.time.set_timer(MYBULLETNOTCOOLINGEVENT, 200)

    # double life tank property
    BULLETP = pygame.constants.USEREVENT + 4
    pygame.time.set_timer(BULLETP, 1000)
    # Leap events
    LEAP = pygame.constants.USEREVENT + 5
    pygame.time.set_timer(LEAP, 1000)
    # Time events
    TIME = pygame.constants.USEREVENT + 6
    pygame.time.set_timer(TIME, 1000)

    delay = 100
    moving = 0
    movdir = 0
    moving2 = 0
    movdir2 = 0
    switch_R1_R2_image = True
    homeDead = 0
    running_T1 = True
    running_T2 = True
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # check bullet colling event
            if event.type == MYBULLETNOTCOOLINGEVENT:
                myTank_T1.bulletNotCooling = True
                myTank_T2.bulletNotCooling = True

            # check bullet proof event
            if event.type == BULLETP:
                if myTank_T1.ID == 1:
                    myTank_T1.bulletproof = False
                if myTank_T2.ID == 1:
                    myTank_T2.bulletproof = False

            # check leap event
            if event.type == LEAP:
                if myTank_T1.ID == 2:
                    myTank_T1.leap_end()
                if myTank_T2.ID == 2:
                    myTank_T2.leap_end()

            # check time event
            if event.type == TIME:
                ttime.subTime()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_e:
                    myTank_T1.levelUp()
                if event.key == pygame.K_q:
                    myTank_T1.levelDown()

        # check players' operations
        key_pressed = pygame.key.get_pressed()
        key_pressed, moving, movdir, myTank_T1, allTankGroup,\
            bgMap.brickGroup, bgMap.ironGroup, running_T1 = \
            operatePlayer1(fire_sound, key_pressed, moving,
                movdir, myTank_T1, allTankGroup,
                bgMap.brickGroup, bgMap.ironGroup, running_T1)

        key_pressed2 = pygame.key.get_pressed()
        key_pressed2, moving2, movdir2, myTank_T2, allTankGroup,\
            bgMap.brickGroup, bgMap.ironGroup, running_T2 = \
            operatePlayer2(fire_sound, key_pressed2, moving2,
                movdir2, myTank_T2, allTankGroup,
                bgMap.brickGroup, bgMap.ironGroup, running_T2)

        # display game image on the screen
        homeDead, mytankGroup, deadCount1, deadCount2,\
            switch_R1_R2_image, running_T1, running_T2,\
            allTankGroup, myTank_T1.bullet.life,\
            myTank_T1.bullet.rect.left,\
            myTank_T1.bullet.rect.right, myTank_T2.bullet.life,\
            myTank_T2.bullet.rect.left,\
            myTank_T2.bullet.rect.right, moving,\
            myTank_T1.rect.left, myTank_T1.rect.top,\
            myTank_T1.level, myTank_T2.rect.left,\
            myTank_T2.rect.top = drawPVP(homeDead, mytankGroup,
                deadCount1, deadCount2, switch_R1_R2_image, moving,
                running_T1, running_T2, bgMap, background_image,
                screen, delay, myTank_T1, myTank_T2, allTankGroup)

        # set up font
        my_font = pygame.font.Font(None, 40)
        ch = str(ttime.minute) + ':' + str(ttime.second)
        screen.blit(my_font.render(ch, True, (0, 255, 0)), (0, 0))

        # check the game result
        if ttime.second == ttime.minute == ttime.hour == 0:
            game_result = 0
            break
        if deadCount1 >= 3:
            game_result = 2
            break
        if deadCount2 >= 3:
            game_result = 1
            break
        if homeDead == 2:
            game_result = 1
            break
        if homeDead == 1:
            game_result = 2
            break

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)
    # display game result
    endScreen_PVP(game_result)
