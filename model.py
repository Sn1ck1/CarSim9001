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
    def __init__(self):
        self.wheels ={'FR':Wheel(), 'FL':Wheel(), 'BR':Wheel(), 'BL':Wheel()}
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
        self.clutchEnganged = False
        self.currentGear = 0

    def shiftUp(self, currentGear):
        self.currentGear += currentGear
        if self.currentGear >6:
            self.currentGear = 6
        elif self.currentGear <6:
            self.currentGear = +1


    def shiftDown(self,currentGear):
        self.currentGear -= currentGear
        if self.currentGear <0:
            self.currentGear = 0
        elif self.currentGear >0:
            self.currentGear = -1


    def rotate(self, revolutions):
        if self.clutchEnganged:
            for Wheel in self.wheels:
                self.wheels[Wheel].rotate(revolutions * self.gears[self.currentGear])


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








