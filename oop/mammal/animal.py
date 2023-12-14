from abc import abstractmethod

class Animal:
    """a class which defines all Animals"""
    def __init__(self, name):
        # all animals have a name
        self.name = name

    @abstractmethod
    def eat(self, food: str):
        """all animals can eat"""
        pass
