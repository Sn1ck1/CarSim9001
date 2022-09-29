from random import randint




class Car(object):


class Wheel(object):
    def __init__(self):
        self.orientation = randint(0, 360)

    def rotate(self, revolutions):
        degreesOfRotation = (360 * revolutions) %360
        self.orientation = (self.orientation + degreesOfRotation % 360)

class Engine(object):


class Gearbox(object):


class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100
    def refuel(self):
        self.contents = self.capacity
    
    def remove(self, amount):
        self.contents -= amount
        if self.contents <0:
            self.contents = 0








