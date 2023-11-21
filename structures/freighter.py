"""stacks in python"""
class Freighter:
    """
    picture a freighter - a large ship used to transport containers on transoceanic
    voyages. when containers are initially loaded on the ship, they are stacked one
    on top of the other. this implies that the first container to be loaded on the
    ship is the last container to be unloaded from the ship when we arrive at the
    destination. 

    this common data structure is (unsurprisingly) referred to as a stack in
    computer science. in this exercise we'll be implementing a simple stack in python
    using lists. you'll have to learn about the use of "self" to complete the 
    Freighter class implementation.
    """
    def __init__(self):
        # note the use of 'self' here
        # this is an empty list that can be used throughout this assessment
        self.containers = []

    def push(self, container: str) -> None:
        """adds a new container to the stack containers and returns None"""
        # TODO implement push()
        # we are adding a container to the empty list
        self.containers.append(container)
        # we tell the code that we don't want it to return anything
        return None

    def pop(self) -> str:
        """
        removes the container on top of the stack and returns the name
        returns an empty string if the containers stack is empty, instead 
        of an error
        """
        # TODO implement pop()
        # we are telling the code that if the list self.containers is empty we want it to return an empty string
        # if the list isn't empty we want it to return and take out the last object put into the list
        if self.containers == []:
            return ''
        else:
            return (self.containers.pop(-1))

    def top(self) -> str:
        """reads and returns the name of the container on top of the stack"""
        # TODO implement top()
        # we are identifing a new variable and making it the last object in the new self.containers list
        dom = self.containers[-1]
        # return the new last object in the list
        return dom

    def bottom(self) -> str:
        """reads and returns the name of the container on the bottom of the stack"""
        # TODO implement bottom()
        # we are creating a new variable and making it the first object in the list
        sub = self.containers[0]
        # return the first object in the list
        return sub

    def is_empty(self) -> bool:
        """returns True if containers is empty, and False otherwise"""
        # TODO implement is_empty()
        # we are saying that if the list is empty we should return that it is true otherwise we are returning false
        if self.containers == []:
            return True
