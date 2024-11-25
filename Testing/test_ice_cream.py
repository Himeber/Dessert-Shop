from desserts import IceCream

def test_icecream():
    fud = IceCream("vanilla",3,3.5)
    assert fud.calculate_cost() == 3*3.5
    assert fud.calculate_tax() == fud.calculate_cost() * fud.taxpercent/100
    assert fud.taxpercent == 7.25
    assert str(fud) == "vanilla, 3 scoops, $3.5 per scoop, total cost $10.5, tax $0.76, packaging bowl"