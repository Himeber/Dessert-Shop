from desserts import IceCream

def test_icecream():
    fud = IceCream("vanilla",3,3.5)
    assert fud.calculate_cost() == 3*3.5
    assert fud.calculate_tax() == fud.calculate_cost() * fud.taxpercent/100
    assert fud.taxpercent == 7.25