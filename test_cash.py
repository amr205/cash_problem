from cash import calculate_minimum_coins

def test_amount_equals_coin():
    assert calculate_minimum_coins(.01) == 1
    assert calculate_minimum_coins(.05) == 1
    assert calculate_minimum_coins(.10) == 1
    assert calculate_minimum_coins(.25) == 1


def test_case_one():
    assert calculate_minimum_coins(.41) == 4

def test_case_two():
    assert calculate_minimum_coins(.50) == 2

def test_case_three():
    assert calculate_minimum_coins(.54) == 6

def test_case_four():
    assert calculate_minimum_coins(1.54) == 10

def test_case_five():
    assert calculate_minimum_coins(100.41) == 404

def test_case_six():
    assert calculate_minimum_coins(.26) == 2