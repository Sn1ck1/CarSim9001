from random import randint

class Car(object):
    def init(self):
        self.theEngine = Engine()


    def updateModel(self, dt):
        self.theEngine.updatemodel(dt)


class Wheel(object):
    def init(self):
        self.orientation = randint(0,360)

    def rotate(self, revolutions):
        degreesOfRotation = 360 * revolutions
        self.orientation = (self.orientation + degreesOfRotation) %360
class Engine(object):

    def init(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()

    def updateModel(self, dt):
        if  self.theTank.contents > 0 :
            self.currentRpm = self.throttlePosition * self.maxRpm
            self.theTank.remove(
                self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(
                self.currentRpm * (dt/60))
        else:
            self.currentRpm = 0
class Gearbox(object):
    def shiftUp(self):
        if self.currentGear < len(self.gears) - 1 and not self.clutchEngaged:
            self.currentGear +=1

    def shiftDown(self):
        if self.currentGear > 0 and not self.clutchEngaged:
            self.currentGear -= 1

    def rotate(self,revolutions):
        if self.clutchEngaged:
            newRevs = revolutions * self.gears[self.currentGear]
            for wheel in self.wheels:
                self.wheels[wheel].rotate(newRevs)
def init(self):
        self.wheels = {}
        for newWheel in ['frontLeft', 'frontRight','rearLeft', 'rearRight']:
            self.wheels[newWheel] = Wheel()
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
        self.clutchEngaged = False
        self.currentGear = 0
