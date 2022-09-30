from random import randint




class Car(object):
    pass

class Wheel(object):
    def __init__(self):
        self.orientation = randint(0, 360)

    def rotate(self, revolutions):
        degreesOfRotation = (360 * revolutions) %360
        self.orientation = (self.orientation + degreesOfRotation % 360)

class Engine(object):
    pass

class Gearbox(object):
    def __init__(self):
        self.wheels ={'FR':Wheel(), 'FL':Wheel(), 'BR':Wheel(), 'BL':Wheel()}
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
        self.clutchEnganged = False
        self.currentGear = 0

    def shiftUp(self):
        if self.currentGear < len(
                self.gears) - 1 and not self.clutchEngaged:
            self.currentGear = self.currentGear + 1

    def shiftDown(self):
        if self.currentGear > 0 and not self.clutchEngaged:
            self.currentGear = self.currentGear - 1

    def rotate(self, revolutions):
        if self.clutchEngaged:
            for wheel in self.wheels:
                self.wheels[wheel].rotate(revolutions * self.gears[self.currentGear])


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


