import pygame
import random


# Initialise functions
pygame.init()
#pygame.font.init()
myFont1 = pygame.font.SysFont("monospace", 20)
myFont2 = pygame.font.SysFont("comicsansms", 36)
# Open a new window
wind = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")

# Initialise parameters
def initGame():
    headPosX = 100
    headPosY = 100
    vel = 20
    velX = vel
    velY = 0
    loopTime = 2
    loopTimer = 0
    r = 10
    step = 20
    speed = 10
    ctrP1 = [0, 0, 0, 0]
    bodyPosX = []
    bodyPosY = []
    foodEaten = True
    foodPosX = []
    foodPosY = []
    bodyLength = 5
    gameOver = False
    return headPosX, headPosY, vel, velX, velY, loopTimer, loopTime, r, step, speed, ctrP1, bodyPosX, bodyPosY, foodEaten, foodPosX, foodPosY, bodyLength, gameOver

headPosX, headPosY, vel, velX, velY, loopTimer, loopTime, r, step, speed, ctrP1, bodyPosX, bodyPosY, foodEaten, foodPosX, foodPosY, bodyLength, gameOver = initGame()
run = True
# Main loop
while run:
    pygame.time.delay(loopTime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    loopTimer += loopTime
    # ----------------------------------Detect the key pressed------------------------------------------#
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        #print("left")
        ctrP1 = [1, 0, 0, 0]
    if keys[pygame.K_RIGHT]:
        #print("right")
        ctrP1 = [0, 1, 0, 0]
    if keys[pygame.K_UP]:
        #print("up")
        ctrP1 = [0, 0, 1, 0]
    if keys[pygame.K_DOWN]:
        #print("down")
        ctrP1 = [0, 0, 0, 1]
    #------------------------------------------------------------Game Loop----------------#
    # The game iteration loop
    if loopTimer >= 1000/speed and (gameOver is False):
        loopTimer = 0  # Reset game loop clock
        #  Calculate new speed in terms of bodyLength
        speed = 9 + int(bodyLength/5)
        # if bodyLength <= 5:
        #     speed = 5
        # elif bodyLength <= 6:
        #     speed = 7
        # elif bodyLength <= 7:
        #     speed = 10
        # else:
        #     speed = 50


        #  Change moving speed & direction with the key pressed
        if ctrP1 == [1, 0, 0, 0]:
            ctrP1 = [0, 0, 0, 0]  # Reset key pressed
            if velX != vel:  # Not to move back
                velX = -vel
                velY = 0
        if ctrP1 == [0, 1, 0, 0]:
            ctrP1 = [0, 0, 0, 0]
            if velX != -vel:
                velX = +vel
                velY = 0
        if ctrP1 == [0, 0, 1, 0]:
            ctrP1 = [0, 0, 0, 0]
            if velY != vel:
                velX = 0
                velY = -vel
        if ctrP1 == [0, 0, 0, 1]:
            ctrP1 = [0, 0, 0, 0]
            if velY != -vel:
                velX = 0
                velY = +vel
        # Update the head position in terms of the velocity & direction
        headPosX += velX
        headPosY += velY

        # Remove the tails out of body length
        if len(bodyPosY) > bodyLength:
            bodyPosX.remove(bodyPosX[0])
            bodyPosY.remove(bodyPosY[0])

        # scroll the screen
        if headPosX > 500:
            headPosX = headPosX - 500
        elif headPosX < 0:
            headPosX = headPosX + 500
        if headPosY > 500:
            headPosY = headPosY - 500
        elif headPosY < 0:
            headPosY = headPosY + 500

        # Bodylength grows if the food is eaten
        if foodPosX == headPosX and foodPosY == headPosY:
            foodEaten = True
            bodyLength += 1

        # Create a food if food is eaten
        if foodEaten == True:
            foodPosX = random.randint(1, 24) * step
            foodPosY = random.randint(1, 24) * step
            foodEaten = False

        # Paint the screen black
        #wind.fill((141, 185, 216))
        wind.fill((0, 0, 0))
        # Draw food
        pygame.draw.circle(wind, (255, 255, 0), (foodPosX, foodPosY), r)
        # Draw Body
        for i in range(len(bodyPosX)):
            pygame.draw.circle(wind, (0, 0, 255), ((int(bodyPosX[i])), int(bodyPosY[i])), r)
        # Draw head
        pygame.draw.circle(wind, (255, 0, 0), ((int(headPosX)), int(headPosY)), r)

        print(headPosX, headPosY) #for debug
        print(bodyPosX, bodyPosY)   #for debug

        # Decide game over, if head collides body
        if gameOver == False and bodyPosX != []:
            for i in range(len(bodyPosX)):
                if (bodyPosX[i] == headPosX) and (bodyPosY[i] == headPosY):
                    gameOver = True


        # Display Score & Speed
        scoreText = myFont1.render("Score:" + str(bodyLength), 1, (255, 255, 255))
        wind.blit(scoreText, [380, 35])
        speedText = myFont1.render("Speed:" + str(speed), 1, (255, 255, 255))
        wind.blit(speedText, [380, 10])

        # Include head as a part of body
        bodyPosX.append(headPosX)
        bodyPosY.append(headPosY)
        # Update display
        pygame.display.update()


    #-----------------------post-gameOver loop---------------#
    if loopTimer >= 100 and (gameOver is True):
        mousePos = pygame.mouse.get_pos()
        gameOverText = myFont2.render("Game Over", 1, (255, 63, 63))
        if mousePos[0] in range(172,299) and mousePos[1] in range(294, 322):
            restartText = myFont2.render("Restart", 1, (255, 63, 255))
        else:
            restartText = myFont2.render("Restart", 1, (255, 255, 63))
        wind.blit(gameOverText, [150, 230])
        wind.blit(restartText, [170, 280])


        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if pressed1 and mousePos[0] in range(172,299) and mousePos[1] in range(294, 322):
            headPosX, headPosY, vel, velX, velY, loopTimer, loopTime, r, step, speed, ctrP1, bodyPosX, bodyPosY, foodEaten, foodPosX, foodPosY, bodyLength, gameOver = initGame()

        pygame.display.update()


pygame.QUIT

"""Version 0.2. I have add restart function using button click"""