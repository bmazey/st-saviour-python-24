from oop.mammal.animal import Animal

class Mammal(Animal):
    """a class which defines all Mammals"""
    def __init__(self, name):
        super().__init__(name)

        # all Mammals are warm-blooded
        self.warm_blooded = True

    # all mammals eat
    def eat(self, food: str) -> str:
        return self.name + ' the ' + str(self.__class__.__name__) + " eats " + food + "!"
