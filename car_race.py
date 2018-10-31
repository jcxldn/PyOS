import pygame as pg
import time
import random

pg.init()

crash_sound = pg.mixer.Sound("Crash_Sounds.wav")
pg.mixer.music.load("Pagani_zonda.wav")

display_width = 800
display_height = 600

car_width = 70

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
blue = (0,0,255)
green = (0,200,0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption("car race")
clock = pg.time.Clock()

carImg = pg.image.load('car.png')
pause = False

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface ,textSurface.get_rect()



def message_display(text):
    beauty_text = pg.font.Font('freesansbold.ttf',115)
    TextSurf, TextRact = text_object(text , beauty_text)
    TextRact.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRact)
    pg.display.update()
    time.sleep(2)
    gameloop()

def crash():

    pg.mixer.music.stop()
    pg.mixer.Sound.play(crash_sound)

    beauty_text = pg.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRact = text_object("You Crashed", beauty_text)
    TextRact.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRact)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameQuit()

        # button(msg, x, y, w, h, ac, ic):
        button("Replay", 150, 450, 100, 50, bright_green, green, gameloop)
        button("Quit", 550, 450, 100, 50, bright_red, red, gameQuit)

        pg.display.update()
        clock.tick(15)

def gameQuit():
    pg.quit()
    quit()

def enemy_dodged(count):
    font = pg.font.SysFont(None, 25)
    text = font.render("Dodged : "+str(count), True, black)
    gameDisplay.blit(text, (5,5))

def enemy(enemy_x ,enemy_y, enemy_w, enemy_h, color):
    pg.draw.rect(gameDisplay, color, [enemy_x, enemy_y, enemy_w, enemy_h])

def button(msg, x, y, w, h, ac, ic, action = None):
    mouse = pg.mouse.get_pos()

    click = pg.mouse.get_pressed()

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pg.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pg.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = (x + (w / 2), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause

    pg.mixer.music.unpause()

    pause = False

def paused():

    pg.mixer.music.pause()


    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameQuit()
        gameDisplay.fill(white)
        beauty_text = pg.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRact = text_object("Paused", beauty_text)
        TextRact.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRact)

        #button(msg, x, y, w, h, ac, ic):
        button("continue", 150, 450, 100, 50, bright_green, green, unpause)
        button("Quit", 550, 450, 100, 50, bright_red, red, gameQuit)

        pg.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameQuit()
        gameDisplay.fill(white)
        beauty_text = pg.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRact = text_object("Race Game", beauty_text)
        TextRact.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRact)

        #button(msg, x, y, w, h, ac, ic):
        button("GO!", 150, 450, 100, 50, bright_green, green, gameloop)
        button("Quit", 550, 450, 100, 50, bright_red, red, gameQuit)

        pg.display.update()
        clock.tick(15)

def gameloop():

    pg.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change=0

    enemy_startx = random.randrange(0,display_width-100)
    enemy_starty = -600
    enemy_speed = 8
    enemy_width = 100
    enemy_hight = 100

    dodged_object = 0
    increment = 0
    counter = 0
    global pause

    gameExit = False

    while not gameExit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameQuit()
            #print(event)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -(10+increment)
                if event.key == pg.K_RIGHT:
                    x_change = (10+increment)
                if event.key == pg.K_p:
                    pause = True
                    paused()
            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                    x_change = 0


        x += x_change
        gameDisplay.fill(white)

        #def enemy(enemy_x, enemy_y, enemy_w, enemy_h, color):
        enemy(enemy_startx, enemy_starty, enemy_width, enemy_hight, black)
        enemy_starty += enemy_speed

        car(x,y)
        enemy_dodged(dodged_object)

        if x>display_width-car_width or x<0:
            crash()

        if enemy_starty > display_height:
            enemy_starty = 0 - enemy_hight
            enemy_startx = random.randrange(0,display_width-enemy_width)
            dodged_object += 1
            counter += 1
            if counter == 5:
                if enemy_speed < 12:
                    enemy_speed += 1
                    increment += .5
                if enemy_width < 250:
                    enemy_width += 3
                counter = 0


        if y < enemy_starty + enemy_hight:
            if x+car_width > enemy_startx and x < enemy_startx + enemy_width:
                crash()


        pg.display.update()
        clock.tick(60)
game_intro()
gameloop()
gameQuit()