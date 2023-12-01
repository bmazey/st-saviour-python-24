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

    def enqueue(self, patron: str) -> None:
        """adds a patron to the patrons list, returns None"""
        # appends patron to the self.patrons list
        self.patrons.append(patron)
        return None

    def dequeue(self) -> str:
        """
        removes a patron from the patrons list, returns the patron name.
        dequeue() should return an empty string instead of an error if
        someone tries to dequeue from an empty patrons list
        """
        # states that the length of self.patrons is zero, checks to see if empty
        if len(self.patrons) == 0:
            return ''
        # making a variable for the name of the first patron
        name = self.patrons[0]
        # removing first patron in the list
        self.patrons.pop(0)
        return name
        
    def first(self) -> str:
        """reads and returns the name of the first patron in line"""
        # position 0 is the first position, so it returns the position of the first patron
        return self.patrons[0]
        

    def last(self) -> str:
        """reads and returns the name of the last patron in line"""
        # the last position in the list is one less then the whole legnth of the list
        # because positions start at 0, the final position is 1 less then the total length 
        # create a variable for the last patron in line, called last
        last = len(self.patrons) - 1
        # return the last of self.patrons
        return self.patrons[last]


    def is_empty(self) -> bool:
        """returns True if the patrons list is empty, and false otherwise"""
        # an empty line would have no one waiting on it, so an empty list would have nothing in it
        if len(self.patrons) == 0:
            # returns true if the length is 0 because the list it would be true that the list is empty if the list had nothing in it
            return True
        # in case the list doesnt have a length of 0, it will move on and automatically return false
        return False
