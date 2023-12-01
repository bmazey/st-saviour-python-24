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
        self.containers = []

    def push(self, container: str) -> None:
        """adds a new container to the stack containers and returns None"""
        # adds/appends a container to self.containers 
        self.containers.append(container)
        return None

    def pop(self) -> str:
        """
        removes the container on top of the stack and returns the name
        returns an empty string if the containers stack is empty, instead 
        of an error
        """
        # empty lists will have a len of 0
        if len(self.containers) == 0:
            # returns empty quotes cause theres nothing in it
            return ''
        # variable x represents the container that is on top of all the other containers
        # on a freighter, the container on the top gets removed first
        # the container on the top would be the last container in the list
        # because of first in last out
        x = len(self.containers) - 1
        # name is the name of the last container in self.containers
        # the name needs to be accounted for before it gets removed
        name = self.containers[x]
        # .pop removes the last container in the list
        self.containers.pop(x)
        return name
        

    def top(self) -> str:
        """reads and returns the name of the container on top of the stack"""
        # the position of container on the top is one less of the total length of the stack
        last = len(self.containers) - 1
        # return the variable that represents top container in self.containers
        return self.containers[last]

    def bottom(self) -> str:
        """reads and returns the name of the container on the bottom of the stack"""
        # the container on the bottom of the stack has the first position
        # 0 is the first position, so self.containers[0] gets returned
        return self.containers[0]

    def is_empty(self) -> bool:
        """returns True if containers is empty, and False otherwise"""
        # empty containers have a length of 0
        if len(self.containers) == 0:
            # if the list has nothing in it, it will return true
            return True
        # if self.containers has something in it, the len will be > 0 
        if len(self.containers) > 0:
            # then it will be false cause the list is not empty
            return False