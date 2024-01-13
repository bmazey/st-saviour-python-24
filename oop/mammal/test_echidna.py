from oop.mammal.echidna import Echidna

def test_new_echidna():
    """verifies the functionality of the Echdina class and OOP hierarchy"""
    emma = Echidna('Emma')

    # start by asserting empty nest
    assert emma.empty_nest()

    # add some eggs to the nest!
    emma.lay_egg('Knuckles')
    emma.lay_egg('Sonic')
    emma.lay_egg('Tails')

    # attempt to hatch
    knuckles = emma.hatch()

    # assert properties of knuckles
    assert isinstance(knuckles, Echidna)
    assert knuckles.name == 'Knuckles'

    # assert properties of all eggs in emma's nest
    for egg in emma.nest:
        assert egg.warm_blooded
        assert isinstance(egg, Echidna)

    # hatch all eggs
    emma.hatch()
    emma.hatch()

    # check corner case using hatch() on empty nest
    assert emma.hatch() == ''

    # verify nest is empty
    assert emma.empty_nest()
