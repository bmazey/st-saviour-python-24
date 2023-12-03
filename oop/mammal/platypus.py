from oop.mammal.monotreme import Monotreme

class Platypus(Monotreme):
    """a class which defines all Platypus"""

    def lay_egg(self, name: str):
        """creates a new Platypus and adds it to the nest"""
        baby = Platypus(name)
        self.nest.append(baby)

    def hatch(self):
        """removes and returns first Monotreme in nest using list.pop()"""
        # check to see if nest is empty first
        if self.empty_nest():
            return ''

        return self.nest.pop(0)
