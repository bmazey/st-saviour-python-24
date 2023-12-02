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
        # TODO implement enqueue()
        # adds a person to the line
        patrons= []
        self.patrons.append(patron)
        
        return None

    def dequeue(self) -> str:
        """
        removes a patron from the patrons list, returns the patron name.
        dequeue() should return an empty string instead of an error if
        someone tries to dequeue from an empty patrons list
        """
        # TODO implement dequeue()
        # makes sure that/says that self.patrons is equal to zero and checks if its empty
        if len(self.patrons) == 0:
            return ''
        # makes a name for the first patron in the queue
        animatronic = self.patrons[0]
        # first person in line leaves
        self.patrons.pop(0)
        return animatronic
    
    def first(self) -> str:
        """reads and returns the name of the first patron in line"""
        # TODO implement first()
        # repeats the name of the person in the front of the line
        return self.patrons[0]

    def last(self) -> str:
        """reads and returns the name of the last patron in line"""
        # repeats the name at the end of the line
        # TODO implement last()
        a = len(self.patrons) - 1
        return self.patrons[a]

    def is_empty(self) -> bool:
        """returns True if the patrons list is empty, and false otherwise"""
        # TODO implement is_empty()
        # tells us if the line is empty or not by saying true or false
        if len(self.patrons) == 0:
            return True
        return False
        