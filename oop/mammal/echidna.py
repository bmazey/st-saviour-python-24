from oop.mammal.monotreme import Monotreme

class Echidna(Monotreme):
    """a class which defines all Echidnas"""

    def lay_egg(self, name: str):
        """creates a new Echidna and adds it to the nest"""
        baby = Echidna(name)
        self.nest.append(baby)

    def hatch(self):
        """removes and returns first Monotreme in nest using list.pop()"""
        # check to see if nest is empty first
        if self.empty_nest():
            return ''

        return self.nest.pop(0)
