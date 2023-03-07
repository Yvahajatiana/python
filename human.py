class Person:
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName

    def getFullName(self):
        return self.__firstName + " " + self.__lastName

    def showFullName(self):
        print(self.getFullName())

    def __del__(self):
        print('instance deleted')


class Programmer(Person):
    def __init__(self, firstName, lastName):
        Person.__init__(self, firstName, lastName)

    def setLanguage(self, language):
        self.__language = language

    def getProgrammerInformation(self):
        return self.getFullName() + " work with language: " + self.__language

    def showProgrammerInformation(self):
        print(self.getProgrammerInformation())
