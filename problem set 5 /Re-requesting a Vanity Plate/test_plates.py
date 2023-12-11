from plates import is_valid






def test_p():
    assert is_valid("CS50!") == False







def test_l():
    assert is_valid("CS") == True
    assert is_valid("HICS50") == True
    assert is_valid("HELLOCS50") == False







def test_bte():
    assert is_valid("5") == False
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("CS") == True







def test_n():
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False
    assert is_valid("AAA22A") == False




