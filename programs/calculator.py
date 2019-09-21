# PyOS
# Made for Python 2.7
# programs/calculator.py

# Import Libraries
# PyOS Scripts
import internal.extra
import internal.runCommand

# Variables

appName = ("Calculator")
validModes = (["a", "s", "m", "d"])

from internal.baseapp import BaseApp

class App(BaseApp):
    def go(self):
        self.clear()
        print(internal.extra.colors.BOLD + internal.extra.notes.name + " " + appName + internal.extra.colors.ENDC)
        self.__modeselect()

    def __modeselect(self):
        print(internal.extra.colors.OKGREEN + "Choose a mode" + internal.extra.colors.ENDC)
        print(internal.extra.colors.OKBLUE + "(A)dd - (S)ubtract - (M)ultiply - (D)ivide - (E)xit" + internal.extra.colors.ENDC)
        choice = raw_input("Mode > ").lower()
        if choice in validModes:
            number1 = raw_input("First Number > ")
            number2 = raw_input("Second Number > ")
            print(self.__calculate(choice, number1, number2))
            self.__modeselect()
        else:
            if choice == "e":
                return
            self.__modeselect()

    def __calculate(self, mode, number1, number2):
        if (mode == "a"):
            return number1 + " + " + number2 + " = " + str(modulo.add(float(number1), float(number2)))

        if (mode == "s"):
            return number1 + " - " + number2 + " = " + str(modulo.subtract(float(number1), float(number2)))

        if (mode == "m"):
            return number1 + " * " + number2 + " = " + str(modulo.multiply(float(number1), float(number2)))

        if (mode == "d"):
            return number1 + " / " + number2 + " = " + str(modulo.divide(float(number1), float(number2)))


class modulo:
    @staticmethod
    def add(x, y):
        return (x + y)

    @staticmethod
    def subtract(x, y):
        return (x - y)

    @staticmethod
    def multiply(x, y):
        return (x * y)

    @staticmethod
    def divide(x, y):
        return (x / y)
