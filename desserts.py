from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self,name='bob',tax_percent=7.25):
        self.name = name
        self.taxpercent = tax_percent
    
    def __repr__(self):
        return str(f"""{self.name}""")
    
    @abstractmethod
    def calculate_cost(self):
        pass
    
    def calculate_tax(self):
        return round(self.calculate_cost() * (self.taxpercent/100),2)

class Candy(DessertItem):
    def __init__(self,name='bob',candyWeight=0.0,pricePerPound=0.0):
        super().__init__(name)
        self.candyWeight = 0.0
        self.pricePerPound = 0.0
    
    def __repr__(self):
        return str(f"""{str(self.candyWeight)} pound(s) of {self.name}
${str(self.pricePerPound)} per pound""")
    
    def calculate_cost(self):
        return round(self.pricePerPound * self.candyWeight,2)

class Cookie(DessertItem):
    def __init__(self,name='bob',quantity=0,pricePerDozen=0.0):
        super().__init__(name)
        self.quantity = quantity
        self.pricePerDozen = pricePerDozen
    
    def __repr__(self):
        return str(f"""{str(self.quantity)} {self.name} cookie(s)
${str(self.pricePerDozen)} per dozen""")
    
    def calculate_cost(self):
        return round(self.pricePerDozen * (self.quantity/12),2)

class IceCream(DessertItem):
    def __init__(self,name='bob',scoopCount=0,pricePerScoop=0.0):
        super().__init__(name)
        self.scoopCount = scoopCount
        self.pricePerScoop = pricePerScoop
    
    def __repr__(self):
        return str(f"""{str(self.scoopCount)} scoop(s) of {self.name} ice cream
${str(self.pricePerScoop)} per scoop""")
    
    def calculate_cost(self):
        return round(self.scoopCount * self.pricePerScoop,2)

class Sundae(IceCream):
    def __init__(self,name='bob',scoopCount=0,pricePerScoop=0.0,toppingName="",toppingPrice=0.0):
        super().__init__(name,scoopCount,pricePerScoop)
        self.toppingName = toppingName
        self.toppingPrice = toppingPrice

    def __repr__(self):
        return str(f"""{str(self.scoopCount)} scoop(s) of {self.name} sundae
${str(self.pricePerScoop)} per scoop
Topped with {self.toppingName}
Topping costs ${str(self.toppingPrice)}""")
    
    def calculate_cost(self):
        return round(self.pricePerScoop * self.scoopCount + self.toppingPrice,2)