from desserts import (
    DessertItem,
    Candy,
    IceCream,
    Cookie,
    Sundae
)
def test_dessertitem():
    dessert = DessertItem()
    assert(dessert.name == "bob")
    #nothing else to test on this lol
def test_candy():
    candy = Candy()
    assert(candy.name == "bob")
    assert(candy.candyWeight == 0)
    assert (candy.pricePerPound == 0)
    assert (isinstance(candy,DessertItem))
def test_icecream():
    icecream = IceCream()
    assert (icecream.name == "bob")
    assert (icecream.pricePerScoop == 0.0)
    assert (icecream.scoopCount == 0)
    assert (isinstance(icecream,DessertItem))
def test_cookie():
    cookie = Cookie()
    assert (cookie.name == "bob")
    assert (cookie.pricePerDozen == 0.0)
    assert (cookie.quantity == 0)
    assert (isinstance(cookie,DessertItem))
def test_sundae():
    sundae = Sundae()
    assert (sundae.name == "bob")
    assert (sundae.pricePerScoop == 0.0)
    assert (sundae.scoopCount == 0)
    assert (sundae.toppingName == "")
    assert (sundae.toppingPrice == 0.0)
    assert (isinstance(sundae,DessertItem))
    assert (isinstance(sundae,IceCream))