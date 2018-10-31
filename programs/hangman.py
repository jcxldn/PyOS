import random, os

def get_words(file_path):
    with open(file_path) as file:
        word_list = file.read().splitlines()
        return word_list

def logger(msg=None):
    # cross-platform clears stdout
    os.system('cls' if os.name == 'nt' else 'clear')
    if msg:
        print(msg)

def print_word(word, char_left):
    for char in word:
        if char in char_left:
            print('_', end=" ")
        else:
            print('{} '.format(char), end=" ")
    print('')

def game_loop(word):
    char_count = len(word)
    char_left = list(set(word))
    attempt = 5

    logger('This word has {} letter(s)'.format(char_count))
    while attempt != 0 and len(char_left) != 0:
        print_word(word, char_left)
        print('{} attempt(s) left'.format(attempt))
        inp = input('guess character: ')
        if inp not in char_left and inp not in word:
            logger('Incorrect!!')
            attempt -= 1
        elif inp not in char_left and inp in word:
            logger('You already got that one!!')
        else:
            logger('Correct!!')
            char_left.remove(inp)

    if len(char_left) == 0:
        logger('Victory!! Of course, the word is {}'.format(word))
    else:
        logger('Lost!! The mysterious word is {}'.format(word))

def main():
    word_list = get_words('programs/words.txt')

    play = 'Y'
    while play == 'Y':
        word = random.choice(word_list)
        game_loop(word)
        play = input('Continue? (Y/n): ')
        while play != 'Y' and play != 'n':
            logger('Invalid answer!')
            play = input('Continue? (Y/n): ') 


    

main()
