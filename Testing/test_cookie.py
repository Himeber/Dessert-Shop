from desserts import Cookie

def test_cookie():
    fud = Cookie("chocolate chip",12,12.99)
    assert fud.calculate_cost() == 12* 12.99
    assert fud.calculate_tax() == fud.calculate_cost() * fud.taxpercent/100
    assert fud.taxpercent == 7.25