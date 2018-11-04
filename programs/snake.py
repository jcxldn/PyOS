# PyOS
# Made for Python 2.7
# internal/programs/snake.py

# Import Libraries
from random import SystemRandom

# Import PyGame with sdout disabled
import os
import sys
with open(os.devnull, 'w') as f:
    # Disable Stdout
    oldstdout = sys.stdout
    sys.stdout = f
    # Import PyGame
    import pygame
    # Enable Stdout
    sys.stdout = oldstdout

# Snake Class
class Snake():

    def init(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirectionOfSnake(self, direction):
        if direction == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if direction == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if direction == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if direction == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, foodPos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10

        self.body.insert(0, list(self.position))
        if self.position == foodPos:
            return True
        else:
            self.body.pop()

    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return True
        elif self.position[1] > 490 or self.position[1] < 0:
            return True

        # For body part in tail
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return True
        return False

    def getHeadPos(self):
        return self.position

    def getBody(self):
        return self.body

# Food class
class Food():

    cryptogen = SystemRandom()

    def init(self):
        self.position = [self.cryptogen.randrange(1, 50)*10, self.cryptogen.randrange(1, 50)*10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if (not self.isFoodOnScreen):
            self.position = [self.cryptogen.randrange(1, 50)*10, self.cryptogen.randrange(1, 50)*10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self, result):
        self.isFoodOnScreen = result

# Launcher Class
class Launcher:

    # Initialise global variables for display properties
    def init(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Hacktoberfest Snake Game")
        self.fps = pygame.time.Clock()
        self.score = 0

        self.snake = Snake()
        self.snake.init()

        self.food = Food()
        self.food.init()

    def start(self):
        try:
            while True:
                for event in pygame.event.get():
                    self.check_events(event)

                foodPos = self.food.spawnFood()
                if (self.snake.move(foodPos)):
                    self.score += 1
                    self.food.setFoodOnScreen(False)

                self.window.fill(pygame.Color(0, 255, 0))
                for pos in self.snake.getBody():
                    pygame.draw.rect(self.window, pygame.Color(255, 0, 0), pygame.Rect(pos[0], pos[1], 10, 10))
                    pygame.draw.rect(self.window, pygame.Color(100, 100, 100), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

                if (self.snake.checkCollision()):
                    gameOver()

                pygame.display.set_caption("HacktoberFest Snake Game | Score: " + str(self.score))
                pygame.display.flip()
                self.fps.tick(24)
        except Exception:
            pass

    def check_events(self, event):
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.snake.changeDirectionOfSnake('RIGHT')
            if event.key == pygame.K_UP:
                self.snake.changeDirectionOfSnake('UP')
            if event.key == pygame.K_DOWN:
                self.snake.changeDirectionOfSnake('DOWN')
            if event.key == pygame.K_LEFT:
                self.snake.changeDirectionOfSnake('LEFT')


# Main Function, where we initialise game.
def app():
    launcher = Launcher()
    launcher.init()
    launcher.start()

# Gameover function, outside any class structure.
def gameOver():
    pygame.quit()
    print("Ouch!, Game Over!")
    # sys.exit()


if __name__ == "__main__":
    app()
