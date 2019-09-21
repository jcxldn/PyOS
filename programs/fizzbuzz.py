# PyOS
# Made for Python 2.7
# programs/fizzbuzz.py

# Import the base application class.
from internal.baseapp import BaseApp

class App(BaseApp):
    def go(self, args):
        print(self.Colors.Bold("FizzBuzz"))

        if (len(args) >= 2):
            upto = int(args[1])
        else:
            upto = 100

        for num in range(1,upto + 1):
            string = ""
            if num % 3 == 0:
                string = string + "Fizz"
            if num % 5 == 0:
                string = string + "Buzz"
            if num % 5 != 0 and num % 3 != 0:
                string = string + str(num)
            print(string)
