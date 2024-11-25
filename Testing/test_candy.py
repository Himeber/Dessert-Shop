from desserts import (Candy)

def test_candy():
    fud = Candy("chocolate",5,5)
    assert fud.calculate_cost() == 25
    assert fud.calculate_tax() == fud.calculate_cost * fud.taxpercent/100
    assert fud.taxpercent == 7.25
    assert str(fud) == "chocolate, 5lbs, $5 per pound, total cost $25, tax $1.81"