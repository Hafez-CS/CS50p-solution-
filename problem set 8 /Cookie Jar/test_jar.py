import pytest
from jar import Jar




def test_withdraw():
    n = Jar()
    n.deposit(4)
    n.withdraw(1)
    assert n.size == 3
    with pytest.raises(ValueError):
        n.withdraw(100)





def test_deposit():
    n = Jar()
    n.deposit(1)
    assert n.size == 1
    with pytest.raises(ValueError):
        n.deposit(20)




def test_init():
    n = Jar()




def test_str():
    n = Jar()
    assert str(n) == ""
    n.deposit(1)
    assert str(n) == "🍪"
    n.deposit(11)
    assert str(n) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
