## @file myTankControl.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief My Tank Control Module
#  @date 03/24/2020

import pygame
from wall import Brick, Iron


## @brief Implement player1's operation.
#  @details Read player1's key pressed and do the corresponding moving,
#  @or activation of the ultimate skill.
#  @param fire_sound represents a audio file for the sound of shooting.
#  @param key_pressed represents that if the player is pressing a key.
#  @param moving represents the moving condition of the tank.
#  @param movdir1 represents the direction of player's tank.
#  @param myTank represents the player's tank.
#  @param allTankGroup represents a sprite group in pygame for all the tank.
#  @param brickGroup represents a sprite group in pygame for brick walls.
#  @param ironGroup represents a sprite group in pygame for iron walls.
#  @param running_T1 represents that player's tank is moving or not.
#  @return key_pressd represents that if the player is pressing a key.
#  @return moving represents the moving condition of the tank.
#  @return movdir1 represent the direction of of the tank.
#  @return myTank represents the player's tank.
#  @return allTankGroup represents a sprite group in pygame for all the tank.
#  @return brickGroup represents a sprite group in pygame for brick walls.
#  @return ironGroup represents a sprite group in pygame for iron walls.
#  @return running_T1 represents that player's tank is moving or not.
def operatePlayer1(fire_sound, key_pressed, moving, movdir1, myTank,
                   allTankGroup, brickGroup, ironGroup, running_T1):
    if moving:
        moving -= 1
        if movdir1 == 0:
            allTankGroup.remove(myTank)
            myTank.moveUp(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            running_T1 = True
        if movdir1 == 1:
            allTankGroup.remove(myTank)
            myTank.moveDown(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            running_T1 = True
        if movdir1 == 2:
            allTankGroup.remove(myTank)
            myTank.moveLeft(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            running_T1 = True
        if movdir1 == 3:
            allTankGroup.remove(myTank)
            myTank.moveRight(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            running_T1 = True

    if not moving:
        if key_pressed[pygame.K_w]:
            allTankGroup.remove(myTank)
            myTank.moveUp(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            moving = 7
            movdir1 = 0
            running_T1 = True
        elif key_pressed[pygame.K_s]:
            allTankGroup.remove(myTank)
            myTank.moveDown(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            moving = 7
            movdir1 = 1
            running_T1 = True
        elif key_pressed[pygame.K_a]:
            allTankGroup.remove(myTank)
            myTank.moveLeft(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            moving = 7
            movdir1 = 2
            running_T1 = True
        elif key_pressed[pygame.K_d]:
            allTankGroup.remove(myTank)
            myTank.moveRight(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            moving = 7
            movdir1 = 3
            running_T1 = True
    if key_pressed[pygame.K_j]:
        if not myTank.bullet.life:
            fire_sound.play()
            myTank.shoot()
    if key_pressed[pygame.K_k]:
        if myTank.ID == 1:
            myTank.bulletproof = True
        if myTank.ID == 2:
            if myTank.speed == 3:
                myTank.leap_start()
        if myTank.ID == 3:
            if not myTank.bullet.life \
              and not myTank.bullet2.life and myTank.bulletNotCooling:
                fire_sound.play()
                myTank.doubleBullet()
                myTank.bulletNotCooling = False
    return key_pressed, moving, movdir1, myTank, allTankGroup, brickGroup,\
        ironGroup, running_T1


## @brief Implement player2's operation.
#  @details Read player2's key pressed and do the corresponding moving,
#  @shooting or activatation of the ultimate skill.
#  @param fire_sound represents a audio file for the sound of shooting.
#  @param key_pressed represents that if the player is pressing a key.
#  @param moving2 represents the moving condition of the tank.
#  @param movdir2 represents the direction of player's tank.
#  @param myTank represents the player's tank.
#  @param allTankGroup represents a sprite group in pygame for all the tank.
#  @param brickGroup represents a sprite group in pygame for brick walls.
#  @param ironGroup represents a sprite group in pygame for iron walls.
#  @param running_T2 represents that player's tank is moving or not.
#  @return key_pressd represents that if the player is pressing a key.
#  @return moving2 represents the moving condition of the tank.
#  @return movdir2 represent the direction of of the tank.
#  @return myTank represents the player's tank.
#  @return allTankGroup represents a sprite group in pygame for all the tank.
#  @return brickGroup represents a sprite group in pygame for brick walls.
#  @return ironGroup represents a sprite group in pygame for iron walls.
#  @return running_T2 represents that player's tank is moving or not.
def operatePlayer2(fire_sound, key_pressed, moving2, movdir2, myTank,
                   allTankGroup, brickGroup, ironGroup, running_T2):
    if moving2:
        moving2 -= 1
        if movdir2 == 0:
            allTankGroup.remove(myTank)
            myTank.moveUp(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            running_T2 = True
        if movdir2 == 1:
            allTankGroup.remove(myTank)
            myTank.moveDown(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            running_T2 = True
        if movdir2 == 2:
            allTankGroup.remove(myTank)
            myTank.moveLeft(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            running_T2 = True
        if movdir2 == 3:
            allTankGroup.remove(myTank)
            myTank.moveRight(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            running_T2 = True

    if not moving2:
        if key_pressed[pygame.K_UP]:
            allTankGroup.remove(myTank)
            myTank.moveUp(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            moving2 = 7
            movdir2 = 0
            running_T2 = True
        elif key_pressed[pygame.K_DOWN]:
            allTankGroup.remove(myTank)
            myTank.moveDown(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            moving2 = 7
            movdir2 = 1
            running_T2 = True
        elif key_pressed[pygame.K_LEFT]:
            allTankGroup.remove(myTank)
            myTank.moveLeft(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            moving2 = 7
            movdir2 = 2
            running_T2 = True
        elif key_pressed[pygame.K_RIGHT]:
            allTankGroup.remove(myTank)
            myTank.moveRight(allTankGroup, brickGroup, ironGroup)
            allTankGroup.add(myTank)
            moving2 = 7
            movdir2 = 3
            running_T2 = True
    if key_pressed[pygame.K_COMMA]:
        if not myTank.bullet.life:
            fire_sound.play()
            myTank.shoot()
    if key_pressed[pygame.K_PERIOD]:
        if myTank.ID == 1:
            myTank.bulletproof = True
        if myTank.ID == 2:
            if myTank.speed == 3:
                myTank.leap_start()
        if myTank.ID == 3:
            if not myTank.bullet.life\
              and not myTank.bullet2.life and myTank.bulletNotCooling:
                fire_sound.play()
                myTank.doubleBullet()
                myTank.bulletNotCooling = False
    return key_pressed, moving2, movdir2, myTank, allTankGroup, brickGroup,\
        ironGroup, running_T2


## @brief Implement player operation in Map Editing mode.
#  @details Read player's key pressed and do the corresponding moving,
#  shooting, adding brick, adding iron.
#  @param key_pressed represents that if the player is pressing a key.
#  @param moving represents the moving condition of the tank.
#  @param movdir1 represents the direction of player's tank.
#  @param myTank represents the player's tank.
#  @param allTankGroup represents a sprite group in pygame for all the tank.
#  @param brickGroup represents a sprite group in pygame for brick walls.
#  @param ironGroup represents a sprite group in pygame for iron walls.
#  @param running_T1 represents that player's tank is moving or not.
#  @return key_pressd represents that if the player is pressing a key.
#  @return moving represents the moving condition of the tank.
#  @return movdir1 represent the direction of of the tank.
#  @return myTank represents the player's tank.
#  @return allTankGroup represents a sprite group in pygame for all the tank.
#  @return brickGroup represents a sprite group in pygame for brick walls.
#  @return ironGroup represents a sprite group in pygame for iron walls.
#  @return running_T1 represents that player's tank is moving or not.
def operatePlayerME(key_pressed, moving, movdir1, myTank,
                    allTankGroup, bgMap, running_T1):
    if moving:
        moving -= 1
        if movdir1 == 0:
            allTankGroup.remove(myTank)
            myTank.moveUp(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
            allTankGroup.add(myTank)
            running_T1 = True
        if movdir1 == 1:
            allTankGroup.remove(myTank)
            myTank.moveDown(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
            allTankGroup.add(myTank)
            running_T1 = True
        if movdir1 == 2:
            allTankGroup.remove(myTank)
            myTank.moveLeft(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
            allTankGroup.add(myTank)
            running_T1 = True
        if movdir1 == 3:
            allTankGroup.remove(myTank)
            myTank.moveRight(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
            allTankGroup.add(myTank)
            running_T1 = True

    if not moving:
        if key_pressed[pygame.K_w]:
            allTankGroup.remove(myTank)
            myTank.moveUp(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
            allTankGroup.add(myTank)
            moving = 7
            movdir1 = 0
            running_T1 = True
        elif key_pressed[pygame.K_s]:
            allTankGroup.remove(myTank)
            myTank.moveDown(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
            allTankGroup.add(myTank)
            moving = 7
            movdir1 = 1
            running_T1 = True
        elif key_pressed[pygame.K_a]:
            allTankGroup.remove(myTank)
            myTank.moveLeft(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
            allTankGroup.add(myTank)
            moving = 7
            movdir1 = 2
            running_T1 = True
        elif key_pressed[pygame.K_d]:
            allTankGroup.remove(myTank)
            myTank.moveRight(allTankGroup, bgMap.brickGroup, bgMap.ironGroup)
            allTankGroup.add(myTank)
            moving = 7
            movdir1 = 3
            running_T1 = True
    if key_pressed[pygame.K_j]:
        if myTank.rect.left > 315 and myTank.rect.top <= 315:
            x = (myTank.rect.left-3)/24
            y = (myTank.rect.top-3)/24
            brick = Brick()
            brick.rect.left = (int(x)+1)*24+3
            brick.rect.top = int(y)*24+3
            check = True
            for each in bgMap.brickGroup:
                if each.rect.left == brick.rect.left\
                  and each.rect.top == brick.rect.top:
                    check = False
            for each in bgMap.ironGroup:
                if each.rect.left == brick.rect.left\
                  and each.rect.top == brick.rect.top:
                    check = False
            if check is True:
                bgMap.brickGroup.add(brick)
        elif myTank.rect.top > 315 and myTank.rect.left <= 315:
            x = (myTank.rect.left-3)/24
            y = (myTank.rect.top-3)/24
            brick = Brick()
            brick.rect.left = int(x)*24+3
            brick.rect.top = (int(y)+1)*24+3
            check = True
            for each in bgMap.brickGroup:
                if each.rect.left == brick.rect.left\
                  and each.rect.top == brick.rect.top:
                    check = False
            for each in bgMap.ironGroup:
                if each.rect.left == brick.rect.left\
                  and each.rect.top == brick.rect.top:
                    check = False
            if check is True:
                bgMap.brickGroup.add(brick)

        elif myTank.rect.top > 315 and myTank.rect.left > 315:
            x = (myTank.rect.left-3)/24
            y = (myTank.rect.top-3)/24
            brick = Brick()
            brick.rect.left = (int(x)+1)*24+3
            brick.rect.top = (int(y)+1)*24+3
            check = True
            for each in bgMap.brickGroup:
                if each.rect.left == brick.rect.left\
                  and each.rect.top == brick.rect.top:
                    check = False
            for each in bgMap.ironGroup:
                if each.rect.left == brick.rect.left\
                  and each.rect.top == brick.rect.top:
                    check = False
            if check is True:
                bgMap.brickGroup.add(brick)
        else:
            x = (myTank.rect.left-3)/24
            y = (myTank.rect.top-3)/24
            brick = Brick()
            brick.rect.left = int(x)*24+3
            brick.rect.top = int(y)*24+3
            check = True
            for each in bgMap.brickGroup:
                if each.rect.left == brick.rect.left\
                  and each.rect.top == brick.rect.top:
                    check = False
            for each in bgMap.ironGroup:
                if each.rect.left == brick.rect.left\
                  and each.rect.top == brick.rect.top:
                    check = False
            if check is True:
                bgMap.brickGroup.add(brick)

    if key_pressed[pygame.K_k]:
        if myTank.rect.left > 315 and myTank.rect.top <= 315:
            x = (myTank.rect.left-3)/24
            y = (myTank.rect.top-3)/24
            iron = Iron()
            iron.rect.left = (int(x)+1)*24+3
            iron.rect.top = int(y)*24+3
            check = True
            for each in bgMap.ironGroup:
                if each.rect.left == iron.rect.left\
                  and each.rect.top == iron.rect.top:
                    check = False
            for each in bgMap.brickGroup:
                if each.rect.left == iron.rect.left\
                  and each.rect.top == iron.rect.top:
                    check = False
            if check is True:
                bgMap.ironGroup.add(iron)
        elif myTank.rect.top > 315 and myTank.rect.left <= 315:
            x = (myTank.rect.left-3)/24
            y = (myTank.rect.top-3)/24
            iron = Iron()
            iron.rect.left = int(x)*24+3
            iron.rect.top = (int(y)+1)*24+3
            check = True
            for each in bgMap.ironGroup:
                if each.rect.left == iron.rect.left\
                  and each.rect.top == iron.rect.top:
                    check = False
            for each in bgMap.brickGroup:
                if each.rect.left == iron.rect.left\
                  and each.rect.top == iron.rect.top:
                    check = False
            if check is True:
                bgMap.ironGroup.add(iron)
        elif myTank.rect.top > 315 and myTank.rect.left > 315:
            x = (myTank.rect.left-3)/24
            y = (myTank.rect.top-3)/24
            iron = Iron()
            iron.rect.left = (int(x)+1)*24+3
            iron.rect.top = (int(y)+1)*24+3
            check = True
            for each in bgMap.ironGroup:
                if each.rect.left == iron.rect.left\
                  and each.rect.top == iron.rect.top:
                    check = False
            for each in bgMap.brickGroup:
                if each.rect.left == iron.rect.left\
                  and each.rect.top == iron.rect.top:
                    check = False
            if check is True:
                bgMap.ironGroup.add(iron)
        else:
            x = (myTank.rect.left-3)/24
            y = (myTank.rect.top-3)/24
            iron = Iron()
            iron.rect.left = int(x)*24+3
            iron.rect.top = int(y)*24+3
            check = True
            for each in bgMap.ironGroup:
                if each.rect.left == iron.rect.left\
                  and each.rect.top == iron.rect.top:
                    check = False
            for each in bgMap.brickGroup:
                if each.rect.left == iron.rect.left\
                  and each.rect.top == iron.rect.top:
                    check = False
            if check is True:
                bgMap.ironGroup.add(iron)
    if key_pressed[pygame.K_l]:
        if not myTank.bullet.life:
            myTank.shoot()

    return key_pressed, moving, movdir1, myTank, allTankGroup,\
        bgMap, running_T1
