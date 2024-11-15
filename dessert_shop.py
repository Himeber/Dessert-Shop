# imports
import random
import time
import sys
from desserts import (
    DessertItem,
    IceCream,
    Sundae,
    Cookie,
    Candy
)
from receipt_maker import *
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
class Order:
    def __init__(self,desserts=[]):
        self.desserts = desserts
    
    def additem(self,item):
        self.desserts.append(item)

    def __len__(self):
        return len(self.desserts)
    
    def order_cost(self):
        total = 0.0
        for dessert in self.desserts:
            total += dessert.calculate_cost()
        return total

    def order_tax(self):
        total = 0.0
        for dessert in self.desserts:
            total += dessert.calculate_tax()
        return total

  
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
    data = [ 
    ["Name", "Price", "Tax" ]]
    for item in order.desserts:
        data.append([item.name, '$' + str(round(item.calculate_cost(),2)), '$' + str(round(item.calculate_tax(),2))])
    data.append([ "Subtotal", '$' +str(round(order.order_cost(),2)), '$' +str(round(order.order_tax(),2))])
    data.append([ "Total", "", '$' +str(round(order.order_cost() + order.order_tax(),2))])
    data.append(["Total items in the order","",str(len(order))])
    make_receipt(data,'receipt.pdf')


cs()
main()