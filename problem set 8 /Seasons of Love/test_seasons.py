from seasons import cv




def test_date():
    assert cv(365) == "Five hundred twenty-five thousand, six hundred minutes" # use convert
    assert cv(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes" # use convert
