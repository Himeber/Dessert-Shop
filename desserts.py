class DessertItem:
    def __init__(self,name='bob'):
        self.name = name
    def __repr__(self):
        return str(f"""{self.name}""")

class Candy(DessertItem):
    def __init__(self,name='bob',candyWeight=0.0,pricePerPound=0.0):
        super().__init__(name)
        self.candyWeight = 0.0
        self.pricePerPound = 0.0
    def __repr__(self):
        return str(f"""{str(self.candyWeight)} pound(s) of {self.name}
${str(self.pricePerPound)} per pound""")

class Cookie(DessertItem):
    def __init__(self,name='bob',quantity=0,pricePerDozen=0.0):
        super().__init__(name)
        self.quantity = quantity
        self.pricePerDozen = pricePerDozen
    def __repr__(self):
        return str(f"""{str(self.quantity)} {self.name} cookie(s)
${str(self.pricePerDozen)} per dozen""")

class IceCream(DessertItem):
    def __init__(self,name='bob',scoopCount=0,pricePerScoop=0.0):
        super().__init__(name)
        self.scoopCount = scoopCount
        self.pricePerScoop = pricePerScoop
    def __repr__(self):
        return str(f"""{str(self.scoopCount)} scoop(s) of {self.name} ice cream
${str(self.pricePerScoop)} per scoop""")

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
