from cash import calculate_minimum_coins, is_positive_number

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

def test_input_is_a_positive_number():
    assert is_positive_number(".26") == True
    assert is_positive_number("0.0") == True
    assert is_positive_number("0.41") == True
    assert is_positive_number("41") == True
    assert is_positive_number("9.000") == True
    assert is_positive_number("9") == True
    assert is_positive_number("-9") == False
    assert is_positive_number("-9.0") == False
    assert is_positive_number("-.05") == False
    assert is_positive_number("foo") == False
    assert is_positive_number("foo05") == False