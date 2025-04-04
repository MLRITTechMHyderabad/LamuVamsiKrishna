class Animal:
    def __init__(self,type,no_of_legs):
        self.type=type
        self.n=no_of_legs
    def can_sleep(self):
        print("sleeping")
    def can_eat(self):
        print("eating")

class Dog(Animal):
    def __init__(self, name, breed, type, no_of_legs):
        super().__init__(type, no_of_legs)
        self.name=name
        self.breed=breed

    def can_make_sound(self):
        print("Barking")
    def can_run(self):
        print("running")

class Cat(Animal):
    def __init__(self, name, breed, type, no_of_legs):
        super().__init__(type, no_of_legs)
        self.name=name
        self.breed=breed

    def can_make_sound(self):
        print("meow meow")
    def can_run(self):
        print("running")


d=Dog("chimtu","germanshepherd","mammal",4)
c=Cat("chitti","russian","mammal",4)

print("Hierarchical Inheritence")

print(d.type)
print(d.name)
d.can_eat()
d.can_make_sound()
print("==============")
print(c.type)
print(c.name)
c.can_sleep()
c.can_make_sound()