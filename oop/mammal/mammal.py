from oop.animal import Animal

class Mammal(Animal):
    #we use captial letter when we use class.
    """a class which defines all Mammals"""
    def __init__(self, name):
        super().__init__(name)
        #super means one level up. 

        # all Mammals are warm-blooded
        self.warm_blooded = True
        #snake case (self.warm_blooded)

    # all mammals eat
    def eat(self, food: str) -> str:
        return self.name + ' the ' + str(self.__class__.__name__) + " eats " + food + "!"
