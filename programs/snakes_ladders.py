import random

end = 100


def check_ladder(points):
    if points == 8:
        print 'Ladder'
        points = 26
    elif points == 21:
        print 'Ladder'
        points = 82
    elif points == 43:
        print 'Ladder'
        points = 77
    elif points == 50:
        print 'Ladder'
        points = 91
    elif points == 54:
        print 'Ladder'
        points = 93
    elif points == 62:
        print 'Ladder'
        points = 96
    elif points == 66:
        print 'Ladder'
        points = 87
    elif points == 80:
        print 'Ladder'
        points = 100
    else:
        # Not a ladder
        return points
    return points


def check_snake(points):
    if points == 44:
        print 'Snake'
        points = 22
    elif points == 46:
        print 'Snake'
        points = 5
    elif points == 48:
        print 'Snake'
        points = 9
    elif points == 52:
        print 'Snake'
        points = 11
    elif points == 55:
        print 'Snake'
        points = 7
    elif points == 59:
        print 'Snake'
        points = 17
    elif points == 64:
        print 'Snake'
        points = 36
    elif points == 69:
        print 'Snake'
        points = 33
    elif points == 73:
        print 'Snake'
        points = 1
    elif points == 83:
        print 'Snake'
        points = 19
    elif points == 92:
        print 'Snake'
        points = 51
    elif points == 95:
        print 'Snake'
        points = 24
    elif points == 98:
        print 'Snake'
        points = 28
    else:
        # Not a snake
        return points
    return points


def reached_end(points):
    return bool(points == end)


def play():
    # Input player 1 name
    p1_name = raw_input('Player 1, Please enter your name: ')
    # Input player 2 name
    p2_name = raw_input('Player 2, Please enter your name: ')
    # Initialise points of player 1
    pp1 = 0
    # Initialise points of player 2
    pp2 = 0

    turn = 0

    while(1):
        if turn % 2 == 0:
            # Player 1 turn
            print p1_name + ' your turn'
            # Ask player's choice to continue
            c = raw_input('Press 1 to continue, 0 to quit: ')
            if int(c) == 0:
                print p1_name + ' scored ' + str(pp1)
                print p2_name + ' scored ' + str(pp2)
                print 'Quitting the game, Thanks for playing'
                break
            # Generate a random number from 1, 2, 3, 4, 5, 6
            dice = random.randint(1, 6)
            print 'Dice showed: ' + str(dice)
            # Add points
            pp1 = pp1 + dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)

            # Check if the player goes beyond the board
            if pp1 > end:
                pp1 = end

            print p1_name + ' Your score: ' + str(pp1)

            if reached_end(pp1):
                print p1_name + ' won'
                break
        else:
            # Player 2 turn
            print p2_name + ' your turn'
            # Ask player's choice to continue
            c = raw_input('Press 1 to continue, 0 to quit: ')
            if int(c) == 0:
                print p1_name + ' scored ' + str(pp1)
                print p2_name + ' scored ' + str(pp2)
                print 'Quitting the game, Thanks for playing'
                break
            # Generate a random number from 1, 2, 3, 4, 5, 6
            dice = random.randint(1, 6)
            print 'Dice showed: ' + str(dice)
            # Add points
            pp2 = pp2 + dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)

            # Check if the player goes beyond the board
            if pp2 > end:
                pp2 = end

            print p2_name + ' Your score: ' + str(pp2)

            if reached_end(pp2):
                print p2_name + ' won'
                break

        turn = turn + 1


play()
