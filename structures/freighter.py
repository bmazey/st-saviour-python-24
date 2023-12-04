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
        # The stack of containers, initialized as an empty list
        self.containers = []

    def push(self, container: str) -> None:
        """
        Adds a new container to the stack and returns None.
        The container is added to the end of the list.
        """
        # Appends the new container to the end of the list
        self.containers.append(container)
        return None

    def pop(self) -> str:
        """
        Removes the container on top of the stack and returns its name.
        Returns an empty string if the containers stack is empty.
        """
        # Checks that the stack is not empty before trying to pop
        if not self.is_empty():
            return self.containers.pop()
        # Return an empty string if the stack is empty
        return ''

    def top(self) -> str:
        """
        Reads and returns the name of the container on top of the stack.
        Returns an empty string if the containers stack is empty.
        """
        # Checks if the stack is not empty before accessing the last element
        if not self.is_empty():
            return self.containers[-1]
        # Returns an empty string if the stack is empty
        return ''

    def bottom(self) -> str:
        """
        Reads and returns the name of the container on the bottom of the stack.
        Returns an empty string if the containers stack is empty.
        """
        # Checking if the stack is not empty before opening the first element
        if not self.is_empty():
            return self.containers[0]
        # Returns an empty string if the stack is empty
        return ''

    def is_empty(self) -> bool:
        """
        Returns True if the containers stack is empty, and False otherwise.
        """
        # Checks if the length of the stack is 0
        return len(self.containers) == 0