from oop.mammal.mammal import Mammal

class Monotreme(Mammal):
    """a class which defines all Monotremes"""
    def __init__(self, name):
        super().__init__(name)

        # Monotremes lay eggs!
        self.nest = []

    def empty_nest(self) -> bool:
        """returns true iff nest is empty"""
        return len(self.nest) == 0
