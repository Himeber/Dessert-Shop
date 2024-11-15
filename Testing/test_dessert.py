from desserts import (Candy)


def test_dessertitem():
    dessert = Candy()
    assert(dessert.name == "bob")
    assert(dessert.taxpercent == 7.25)