from fundamentals.palindrome import is_palindrome
def test_is_palindrome():
    assert is_palindrome('civic')
    assert is_palindrome('racecar')
    assert is_palindrome('tacocat')

    assert not is_palindrome('robot')
    assert not is_palindrome('cookies')
    
    # TODO - add more test cases ... 