from desserts import Cookie

def test_cookie():
    fud = Cookie("chocolate chip",12,12.99)
    assert fud.calculate_cost() == 12.99
    assert fud.calculate_tax() == fud.calculate_cost() * fud.taxpercent/100
    assert fud.taxpercent == 7.25
    assert str(fud) == "chocolate chip, 12 cookies, $12.99 per dozen, total cost $12.99, tax $0.94, packaging box"