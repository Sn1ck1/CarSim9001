from random import randint

class Car(object): # en class så man kan refere til de forskellige elementer.
    def __init__(self): # initiere klassen car så man kan kalde den ved hjælp af "self."
        self.theEngine = Engine() # kalder Engine

    def updateModel(self, dt):
        self.theEngine.updateModel(dt) # Updatere Engine med nye værdier

class Wheel(object):
    def __init__(self):
        self.orientation = randint(0, 360) # sætter orientation til er tilfældigt nummer mellem 0 og 360

    def rotate(self, revolutions):
        degreesOfRotation = 360 * revolutions
        self.orientation = (self.orientation + degreesOfRotation) % 360 # rotere hjulet med en hvis hastighed.

class Engine(object):

    def __init__(self):
        self.throttlePosition = 0 # throttle 1 eller 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0 # deafault = 0
        self.consumptionRate = 0.0025 # en konstant som styrer hvor meget bilen skal bruge af benzin.
        self.maxRPM = 100 # sætter et maximum for hastigheden
        self.theTank = Tank()

    def updateModel(self,dt): # selve kernekoden af bilen. Denne function sørger for at det hel virker
        if self.theTank.contents > 0: # hvis tankens indhold er højere end 0 skal bilen kunne køre
            self.currentRpm = self.throttlePosition * self.maxRPM # sætter currentRpm til throttlePosition * maxRPM
            self.theTank.remove(
                self.currentRpm * self.consumptionRate) # fjerner hvor meget der er i tanken ved at gange currentRpm med konstanten consumptionRate.
            self.theGearbox.rotate(
                self.currentRpm * (dt / 60)) # rotere gearbox med hvor mange gange der opdateres
        else:
            self.currentRpm = 0 # hvis brændstof er = 0 så set currentrpm til 0


class Gearbox(object):
    def __init__(self):
        self.wheels ={'frontRight': Wheel(), 'frontLeft': Wheel(), 'rearRight': Wheel(), 'rearLeft': Wheel()} #laver en instans med fire hjul
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8] # laver en instans med alle gear, disse gear bliver ganget i Gearbox
        self.clutchEngaged = False # sætter clutch til false-
        self.currentGear = 0 # sætter currentgear til 0

    def shiftUp(self):
        if self.currentGear < len(
                self.gears) - 1 and not self.clutchEngaged: # hvis gear værdien er under det maksimale gear i gears array
            self.currentGear += 1 # så skal der lægget 1 til current gear

    def shiftDown(self):
        if self.currentGear > 0 and not self.clutchEngaged: # hvis currentgear er større end det minimale gear i array
            self.currentGear -= 1 # så skal der trækkes 1 fra currentGear

    def rotate(self, revolutions):
        if self.clutchEngaged: # hvis clutch værdien er sand,
            newRevs = revolutions * self.gears[self.currentGear] # så skal hver hjul
            for wheel in self.wheels:
                self.wheels[wheel].rotate(newRevs) # rotere ganget med gear ratioen


class Tank(object):

    def __init__(self):
        self.capacity = 100 # sætter max på hvor meget der kan være i tanken til 100
        self.contents = 100 # sætter hvor meget der i tanken når bilen startes første gang til 100
    def refuel(self):
        self.contents = self.capacity # funktion som refueler contents til capacity altså max
    
    def remove(self, amount):
        self.contents -= amount # fjerner brændstof
        if self.contents <0: # hvis contents er laver end nul så skal 0 returnere ligemeget hvad
            self.contents = 0 # ekstra beskyttelse så værdier ikke overflower og skaber problemer i programmet


