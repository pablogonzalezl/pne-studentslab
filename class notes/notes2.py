#20/2 inheritance
class Vehicle:
    def set_speed(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed=0): #speed is optional o algo así ha dicho
        self.car_brand = brand
        self.speed = speed

class Ferrari(Car): #esto es la inheritance supongo
    def __init__(self):
        #call the innit of the mother class
        super().__init__("Ferrari",100)
        self.music = "classic"
    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "Wow"

mycar= Car("Renault")
yourcar = Ferrari() #--> __init__
print(yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)

print(yourcar.make_cabrio(), "and music is", yourcar.music, "and speed is", yourcar.speed)
