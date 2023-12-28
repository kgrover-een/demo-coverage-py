from branch import calc_tax

def test_calc_tax_percent():
    assert calc_tax(33,250001) == 25000

def test_calc_other_tax():
    assert calc_tax(40,130000) == 0

def test_calc_another_tax():
    assert calc_tax(65,250001) == 0

def test_calc_more_tax():
    assert calc_tax(70, 320000)== 32000