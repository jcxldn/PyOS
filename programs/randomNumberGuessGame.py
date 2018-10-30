import random
guess = input("Guess a number between 1 and 10!")
num = random.randint(1,11)
if guess == num:
    print("you win!")
else:
    print("you lose!")

