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
        return self.calculate_cost() * (self.taxpercent/100)
    
    def __str__(self):
        pass

class Candy(DessertItem):
    def __init__(self,name='bob',candyWeight=0.0,pricePerPound=0.0):
        super().__init__(name)
        self.candyWeight = candyWeight
        self.pricePerPound = pricePerPound
    
    def __repr__(self):
        return str(f"""{str(self.candyWeight)} pound(s) of {self.name}
${str(self.pricePerPound)} per pound""")
    
    def calculate_cost(self):
        return self.pricePerPound * self.candyWeight
    
    def __str__(self):
        return f"{self.name}, {self.candyWeight}lbs, ${self.pricePerPound} per pound, total cost ${self.calculate_cost()}, tax ${self.calculate_tax()}"

class Cookie(DessertItem):
    def __init__(self,name='bob',quantity=0,pricePerDozen=0.0):
        super().__init__(name)
        self.quantity = quantity
        self.pricePerDozen = pricePerDozen
    
    def __repr__(self):
        return str(f"""{str(self.quantity)} {self.name} cookie(s)
${str(self.pricePerDozen)} per dozen""")
    
    def calculate_cost(self):
        return self.pricePerDozen * (self.quantity/12)
    def __str__(self):
        return f"{self.name}, {self.quantity} cookies, ${self.pricePerDozen} per dozen, total cost ${self.calculate_cost()}, tax ${self.calculate_tax()}"

class IceCream(DessertItem):
    def __init__(self,name='bob',scoopCount=0,pricePerScoop=0.0):
        super().__init__(name)
        self.scoopCount = scoopCount
        self.pricePerScoop = pricePerScoop
    
    def __repr__(self):
        return str(f"""{str(self.scoopCount)} scoop(s) of {self.name} ice cream
${str(self.pricePerScoop)} per scoop""")
    
    def calculate_cost(self):
        return self.scoopCount * self.pricePerScoop
    
    def __str__(self):
        return f"{self.name}, {self.scoopCount} scoops, ${self.pricePerScoop} per scoop, total cost ${self.calculate_cost()}, tax ${self.calculate_tax()}"

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
        return self.pricePerScoop * self.scoopCount + self.toppingPrice
    
    def __str__(self):
        return f"{self.name}, {self.scoopCount}scoops, ${self.pricePerScoop} per scoop, topping of {self.toppingName}, topping price ${self.toppingPrice}, total cost ${self.calculate_cost()}, tax ${self.calculate_tax()}"