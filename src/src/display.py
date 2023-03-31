## @file display.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Functions that can show the change during the game.
#  @date 03/25/2020

import pygame
import wall
from Map import CoordinateT

## @brief display Constant
#  @details EDGE_LENGTH represents the length of the edge in pixel.
#  GRID_LENGTH represents the length of one grid of the map in pixel.
#  TANK1_BORN represents the location that player1's tank borns at.
#  TANK2_BORN represents the location that player2's tank borns at.
#  BULLET_COORDINATE represents the coordinate of the bullet.
EDGE_LENGTH = 3
GRID_LENGTH = 24
TANK1_BORN = CoordinateT(8, 24)
TANK2_BORN = CoordinateT(16, 24)
BULLET_COORDINATE = CoordinateT(12, 24)

pygame.mixer.init()
bang_sound = pygame.mixer.Sound("../music/bang.wav")
bang_sound.set_volume(1)


## @brief checkCollideME.
#  @details checkCollideME function will check whether
#  the players' bullet collide with brick or iron wall in
#  map editing mode.
def checkCollideME(bullet, bgMap):
    if pygame.sprite.spritecollide(bullet, bgMap.brickGroup, True, None):
        bullet.life = False
        bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH
    elif pygame.sprite.spritecollide(bullet, bgMap.ironGroup, True, None):
        bullet.life = False
        bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH
    return bullet, bgMap


## @brief checkCollidePVP.
#  @details checkCollidePVP function will check whether
#  the players' bullets collide with brick wall, iron wall, the
#  other player's tank, and other player's home base in the
#  PVP mode.
def checkCollidePVP(tank_born_coordinate, bullet, bgMap, myTank, homeDead, deadCount2):

    # check collides between bullet and players' tanks.
    if pygame.sprite.collide_rect(bullet, myTank):
        bullet.life = False
        if deadCount2 < 3:
            if myTank.ID == 1:
                if myTank.bulletproof is False and myTank.life == 1:
                    bang_sound.play()
                    myTank.rect.left, myTank.rect.top = EDGE_LENGTH + tank_born_coordinate.x * GRID_LENGTH, EDGE_LENGTH + tank_born_coordinate.y * GRID_LENGTH

                    for i in range(myTank.level+1):
                        myTank.levelDown()
                    deadCount2 += 1
                    myTank.life = 2

                elif myTank.bulletproof is True:
                    pass
                elif myTank.life == 2:
                    myTank.life -= 1

            else:
                bang_sound.play()
                myTank.rect.left, myTank.rect.top = EDGE_LENGTH + tank_born_coordinate.x * GRID_LENGTH, EDGE_LENGTH + tank_born_coordinate.y * GRID_LENGTH

                for i in range(myTank.level+1):
                    myTank.levelDown()
                deadCount2 += 1


#    Check collisions between bullet and brick walls.
    if pygame.sprite.spritecollide(bullet, bgMap.brickGroup, True, None):
        bullet.life = False
        bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH

#    Check collisions between bullet and home bases.
    blocks_hit_list = pygame.sprite.spritecollide(bullet, bgMap.homeGroup, True, None)
    if blocks_hit_list:
        bullet.life = False
        bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH
        homeDead = blocks_hit_list[0].homeID

#    Check collisions between bullet and iron walls.
    if bullet.strong:
        if pygame.sprite.spritecollide(bullet, bgMap.ironGroup, True, None):
            bullet.life = False
            bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH
    else:
        if pygame.sprite.spritecollide(bullet, bgMap.ironGroup, False, None):
            bullet.life = False
            bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH
    return bullet, bgMap, myTank, homeDead, deadCount2


## @brief checkCollidePVE.
#  @details checkCollidePVE function will check whether
#  the players' bullets collide with brick wall, iron wall,
#  enemies' tanks, and home base in the PVP mode.
def checkCollidePVE(enemyBulletGroup, bullet, redEnemyGroup, greenEnemyGroup, otherEnemyGroup, bgMap, prop, enemyNumber, homeSurvive):

    # check collision between bullet and enemy tanks.
    for each in enemyBulletGroup:
        if each.life:
            if pygame.sprite.collide_rect(bullet, each):
                bullet.life = False
                each.life = False
                pygame.sprite.spritecollide(bullet, enemyBulletGroup, True, None)

    if pygame.sprite.spritecollide(bullet, redEnemyGroup, True, None):
        prop.change()
        bang_sound.play()
        enemyNumber -= 1
        bullet.life = False

    elif pygame.sprite.spritecollide(bullet, greenEnemyGroup, False, None):
        for each in greenEnemyGroup:
            if pygame.sprite.collide_rect(bullet, each):
                if each.life == 1:
                    pygame.sprite.spritecollide(bullet, greenEnemyGroup, True, None)
                    bang_sound.play()
                    enemyNumber -= 1

                elif each.life == 2:
                    each.life -= 1
                    each.tank = each.enemy_3_0
                elif each.life == 3:
                    each.life -= 1
                    each.tank = each.enemy_3_2
        bullet.life = False
    elif pygame.sprite.spritecollide(bullet, otherEnemyGroup, True, None):
        bang_sound.play()
        enemyNumber -= 1
        bullet.life = False


#    Check collisions between bullet and brick walls.
    if pygame.sprite.spritecollide(bullet, bgMap.brickGroup, True, None):
        bullet.life = False
        bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH

#    Check collisions between bullet and home bases.
    if pygame.sprite.spritecollide(bullet, bgMap.homeGroup, True, None):
        bullet.life = False
        bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH
        homeSurvive = False

#    Check collisions between bullet and iron walls.
    if bullet.strong:
        if pygame.sprite.spritecollide(bullet, bgMap.ironGroup, True, None):
            bullet.life = False
            bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH
    else:
        if pygame.sprite.spritecollide(bullet, bgMap.ironGroup, False, None):
            bullet.life = False
            bullet.rect.left, bullet.rect.right = EDGE_LENGTH + BULLET_COORDINATE.x * GRID_LENGTH, EDGE_LENGTH + BULLET_COORDINATE.y * GRID_LENGTH
    return enemyBulletGroup, bullet, redEnemyGroup, greenEnemyGroup, otherEnemyGroup, bgMap, prop, enemyNumber, homeSurvive


## @brief drawBG.
#  @details drawBG function draw the background on screen.
def drawBG(background_image, screen):
    screen.blit(background_image, (0, 0))


## @brief drawBrick.
#  @details drawBrick function draw all the brick walls on screen.
def drawBrick(bgMap, screen):
    for each in bgMap.brickGroup:
        screen.blit(each.image, each.rect)


## @brief drawIron.
#  @details drawIron function draw all the iron walls on screen.
def drawIron(bgMap, screen):
    for each in bgMap.ironGroup:
        screen.blit(each.image, each.rect)


## @brief drawHome.
#  @details drawHome function draw all the home bases on screen.
def drawHome(bgMap, screen):
    for each in bgMap.homeGroup:
        screen.blit(each.image, each.rect)


## @brief drawTank_1.
#  @details drawTank_1 function draw the player1's tank on screen.
#  The tank image will change based on switch_R1_R2_image in order
#  to show the dynamic wheel.
def drawTank_1(deadCount1, switch_R1_R2_image, running_T1, delay, myTank_T1, screen):

    if deadCount1 < 3:
        if not (delay % 5):
            switch_R1_R2_image = not switch_R1_R2_image
        if (switch_R1_R2_image) and running_T1:
            screen.blit(myTank_T1.tank_R0, (myTank_T1.rect.left, myTank_T1.rect.top))
            running_T1 = False
        else:
            screen.blit(myTank_T1.tank_R1, (myTank_T1.rect.left, myTank_T1.rect.top))
    return switch_R1_R2_image, running_T1


## @brief drawTank_2.
#  @details drawTank_2 function draw the player2's tank on screen.
#  The tank image will change based on switch_R1_R2_image in order
#  to show the dynamic wheel.
def drawTank_2(deadCount2, switch_R1_R2_image, running_T2, myTank_T2, screen):
    if deadCount2 < 3:
        if switch_R1_R2_image and running_T2:
            screen.blit(myTank_T2.tank_R0, (myTank_T2.rect.left, myTank_T2.rect.top))
            running_T2 = False
        else:
            screen.blit(myTank_T2.tank_R1, (myTank_T2.rect.left, myTank_T2.rect.top))
    return running_T2


## @brief drawEnemyTank.
#  @details drawEnemyTank function draw the enemies' tanks on screen.
#  The tank image will change based on switch_R1_R2_image in order
#  to show the dynamic wheel.
def drawEnemyTank(switch_R1_R2_image, enemyCouldMove, bgMap, allEnemyGroup, screen, allTankGroup, appearance):
    for each in allEnemyGroup:

        if each.flash:

            if switch_R1_R2_image:
                screen.blit(each.tank_R0, (each.rect.left, each.rect.top))
                if enemyCouldMove:
                    allTankGroup.remove(each)
                    each.move(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
                    allTankGroup.add(each)
            else:
                screen.blit(each.tank_R1, (each.rect.left, each.rect.top))
                if enemyCouldMove:
                    allTankGroup.remove(each)
                    each.move(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
                    allTankGroup.add(each)
        else:

            if each.times > 0:
                each.times -= 1
                if each.times <= 10:
                    screen.blit(appearance[2], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
                elif each.times <= 20:
                    screen.blit(appearance[1], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
                elif each.times <= 30:
                    screen.blit(appearance[0], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
                elif each.times <= 40:
                    screen.blit(appearance[2], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
                elif each.times <= 50:
                    screen.blit(appearance[1], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
                elif each.times <= 60:
                    screen.blit(appearance[0], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
                elif each.times <= 70:
                    screen.blit(appearance[2], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
                elif each.times <= 80:
                    screen.blit(appearance[1], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
                elif each.times <= 90:
                    screen.blit(appearance[0], (EDGE_LENGTH + each.x * 12 * GRID_LENGTH, EDGE_LENGTH))
            if each.times == 0:
                each.flash = True
    return switch_R1_R2_image, allTankGroup


## @brief drawMyBullet.
#  @details drawMyBullet function draw the players' bullets on screen in
#  PVE mode. It will also check the collide between the bullet and other
#  sprites by calling the checkCollidePVE function.
def drawMyBullet(deadCount, homeSurvive, enemyNumber, prop, bgMap, myTank, screen, enemyBulletGroup, redEnemyGroup, greenEnemyGroup, otherEnemyGroup):
    if deadCount < 3:
        if myTank.bullet.life:
            myTank.bullet.move()

            screen.blit(myTank.bullet.bullet, myTank.bullet.rect)

            B1 = myTank.bullet

            enemyBulletGroup, B1, redEnemyGroup, greenEnemyGroup, otherEnemyGroup, bgMap, prop, enemyNumber, homeSurvive = checkCollidePVE(enemyBulletGroup, B1, redEnemyGroup, greenEnemyGroup, otherEnemyGroup, bgMap, prop, enemyNumber, homeSurvive)

        if myTank.ID == 3 and myTank.bullet2.life:
            myTank.bullet2.move()

            screen.blit(myTank.bullet2.bullet, myTank.bullet2.rect)

            B2 = myTank.bullet2

            enemyBulletGroup, B2, redEnemyGroup, greenEnemyGroup, otherEnemyGroup, bgMap, prop, enemyNumber, homeSurvive = checkCollidePVE(enemyBulletGroup, B2, redEnemyGroup, greenEnemyGroup, otherEnemyGroup, bgMap, prop, enemyNumber, homeSurvive)

    return deadCount, homeSurvive, enemyNumber, myTank.bullet.life, myTank.bullet.rect.left, myTank.bullet.rect.right


## @brief drawEnemyBullet.
#  @details drawEnemyBullet function draw the enemies' bullets on screen in
#  PVE mode. It will also check the collide between the bullet and other
#  sprites like players' tanks, brick wall, iron wall, and home base.
def drawEnemyBullet(homeSurvive, mytankGroup, deadCount1, deadCount2, enemyCouldMove, moving, bgMap, allEnemyGroup, enemyBulletGroup, screen, myTank_T1, myTank_T2):
    for each in allEnemyGroup:

        if not each.bullet.life and each.bulletNotCooling and enemyCouldMove:
            enemyBulletGroup.remove(each.bullet)
            each.shoot()
            enemyBulletGroup.add(each.bullet)
            each.bulletNotCooling = False

        if each.flash:
            if each.bullet.life:

                if enemyCouldMove:
                    each.bullet.move()
                screen.blit(each.bullet.bullet, each.bullet.rect)

                # check collision between enemy bullets and player1's tank.
                if pygame.sprite.collide_rect(each.bullet, myTank_T1):
                    if deadCount1 < 3:
                        if myTank_T1.ID == 1:
                            if myTank_T1.bulletproof is False and myTank_T1.life == 1:
                                bang_sound.play()
                                myTank_T1.rect.left, myTank_T1.rect.top = EDGE_LENGTH + TANK1_BORN.x * GRID_LENGTH, EDGE_LENGTH + TANK1_BORN.y * GRID_LENGTH
                                each.bullet.life = False
                                moving = 0
                                for i in range(myTank_T1.level+1):
                                    myTank_T1.levelDown()
                                deadCount1 += 1
                                myTank_T1.life = 2
                            elif myTank_T1.bulletproof is True:
                                each.bullet.life = False
                            else:
                                each.bullet.life = False
                                myTank_T1.life -= 1
                        else:
                            bang_sound.play()
                            myTank_T1.rect.left, myTank_T1.rect.top = EDGE_LENGTH + TANK1_BORN.x * GRID_LENGTH, EDGE_LENGTH + TANK1_BORN.y * GRID_LENGTH
                            each.bullet.life = False
                            moving = 0
                            for i in range(myTank_T1.level+1):
                                myTank_T1.levelDown()
                            deadCount1 += 1

                # check collision between enemy bullets and player2's tank.
                if pygame.sprite.collide_rect(each.bullet, myTank_T2):
                    if deadCount2 < 3:
                        if myTank_T2.ID == 1:
                            if myTank_T2.bulletproof is False and myTank_T2.life == 1:
                                bang_sound.play()
                                myTank_T2.rect.left, myTank_T2.rect.top = EDGE_LENGTH + TANK2_BORN.x * GRID_LENGTH, EDGE_LENGTH + TANK2_BORN.y * GRID_LENGTH
                                each.bullet.life = False
                                for i in range(myTank_T2.level+1):
                                    myTank_T2.levelDown()
                                deadCount2 += 1
                                myTank_T2.life = 2
                            elif myTank_T2.bulletproof is True:
                                each.bullet.life = False
                            else:
                                each.bullet.life = False
                                myTank_T2.life -= 1

                        else:
                            bang_sound.play()
                            myTank_T2.rect.left, myTank_T2.rect.top = EDGE_LENGTH + TANK2_BORN.x * GRID_LENGTH, EDGE_LENGTH + TANK2_BORN.y * GRID_LENGTH
                            each.bullet.life = False
                            moving = 0
                            for i in range(myTank_T2.level+1):
                                myTank_T2.levelDown()
                            deadCount2 += 1

                # check collision between enemy bullets and home base.
                if pygame.sprite.spritecollide(each.bullet, bgMap.homeGroup, True, None):
                    each.bullet.life = False
                    homeSurvive = False

                # check collision between enemy bullets and brick walls.
                if pygame.sprite.spritecollide(each.bullet, bgMap.brickGroup, True, None):
                    each.bullet.life = False

                # check collision between enemy bullets and iron walls.
                if each.bullet.strong:
                    if pygame.sprite.spritecollide(each.bullet, bgMap.ironGroup, True, None):
                        each.bullet.life = False
                else:
                    if pygame.sprite.spritecollide(each.bullet, bgMap.ironGroup, False, None):
                        each.bullet.life = False
    return homeSurvive, mytankGroup, deadCount1, deadCount2, moving, myTank_T1.rect.left, myTank_T1.rect.top, myTank_T1.level, myTank_T2.rect.left, myTank_T2.rect.top


## @brief drawFood.
#  @details drawFood function draws the food on screen in
#  PVE mode. It will also check the collide between the bullet and other
#  sprites. It also defines the result after eating the corresponding food.
def drawFood(enemyNumber, enemyCouldMove, prop, bgMap, screen, allEnemyGroup, myTank):
    if prop.life:
        screen.blit(prop.image, prop.rect)

        if pygame.sprite.collide_rect(myTank, prop):
            if prop.kind == 1:
                for each in allEnemyGroup:
                    if pygame.sprite.spritecollide(each, allEnemyGroup, True, None):
                        bang_sound.play()
                        enemyNumber -= 1
                prop.life = False
            if prop.kind == 2:
                enemyCouldMove = False
                prop.life = False
            if prop.kind == 3:
                myTank.bullet.strong = True
                prop.life = False
            if prop.kind == 4:
                for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
                    bgMap.iron = wall.Iron()
                    bgMap.iron.rect.left, bgMap.iron.rect.top = EDGE_LENGTH + x * GRID_LENGTH, EDGE_LENGTH + y * GRID_LENGTH
                    bgMap.ironGroup.add(bgMap.iron)
                prop.life = False
            if prop.kind == 5:
                prop.life = False
                pass
            if prop.kind == 6:
                myTank.levelUp()
                prop.life = False
            if prop.kind == 7:
                myTank.life += 1
                prop.life = False
    return prop.life, enemyCouldMove, enemyNumber


## @brief drawMyBulletPVP.
#  @details drawMyBulletPVP function draw the players' bullets on screen in
#  PVP mode. It will also check the collide between the bullet and other
#  sprites by calling the checkCollidePVP function.
def drawMyBulletPVP(tank_born_coordinate, deadCount1, deadCount2, myTank_T2, homeDead, bgMap, myTank_T1, screen):
    if deadCount1 < 3:
        if myTank_T1.ID == 3:
            if myTank_T1.bullet.life:
                myTank_T1.bullet.move()

                screen.blit(myTank_T1.bullet.bullet, myTank_T1.bullet.rect)

                bullet1 = myTank_T1.bullet

                bullet1, bgMap, myTank_T2, homeDead, deadCount2 = checkCollidePVP(tank_born_coordinate, bullet1, bgMap, myTank_T2, homeDead, deadCount2)

            if myTank_T1.bullet2.life:
                myTank_T1.bullet2.move()

                screen.blit(myTank_T1.bullet2.bullet, myTank_T1.bullet2.rect)

                bullet2 = myTank_T1.bullet2

                bullet2, bgMap, myTank_T2, homeDead, deadCount2 = checkCollidePVP(tank_born_coordinate, bullet2, bgMap, myTank_T2, homeDead, deadCount2)

        else:
            if myTank_T1.bullet.life:

                screen.blit(myTank_T1.bullet.bullet, myTank_T1.bullet.rect)

                bullet1 = myTank_T1.bullet

                bullet1, bgMap, myTank_T2, homeDead, deadCount2 = checkCollidePVP(tank_born_coordinate, bullet1, bgMap, myTank_T2, homeDead, deadCount2)
                myTank_T1.bullet.move()

    return deadCount2, myTank_T2.rect.left, myTank_T2.rect.top, myTank_T2.level, homeDead, myTank_T1.bullet.life, myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right


## @brief drawBulletME.
#  @details drawBulletME function draw the players' bullets on screen in
#  map editing mode. It will also check the collide between
#  the bullet and other sprites by calling the checkCollideME function.
def drawBulletME(bgMap, myTank_T1, screen):
    if myTank_T1.bullet.life:
        screen.blit(myTank_T1.bullet.bullet, myTank_T1.bullet.rect)

        B = myTank_T1.bullet

        B, bgMap = checkCollideME(B, bgMap)
        myTank_T1.bullet.move()
    return bgMap, myTank_T1, screen


## @brief drawPVE.
#  @details drawPVE function draw all the necessary elements in
#  PVE mode by calling drawBG, drawBrick, drawIron, drawHome,
#  drawTank_1, drawTank_2, drawEnemyTank, drawMyBullet, drawEnemyBullet,
#  drawFood functions.
def drawPVE(homeSurvive, mytankGroup, deadCount1, deadCount2, switch_R1_R2_image, enemyCouldMove, enemyNumber, prop, moving, running_T1, running_T2, bgMap, background_image, screen, delay, myTank_T1, myTank_T2, allEnemyGroup, allTankGroup, appearance, enemyBulletGroup, redEnemyGroup, greenEnemyGroup, otherEnemyGroup):
    drawBG(background_image, screen)
    drawBrick(bgMap, screen)
    drawIron(bgMap, screen)
    drawHome(bgMap, screen)
    switch_R1_R2_image, running_T1 = drawTank_1(deadCount1, switch_R1_R2_image, running_T1, delay, myTank_T1, screen)
    running_T2 = drawTank_2(deadCount2, switch_R1_R2_image, running_T2, myTank_T2, screen)
    switch_R1_R2_image, allTankGroup = drawEnemyTank(switch_R1_R2_image, enemyCouldMove, bgMap, allEnemyGroup, screen, allTankGroup, appearance)
    deadCount1, homeSurvive, enemyNumber, myTank_T1.bullet.life, myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right = drawMyBullet(deadCount1, homeSurvive, enemyNumber, prop, bgMap, myTank_T1, screen, enemyBulletGroup, redEnemyGroup, greenEnemyGroup, otherEnemyGroup)
    deadCount2, homeSurvive, enemyNumber, myTank_T2.bullet.life, myTank_T2.bullet.rect.left, myTank_T2.bullet.rect.right = drawMyBullet(deadCount2, homeSurvive, enemyNumber, prop, bgMap, myTank_T2, screen, enemyBulletGroup, redEnemyGroup, greenEnemyGroup, otherEnemyGroup)
    homeSurvive, mytankGroup, deadCount1, deadCount2, moving, myTank_T1.rect.left, myTank_T1.rect.top, myTank_T1.level, myTank_T2.rect.left, myTank_T2.rect.top = drawEnemyBullet(homeSurvive, mytankGroup, deadCount1, deadCount2, enemyCouldMove, moving, bgMap, allEnemyGroup, enemyBulletGroup, screen, myTank_T1, myTank_T2)
    prop.life, enemyCouldMove, enemyNumber = drawFood(enemyNumber, enemyCouldMove, prop, bgMap, screen, allEnemyGroup, myTank_T1)
    prop.life, enemyCouldMove, enemyNumber = drawFood(enemyNumber, enemyCouldMove, prop, bgMap, screen, allEnemyGroup, myTank_T2)
    return homeSurvive, mytankGroup, deadCount1, deadCount2, switch_R1_R2_image, running_T1, running_T2, allTankGroup, enemyNumber, myTank_T1.bullet.life, myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right, myTank_T2.bullet.life, myTank_T2.bullet.rect.left, myTank_T2.bullet.rect.right, moving, myTank_T1.rect.left, myTank_T1.rect.top, myTank_T1.level, myTank_T2.rect.left, myTank_T2.rect.top, prop.life, enemyCouldMove


## @brief drawPVP.
#  @details drawPVP function draw all the necessary elements in
#  PVP mode by calling drawBG, drawBrick, drawIron, drawHome,
#  drawTank_1, drawTank_2, drawMyBulletPVP functions.
def drawPVP(homeDead, mytankGroup, deadCount1, deadCount2, switch_R1_R2_image, moving, running_T1, running_T2, bgMap, background_image, screen, delay, myTank_T1, myTank_T2, allTankGroup):
    drawBG(background_image, screen)
    drawBrick(bgMap, screen)
    drawIron(bgMap, screen)
    drawHome(bgMap, screen)
    switch_R1_R2_image, running_T1 = drawTank_1(deadCount1, switch_R1_R2_image, running_T1, delay, myTank_T1, screen)
    running_T2 = drawTank_2(deadCount2, switch_R1_R2_image, running_T2, myTank_T2, screen)
    deadCount2, myTank_T2.rect.left, myTank_T2.rect.top, myTank_T2.level, homeDead, myTank_T1.bullet.life, myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right = drawMyBulletPVP(TANK2_BORN, deadCount1, deadCount2, myTank_T2, homeDead, bgMap, myTank_T1, screen)
    deadCount1, myTank_T1.rect.left, myTank_T1.rect.top, myTank_T1.level, homeDead, myTank_T2.bullet.life, myTank_T2.bullet.rect.left, myTank_T2.bullet.rect.right = drawMyBulletPVP(TANK1_BORN, deadCount2, deadCount1, myTank_T1, homeDead, bgMap, myTank_T2, screen)
    return homeDead, mytankGroup, deadCount1, deadCount2, switch_R1_R2_image, running_T1, running_T2, allTankGroup, myTank_T1.bullet.life, myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right, myTank_T2.bullet.life, myTank_T2.bullet.rect.left, myTank_T2.bullet.rect.right, moving, myTank_T1.rect.left, myTank_T1.rect.top, myTank_T1.level, myTank_T2.rect.left, myTank_T2.rect.top


## @brief drawME.
#  @details drawME function draw all the necessary elements in
#  map editing mode by calling drawBG, drawBrick, drawIron, drawHome,
#  drawTank_1, drawBulletME functions.
def drawME(bgMap, deadCount1, mytankGroup, switch_R1_R2_image, moving, running_T1, background_image, screen, delay, myTank_T1, allTankGroup):
    drawBG(background_image, screen)
    drawBrick(bgMap, screen)
    drawIron(bgMap, screen)
    drawHome(bgMap, screen)
    switch_R1_R2_image, running_T1 = drawTank_1(deadCount1, switch_R1_R2_image, running_T1, delay, myTank_T1, screen)
    bgMap, myTank_T1, screen = drawBulletME(bgMap, myTank_T1, screen)
    return bgMap, allTankGroup, mytankGroup, switch_R1_R2_image, moving, running_T1, myTank_T1.bullet.life, myTank_T1.bullet.rect.left, myTank_T1.bullet.rect.right, myTank_T1.rect.left, myTank_T1.rect.top
