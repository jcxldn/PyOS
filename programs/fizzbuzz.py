# PyOS
# Made for Python 2.7
# programs/fizzbuzz.py

# Import Libraries
# PyOS Scripts
import internal.extra

def app():
    print(internal.extra.colors.BOLD + "FizzBuzz" + internal.extra.colors.ENDC)
    upto = int(raw_input("Up to number [int]: "))
    for num in range(1,upto + 1):
        string = ""
        if num % 3 == 0:
            string = string + "Fizz"
        if num % 5 == 0:
            string = string + "Buzz"
        if num % 5 != 0 and num % 3 != 0:
            string = string + str(num)
        print(string)
