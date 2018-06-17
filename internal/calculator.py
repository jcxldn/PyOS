# PyOS
# Made for Python 2.7
# internal/calculator.py

# Import Libraries

import extra
# PyOS Scripts
import runCommand

# Variables

appName = ("Calculator")
validModes = (["a", "s", "m", "d"])

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

def start():
    runCommand.commands.clear()
    print(extra.colors.BOLD + extra.notes.name + " " + appName + extra.colors.ENDC)
    modeSelect()

def modeSelect():
    print(extra.colors.OKGREEN + "Choose a mode" + extra.colors.ENDC)
    print(extra.colors.OKBLUE + "(A)dd - (S)ubtract - (M)ultiply - (D)ivide - (E)xit" + extra.colors.ENDC)
    choice = raw_input("Mode > ").lower()
    if choice in validModes:
        number1 = raw_input("First Number > ")
        number2 = raw_input("Second Number > ")
        print(calculate(choice, number1, number2))
    else:
            if choice == "e":
                return
            modeSelect()

def calculate(mode, number1, number2):
    if (mode == "a"):
        return number1 + " + " + number2 + " = " + str(modulo.add(float(number1), float(number2)))

    if (mode == "s"):
        return number1 + " - " + number2 + " = " + str(modulo.subtract(float(number1), float(number2)))

    if (mode == "m"):
        return number1 + " * " + number2 + " = " + str(modulo.multiply(float(number1), float(number2)))

    if (mode == "d"):
        return number1 + " / " + number2 + " = " + str(modulo.divide(float(number1), float(number2)))