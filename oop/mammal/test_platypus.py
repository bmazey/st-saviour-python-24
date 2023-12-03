from oop.animal import Animal
from oop.mammal.mammal import Mammal
from oop.mammal.platypus import Platypus

def test_new_platypus():
    """verifies functionality of Platypus and OOP hierarchy"""
    perry = Platypus('Perry')

    # check properties
    assert perry.name == 'Perry'
    assert perry.warm_blooded

    # check types
    assert isinstance(perry, Animal)
    assert isinstance(perry, Mammal)

    # assert perry's nest is empty
    assert perry.empty_nest()

    # feed perry
    assert perry.eat('ants') == 'Perry the Platypus eats ants!'
