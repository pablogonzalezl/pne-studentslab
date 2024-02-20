#20/2 classes
class Car:
    def __init__(self, brand): #when we move from class to object we use the init method
        self.brand = brand #this is a special variable attached to the object called atribute (la de self.brand, la otra es una variable normal)
        self.speed = 0
        #brand += "TM"
    def set_speed(self, speed):
        self.speed = speed
        #self.brand += "TM"
    def get_speed(self):
        return self.speed


mycar = Car("Renault", 30)
mycar.get_speed(80)
print(mycar.speed)


yourcar = Car("Ferrari", 250)
print(yourcar.speed) #this is the preferred way in python
