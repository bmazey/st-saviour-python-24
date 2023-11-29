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
        # TODO implement push()
        self.containers.append(container)
        return None

    def pop(self) -> str:
        """
        removes the container on top of the stack and returns the name
        returns an empty string if the containers stack is empty, instead 
        of an error
        """
        # TODO implement pop()
        if not self.is_empty():
            return self.containers.pop()
       

    def top(self) -> str:
        """reads and returns the name of the container on top of the stack"""
        # TODO implement top()
        if not self.is_empty():
            return self.containers[-1]
        

    def bottom(self) -> str:
        """reads and returns the name of the container on the bottom of the stack"""
        # TODO implement bottom()
        if not self.is_empty():
            return self.containers[0]
        

    def is_empty(self) -> bool:
        """returns True if containers is empty, and False otherwise"""
        # TODO implement is_empty()
        return len(self.containers) == 0
        
