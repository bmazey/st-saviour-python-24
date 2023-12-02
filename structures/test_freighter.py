"""a test suite for python stacks"""
from structures.freighter import Freighter

def test_freighter():
    """verify freighter stack implementation"""
    # create a Freighter called S.S. Anne
    ss_anne = Freighter()

    # add an item to the containers stack on the S.S. Anne
    ss_anne.push('pokeball')

    # ensure containers stack isn't empty
    assert not ss_anne.is_empty()

    # take the item off the stack, and assert the containers stack is empty
    assert ss_anne.pop() == 'pokeball'
    assert ss_anne.is_empty()

    # now let's load and unload some containers
    ss_anne.push('paralyze heal')
    ss_anne.push('repel')
    ss_anne.push('super potion')

    # check order of containers stack
    assert ss_anne.top() == 'super potion'
    assert ss_anne.bottom() == 'paralyze heal'

    # take an item off
    ss_anne.pop()

    # verify the new top item
    assert ss_anne.top() == 'repel'

    # take all items off
    assert ss_anne.pop() == 'repel'
    assert ss_anne.pop() == 'paralyze heal'

    # check emptiness
    assert ss_anne.is_empty()

    # try to pop an item off an empty containers stack
    assert ss_anne.pop() == ''
