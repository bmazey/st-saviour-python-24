"""queues in python"""
class Movie:
    """
    picture a group of patrons (or fans) camped outside a movie theater awaiting
    a major motion picture release. generally, the first to get in line will be
    the first to be admitted into the theater. by extension, the last to get in
    line will be the last to enter. 

    in computer science we refer to this common data structure as a queue. in this
    exercise we'll be implementing a simple queue of patrons for our movie theater.
    you'll have to learn about the use of "self" in order to complete the Movie
    implementation.
    """
    def __init__(self):
        # notice the use of 'self' here
        self.patrons = []
        # saying that self.patrons is an empty list

    def enqueue(self, patron: str) -> None:
        """adds a patron to the patrons list, returns None"""
        # we are saying that we are going to add a patron to the list
        self.patrons.append(patron)
        
        # We are telling the code that it shouldn't return anything
        return None

    def dequeue(self) -> str:
        """
        removes a patron from the patrons list, returns the patron name.
        dequeue() should return an empty string instead of an error if
        someone tries to dequeue from an empty patrons list
        """
        # TODO implement dequeue()
        # if the list is empty return an empty string, otherwise remove the first patron from the list and return it as a string
        if self.patrons == []:
            return ''
        else:
            return self.patrons.pop(0)
        

    def first(self) -> str:
        """reads and returns the name of the first patron in line"""
        # were creating a variable and saying it's equal to the first digit, 0, and then we are saying to return that digit
        first = self.patrons[0]
        return first

    def last(self) -> str:
        """reads and returns the name of the last patron in line"""
        # were creating a variable and saying it is equal to the last digit in the list, then were saying to return that digit
        last = self.patrons[-1]
        return last

    def is_empty(self) -> bool:
        """returns True if the patrons list is empty, and false otherwise"""
        # if the list is empty return true if it isn't return false
        if self.patrons == []:
            return True
        return False
        
