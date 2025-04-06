from abc import ABC, abstractmethod
class Chai:

    def __init__(self,n,p,s):
        self.name=n
        self.base_price=p
        self.quantity_in_stock=s

    @abstractmethod
    def calculate_price(self):
        pass
    @abstractmethod
    def display_info(self):
        pass


class MasalaChai(Chai):
    def __init__(self, n, p, s):
        super().__init__(n, p, s)
        self.extra=10
    def calculate_price(self):
        return self.base_price+self.extra
    def display_info(self):
        print("Name:",self.name,"| Price per cup:",self.calculate_price(),"| Stock",self.quantity_in_stock)


class GingerChai(Chai):
    def __init__(self, n, p, s):
        super().__init__(n, p, s)
        self.e=8
    def calculate_price(self):
        return self.base_price+self.e
    def display_info(self):
        print("Name:",self.name,"| Price per cup:",self.calculate_price(),"| Stock:",self.quantity_in_stock)

class ElaichiChai(Chai):
    def __init__(self, n, p, s):
        super().__init__(n, p, s)
        self.e=12
    def calculate_price(self):
        return self.base_price+self.e
    def display_info(self):
        print("Name:",self.name,"| Price per cup:",self.calculate_price(),"| Stock:",self.quantity_in_stock)


class Inventory:
    cc={}
    li=[]
    def add_chai(self,c):
       
        self.li.append(c)

    def show_inventory(self):
        for i in self.li:
            i.display_info()
            

    def get_total_inventory_value(self):
        total=0
        for i in self.li:
            total+=i.calculate_price()*i.quantity_in_stock
        return total




chai1=MasalaChai("masala chai",20,50)
chai2=GingerChai("Ginger Chai",18,40)
chai3=ElaichiChai("Elaichi Chai",25,30)
# chai1.display_info()

i=Inventory()
i.add_chai(chai1)
i.add_chai(chai2)
i.add_chai(chai3)

i.show_inventory()
print(i.get_total_inventory_value())