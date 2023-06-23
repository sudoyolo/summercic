#POOP stands for Python Object Oriented Programming

class Poop:
    def __init__(self,gender,vacancy,floor):
        self.gender = gender
        self.vacancy = vacancy
        self.floor = floor

    def vac(self):
        print("This bathroom is {}.".format(self.vacancy))

    def gen(self):
        print("This is a {}'s bathroom.".format(self.gender))

    def flr(self):
        print("This bathroom is on floor {}.".format(self.floor))