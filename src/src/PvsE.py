## @file PvsE.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief PvsE Module
#  @date 03/23/2020

import pygame
from myTankControl import operatePlayer1, operatePlayer2
from Screen import chooseTankScreen, loadingMapScreen,\
    operationInstructPlay, ruleScreen, endScreen_PVE
from display import drawPVE
import food
import Map
from Map import CoordinateT
import enemyTank
import sys
import datetime
from decTime import decTime
from os import listdir
from os.path import isfile, join


## @brief Starts the PvsE mode
#  @details Starts the PvsE mode. Two players can control their tanks to
#  have a battle with enermy tnaks.
def PvsE():
    game_result = False

    # let players choose their tanks
    coordinate_T1 = CoordinateT(8, 24)
    coordinate_T2 = CoordinateT(16, 24)
    myTank_T1, myTank_T2 = chooseTankScreen(coordinate_T1, coordinate_T2)

    # let players to choose map
    File = [f for f in listdir("../map/PVEMap") if
        isfile(join("../map/PVEMap", f))]
    returnMap = loadingMapScreen(File)
    returnMap = "../map/PVEMap/" + returnMap
    operationInstructPlay()
    ruleScreen(0)

    pygame.init()
    pygame.mixer.init()

    resolution = 630, 630
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Tank War ")

    # loading images and audio
    background_image = pygame.image.load('../image/background.png')

    bang_sound = pygame.mixer.Sound("../music/bang.wav")
    bang_sound.set_volume(1)
    fire_sound = pygame.mixer.Sound("../music/Gunfire.wav")
    start_sound = pygame.mixer.Sound("../music/start.wav")
    start_sound.play()

    # define groups for tanks, bullets
    allTankGroup = pygame.sprite.Group()
    mytankGroup = pygame.sprite.Group()
    allEnemyGroup = pygame.sprite.Group()
    redEnemyGroup = pygame.sprite.Group()
    greenEnemyGroup = pygame.sprite.Group()
    otherEnemyGroup = pygame.sprite.Group()
    enemyBulletGroup = pygame.sprite.Group()
    # create map
    bgMap = Map.PVEMap()
    bgMap.loadPVEMap(returnMap)
    # create food
    prop = food.Food()

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
    # create enemy tank
    for i in range(1, 4):
        enemy = enemyTank.EnemyTank(i)
        allTankGroup.add(enemy)
        allEnemyGroup.add(enemy)
        if enemy.isred == True:
            redEnemyGroup.add(enemy)
            continue
        if enemy.kind == 3:
            greenEnemyGroup.add(enemy)
            continue
        otherEnemyGroup.add(enemy)
    # enemy tank appearance effect
    appearance_image = pygame.image.load("../image/appear.png").convert_alpha()
    appearance = []
    appearance.append(appearance_image.subsurface((0, 0), (48, 48)))
    appearance.append(appearance_image.subsurface((48, 0), (48, 48)))
    appearance.append(appearance_image.subsurface((96, 0), (48, 48)))

    # define events
    # create enemy tank events
    DELAYEVENT = pygame.constants.USEREVENT
    pygame.time.set_timer(DELAYEVENT, 200)
    # create enemy bullets events
    ENEMYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 1
    pygame.time.set_timer(ENEMYBULLETNOTCOOLINGEVENT, 1000)
    # create my tank events
    MYBULLETNOTCOOLINGEVENT = pygame.constants.USEREVENT + 2
    pygame.time.set_timer(MYBULLETNOTCOOLINGEVENT, 200)
    # enemy tank freeze events
    NOTMOVEEVENT = pygame.constants.USEREVENT + 3
    pygame.time.set_timer(NOTMOVEEVENT, 8000)
    # double life tank events
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
    enemyNumber = 3
    enemyCouldMove = True
    switch_R1_R2_image = True
    homeSurvive = True
    running_T1 = True
    running_T2 = True
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # check my tank bullet cooling event
            if event.type == MYBULLETNOTCOOLINGEVENT:
                myTank_T1.bulletNotCooling = True
                myTank_T2.bulletNotCooling = True
            # check enemy tank bullet cooling events
            if event.type == ENEMYBULLETNOTCOOLINGEVENT:
                for each in allEnemyGroup:
                    each.bulletNotCooling = True

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

            # enemy tank freeze
            if event.type == NOTMOVEEVENT:
                enemyCouldMove = True

            # create enermy tank
            if event.type == DELAYEVENT:
                if enemyNumber < 4:
                    enemy = enemyTank.EnemyTank()
                    if pygame.sprite.spritecollide(enemy, allTankGroup, False, None):
                        break
                    allEnemyGroup.add(enemy)
                    allTankGroup.add(enemy)
                    enemyNumber += 1
                    if enemy.isred == True:
                        redEnemyGroup.add(enemy)
                    elif enemy.kind == 3:
                        greenEnemyGroup.add(enemy)
                    else:
                        otherEnemyGroup.add(enemy)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.KMOD_CTRL:
                    pygame.quit()
                    sys.exit()

        # check players' operations
        key_pressed = pygame.key.get_pressed()
        key_pressed, moving, movdir, myTank_T1, allTankGroup,\
            bgMap.brickGroup, bgMap.ironGroup, running_T1 =\
            operatePlayer1(fire_sound, key_pressed, moving,
                movdir, myTank_T1, allTankGroup, bgMap.brickGroup,
                bgMap.ironGroup, running_T1)

        key_pressed2 = pygame.key.get_pressed()
        key_pressed2, moving2, movdir2, myTank_T2, allTankGroup,\
            bgMap.brickGroup, bgMap.ironGroup, running_T2 = \
            operatePlayer2(fire_sound, key_pressed2, moving2,
                movdir2, myTank_T2, allTankGroup, bgMap.brickGroup,
                bgMap.ironGroup, running_T2)

        # display game image on the screen
        homeSurvive, mytankGroup, deadCount1, deadCount2,\
            switch_R1_R2_image, running_T1, running_T2,\
            allTankGroup, enemyNumber, myTank_T1.bullet.life,\
            myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right,\
            myTank_T2.bullet.life, myTank_T2.bullet.rect.left,\
            myTank_T2.bullet.rect.right, moving, myTank_T1.rect.left,\
            myTank_T1.rect.top, myTank_T1.level, myTank_T2.rect.left,\
            myTank_T2.rect.top, prop.life, enemyCouldMove = \
            drawPVE(homeSurvive, mytankGroup, deadCount1,
                deadCount2, switch_R1_R2_image, enemyCouldMove,
                enemyNumber, prop, moving, running_T1, running_T2,
                bgMap, background_image, screen, delay, myTank_T1,
                myTank_T2, allEnemyGroup, allTankGroup, appearance,
                enemyBulletGroup, redEnemyGroup, greenEnemyGroup,
                otherEnemyGroup)

        # display count down time
        my_font = pygame.font.Font(None, 40)
        ch = str(ttime.minute)+':'+str(ttime.second)
        screen.blit(my_font.render(ch, True, (0, 255, 0)), (0, 0))

        # check the game result
        if ttime.second == ttime.minute == ttime.hour == 0:
            game_result = True
            break
        if deadCount1 >= 3 and deadCount2 >= 3:
            game_result = False
            break
        if homeSurvive == False:
            game_result = False
            break

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)

    # display game result
    endScreen_PVE(game_result)
