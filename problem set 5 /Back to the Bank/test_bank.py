from bank import value


def test_greeting(): # test it
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
    assert value("WASSUP WORLD") == 100
    assert value("HELLO WORLD") == 0
    assert value("wassup world") == 100
    assert value("hello world") == 0

