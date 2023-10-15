from fundamentals.fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(1) == ''
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(15) == 'fizzbuzz'

    # TODO - add more test cases ...
