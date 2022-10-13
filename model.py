from random import randint

class Car(object):
    def __init__(self):
        self.theEngine = Engine()

    def updateMoldel(self, dt):
        self.theEngine.updateModel(dt)

class Wheel(object):
    def __init__(self):
        self.orientation = randint(0, 360)

    def rotate(self, revolutions):
        degreesOfRotation = 360 * revolutions
        self.orientation = (self.orientation + degreesOfRotation) % 360

class Engine(object):

    def __init__(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRPM = 0
        self.consumptionRate = 0.0025
        self.maxRPM = 100
        self.theTank = Tank()

    def updateModel(self,dt):
        if self.theTank.contents > 0:
            self.currentRPM = self.throttlePosition * self.maxRPM
            self.theTank.remove(
                self.currentRPM * self.consumptionRate)
            self.theGearbox.rotate(
                self.currentRPM * (dt / 60))
        else:
            self.currentRPM = 0


class Gearbox(object):
    def __init__(self):
        self.wheels ={'FR':Wheel(), 'FL':Wheel(), 'BR':Wheel(), 'BL':Wheel()}
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
        self.clutchEngaged = False
        self.currentGear = 0

    def shiftUp(self):
        if self.currentGear < len(
                self.gears) - 1 and not self.clutchEngaged:
            self.currentGear += 1

    def shiftDown(self):
        if self.currentGear > 0 and not self.clutchEngaged:
            self.currentGear -= 1

    def rotate(self, revolutions):
        if self.clutchEngaged:
            newRevs = revolutions * self.gears[self.currentGear]
            for wheel in self.wheels:
                self.wheels[wheel].rotate(newRevs)


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


