from desserts import Sundae

def test_sundae():
    fud = Sundae("Banana",3,3.5,"banana",0.75)
    assert fud.calculate_cost() == 3*3.5 + 0.75
    assert fud.calculate_tax() == fud.calculate_cost() * fud.taxpercent/100
    assert fud.taxpercent == 7.25