"""a test suite for python stacks"""
from structures.freighter import Freighter

def test_freighter():
    """verify freighter stack implementation"""
    # creates a Freighter called S.S. Anne
    ss_anne = Freighter()

    # adds an item to the containers stack on the S.S. Anne
    ss_anne.push('pokeball')

    # ensures containers stack isn't empty
    assert not ss_anne.is_empty()

    # takes the item off the stack, and asserts the containers stack is empty
    assert ss_anne.pop() == 'pokeball'
    assert ss_anne.is_empty()

    # loading and unloading some containers
    ss_anne.push('paralyze heal')
    ss_anne.push('repel')
    ss_anne.push('super potion')

    # checks order of containers stack
    assert ss_anne.top() == 'super potion'
    assert ss_anne.bottom() == 'paralyze heal'

    # takes an item off
    ss_anne.pop()

    # verifys the new top item
    assert ss_anne.top() == 'repel'

    # takes all items off
    assert ss_anne.pop() == 'repel'
    assert ss_anne.pop() == 'paralyze heal'

    # checks emptiness
    assert ss_anne.is_empty()

    # try to pop an item off an empty containers stack
    assert ss_anne.pop() == ''