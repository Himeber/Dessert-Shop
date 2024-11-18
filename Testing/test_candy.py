from desserts import (Candy)

def test_candy():
    fud = Candy("chocolate",5,5)
    assert fud.calculate_cost() == 25
    assert fud.calculate_tax() == fud.calculate_cost * fud.taxpercent/100
    assert fud.taxpercent == 7.25