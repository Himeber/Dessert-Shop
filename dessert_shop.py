# imports
import random
import time
import sys

# functions
def cs():
    print('\033c')

def timeprint(text):
    punctuation = {
    "." : 0.25,
    "!" : 0.15,
    "?" : 0.15,
    "," : 0.05,
    ":" : 0.1
    }
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in punctuation:
            time.sleep(punctuation[char])
        else:
            time.sleep(random.random()/25)
    print()
    time.sleep(0.25)

def intput(text):
    while True:
        try:
            timeprint(text)
            ans = input("> ")
            return int(ans)
        except:
            timeprint("That is not a number. Try again.")

def strput(text):
    timeprint(text)
    ans = input("> ")
    return str(ans)

def line():
    return "-----------------------"

#ACTUAL CODE STARTS HERE

def main():
    order = Order()
    order.additem(Candy("Candy Corn", 1.5, .25))
    order.additem(Candy("Gummy Bears", .25, .35))
    order.additem(Cookie("Chocolate Chip", 6, 3.99))
    order.additem(IceCream("Pistachio", 2, .79))
    order.additem(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.additem(Cookie("Oatmeal Raisin", 2, 3.45))
    timeprint("Items in order:")
    print(line())
    for i in order.desserts:
        timeprint(str(i.name))
    timeprint(f"There are {len(order)} items in the order.")
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

class Order:
    def __init__(self,desserts=[]):
        self.desserts = desserts
    
    def additem(self,item):
        self.desserts.append(item)

    def __len__(self):
        return len(self.desserts)

cs()
main()