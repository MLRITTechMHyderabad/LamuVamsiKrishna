class Vechicle:

    def __init__(self,brand,no_of_tyres):
        self.brand = brand
        self.n = no_of_tyres
    
    def start(self):
        print("Starting")
    def stop(self):
        print("Stopped")

class Car(Vechicle):
    def __init__(self, name, color, brand, no_of_tyres):
        super().__init__(brand, no_of_tyres)
        self.name = name
        self.color = color
    
    def can_travel(self):
        print("tavelling")
    def can_stunt(self):
        print("drifting")

class Innova(Car):
    def __init__(self, max_speed, ac, name, color, brand, no_of_tyres):
        super().__init__(name, color, brand, no_of_tyres)
        self.ms=max_speed
        self.ac=ac

    def can_sit(self):
        print("stting")
    def can_sleep(self):
        print("sleeping")


print("Multi Level Inheritence")

c=Innova(230,True,"Innova","white","Toyota",4)
print(c.brand)
print(c.name)
print(c.ac)
c.start()
c.can_travel()
c.can_sleep()

