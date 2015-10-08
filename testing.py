import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screenSize = [400, 500]
def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((screenSize[0], screenSize[1]))
    pygame.display.set_caption("Pong!")

    # Ball Speed [x, y]
    ballSpeed = [5, 2]
    ballRadius = 5

    # Paddle size [width, height]
    paddle = [10, 200]
    LPaddlePosition = (50, int(screenSize[1]/2 - paddle[1]/2), paddle[0], paddle[1])
    RPaddlePosition = (screenSize[0]-50-paddle[0], int(screenSize[1]/2 - paddle[1]/2), paddle[0], paddle[1])

    # Center of the screen
    ballPosition = [int(800/2 - ballRadius), int(500/2 - ballRadius)]

    # Draw the circle
    ball = pygame.draw.circle(screen, WHITE, ballPosition, ballRadius, 0)
    leftPaddle = pygame.draw.rect(screen, WHITE, LPaddlePosition)
    rightPaddle = pygame.draw.rect(screen, WHITE, RPaddlePosition)
    pygame.display.update()

    while (True):
        #Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Shut down pygame
                pygame.quit()
                #Shut down the program
                sys.exit()

        update(screen, ballPosition, ballRadius, ball, LPaddlePosition, RPaddlePosition, ballSpeed)
        msElapsed = clock.tick(60)
        pygame.display.update()

def update(screen, ballPosition, ballRadius, ball, LPaddlePosition, RPaddlePosition, speed):
    #print(ballPosition)
    ballLeft = ballPosition[0] - ballRadius
    ballRight = ballPosition[0] + ballRadius
    ballTop = ballPosition[1] - ballRadius
    ballBottom = ballPosition[1] + ballRadius

    if (ballLeft <= 0 or ballRight >= screenSize[0]):
        speed[0] = -speed[0]
    if (ballTop <= 0 or ballBottom >= screenSize[1]):
        speed[1] = -speed[1]
    #print(RPaddlePosition)
    #Bouncing the ball on the right paddle when moving to the right but not when moving from behind the paddle
    if ((speed[0] > 0) and (ballRight >= RPaddlePosition[0])and (ballTop >= RPaddlePosition[1])and(ballBottom <= (RPaddlePosition[1]+RPaddlePosition[3]))):
        speed[0] = -speed[0]

    #Bouncing the ball on the left paddle when moving to the left but not when moving from behind the paddle
    if ((speed[0] < 0) and (ballLeft <= LPaddlePosition[0]+LPaddlePosition[2])and (ballTop >= LPaddlePosition[1])and(ballBottom <= (LPaddlePosition[1]+LPaddlePosition[3]))):
                speed[0] = -speed[0]

    ballPosition[0] = ballPosition[0] + speed[0]
    ballPosition[1] = ballPosition[1] + speed[1]
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, WHITE, ballPosition, ballRadius, 0)
    pygame.draw.rect(screen, WHITE, LPaddlePosition)
    pygame.draw.rect(screen, WHITE, RPaddlePosition)

main()
