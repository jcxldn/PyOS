class Colors:
    # Define Colors
    __light_blue = '\033[94m'
    __light_green = '\033[92m'
    __light_yellow = '\033[93m'
    __light_red = '\033[91m'
    __reset = '\033[0m'
    __bold = '\033[1m'
    __underlined = '\033[4m'

    # Color Message Functions
    def Blue(self, msg):
        return self.__light_blue + msg + self.__reset

    def Green(self, msg):
        return self.__light_green + msg + self.__reset

    def Yellow(self, msg):
        return self.__light_yellow + msg + self.__reset

    def Red(self, msg):
        return self.__light_red + msg + self.__reset

    def Bold(self, msg):
        return self.__bold + msg + self.__reset

    def Underlined(self, msg):
        return self.__underlined + msg + self.__reset

    # Alternate name functions
    def OK(self, msg):
        return self.Green(msg)

    def Warning(self, msg):
        return self.Yellow(msg)

    def Error(self, msg):
        return self.Red(msg)
