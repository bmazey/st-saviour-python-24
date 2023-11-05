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
        return None

    def dequeue(self) -> str:
        """
        removes a patron from the patrons list, returns the patron name
        dequeue() should return an empty string instead of an error if
        someone tries to dequeue from an empty patrons list
        """
        return ''

    def first(self) -> str:
        """reads and returns the name of the first patron in line"""
        return ''

    def last(self) -> str:
        """reads and returns the name of the last patron in line"""
        return ''

    def is_empty(self) -> bool:
        """returns True if the patrons list is empty, and false otherwise"""
        return True
