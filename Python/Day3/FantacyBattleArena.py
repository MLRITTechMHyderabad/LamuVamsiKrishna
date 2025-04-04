import random
class Character:
    def __init__(self,c_name,c_health,c_attack_power,c_defence,c_speed):
        self.c_name=c_name
        self.health=c_health
        self.attack_power=c_attack_power
        self.defence=c_defence
        self.speed=c_speed

    def attack(self,target):
        target.take_damage(self.attack_power)

    def take_damage(self,amount):
        self.health-=amount

    def is_alive(self):
        if(self.health<=0):
            return False
        return True



class Warrior(Character):
    def __init__(self, rage, c_name, c_health, c_attack_power, c_defence, c_speed):
        super().__init__(c_name, c_health, c_attack_power, c_defence, c_speed)
        self.rage=rage

    def boost_speed(self,rage):
        if rage==10:
            self.attack_power+=2
            rage-=10
    
    def benserk_mode(self):
        if self.health<=30:
            self.attack_power *=2
        else:
            self.attack_power=25

class Mage(Character):
    def __init__(self, mana,  c_name, c_health, c_attack_power, c_defence, c_speed):
        super().__init__(c_name, c_health, c_attack_power, c_defence, c_speed)
        self.mana=mana

    def fireball(self,mana):
        if mana>0:
            self.attack_power*=2
            self.health/=10




class Archer(Character):
    def __init__(self, cc,  c_name, c_health, c_attack_power, c_defence, c_speed):
        super().__init__(c_name, c_health, c_attack_power, c_defence, c_speed)
        self.cc=cc

    def precision_shot(self,cc):
        if cc:
            self.attack_power*=2


w= Warrior(0,"Thor",100,25,80,60)
m=Mage(20,"Gandalf",100,40,30,50)
a=Archer(False,"Alex",100,40,60,80)

while (w.health>0 or m.health>0 or a.health>0):
    print("while")
    if(w.health<=0 and m.health<=0):
        print("Alex (Archer) wins the battle")
        break
    elif(w.health<=0 and a.health<=0):
        print("Gandalf (mage) wins the battle")
        break
    elif(m.health<0 and a.health<=0):
        print("Thor (warrior) wins the battle")
        break
    else:
        print("no")
    if w.health<30:
        w.benserk_mode()
    if(w.attack(a)):
        w.boost_speed(w.rage)
    
    if(m.attack(w)):
        m.fireball(m.mana)
    
    if(a.attack(w)):
        a.precision_shot(a.cc)
   

    if(w.attack(m)):
        w.boost_speed(w.rage)

    if(m.attack(a)):
        m.fireball(m.mana)

    if(a.attack(m)):
        a.precision_shot(a.cc)
    
    # w.attack(m)
    # a.attack(w)
    # a.attack(m)
    # m.attack(a)
    # m.attack(w)
    
    print("warrior",w.is_alive())
    print("mage",m.is_alive())
    print("archer",a.is_alive())