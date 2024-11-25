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
    
    def add(self,item):
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
    
    def __str__(self):
        returner = "Order:"
        for item in self.desserts:
            returner += "\n"
            returner += str(item)
        return returner

class DessertShop:
    def __init__(self,order=None):
        self.order = order
    
    def user_prompt_candy(self):
        name = strput("Enter the type of candy.")
        cost = float(strput("Enter the cost per pound."))
        amount = float(strput("Enter the amount of candy in pounds."))
        return Candy(name,amount,cost)
    
    def user_prompt_cookie(self):
        name = strput("Enter the type of cookie.")
        cost = float(strput("Enter the cost per dozen."))
        amount = intput("Enter the amount of cookies.")
        return Cookie(name,amount,cost)
    
    def user_prompt_icecream(self):
        name = strput("Enter the type of ice cream.")
        cost = float(strput("Enter the cost per scoop."))
        amount = intput("Enter the amount of scoops.")
        return IceCream(name,amount,cost)
    
    def user_prompt_sundae(self):
        name = strput("Enter the type of icecream.")
        cost = float(strput("Enter the cost per scoop."))
        amount = intput("Enter the amount of scoops.")
        topping = strput("Enter the topping.")
        toppingcost = float(strput("Enter the price of the topping."))
        return Sundae(name,amount,cost,topping,toppingcost)

def main():
    shop = DessertShop()
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([
    '1: Candy',
    '2: Cookie',
    '3: Ice Cream',
    '4: Sundae',
    '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])
    while not done:
      cs()
      choice = strput(prompt)
      match choice:
        case '':
            done = True
        case '1':
            item = shop.user_prompt_candy()
            order.add(item)
            timeprint(f'{item.name} has been added to your order.')
        case '2':
            item = shop.user_prompt_cookie()
            order.add(item)
            timeprint(f'{item.name} has been added to your order.')
        case '3':
            item = shop.user_prompt_icecream()
            order.add(item)
            timeprint(f'{item.name} has been added to your order.')
        case '4':
            item = shop.user_prompt_sundae()
            order.add(item)
            timeprint(f'{item.name} has been added to your order.')
        case _:
            timeprint('Invalid response: Please enter a choice from the menu (1-4) or Enter')
    #
    #add your code below here to print the PDF receipt as the last thing in main()
    #
    data = [ 
    ["Name", "Price", "Tax" ]]
    for item in order.desserts:
        data.append([f"{item.name} ({item.packaging})", '$' + str(round(item.calculate_cost(),2)), '$' + str(round(item.calculate_tax(),2))])
    data.append([ "Subtotal", '$' +str(round(order.order_cost(),2)), '$' +str(round(order.order_tax(),2))])
    data.append([ "Total", "", '$' +str(round(order.order_cost() + order.order_tax(),2))])
    data.append(["Total items in the order","",str(len(order))])
    make_receipt(data,"reciept.pdf")

cs()
main()