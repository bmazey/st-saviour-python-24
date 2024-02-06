from oop.mammal.mammal import Mammal

class Monotreme(Mammal):
    """a class which defines all Monotremes"""
    def __init__(self, name):
        super().__init__(name)

        # Monotremes lay eggs!
        self.nest = [] #empty list,no eggs in the nest

    def empty_nest(self) -> bool:
        """returns true iff nest is empty"""
        # iff means if and only if
        return len(self.nest) == 0
