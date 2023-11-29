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

    # class  vs instance 
    # class is ideal 
    # instance is reality 

    # queue is first in first out

    def __init__(self):
        # notice the use of 'self' here
        self.patrons = []
        # self patrons is an open list/ start of a line/queue

    def enqueue(self, patron: str) -> None:
        """adds a patron to the patrons list, returns None"""
        # TODO implement enqueue()
        self.patrons.append(patron)
        return None
    # return nothing, append the name of a patron to the end of the queue 
        

    def dequeue(self) -> str:
        """
        removes a patron from the patrons list, returns the patron name.
        dequeue() should return an empty string instead of an error if
        someone tries to dequeue from an empty patrons list
        """
        # TODO implement dequeue()
        if self.patrons == []:
            return ''
        # returns an open string of the list is empty 
        else:
            return (self.patrons.pop(0))
        # pops the name or removes the name of the first patron in queue 


    def first(self) -> str:
        """reads and returns the name of the first patron in line"""
        # TODO implement first()
        first = self.patrons[0]
        # the first person in the queue is 0, retuns the name of the first in line 
        return first
    

    def last(self) -> str:
        """reads and returns the name of the last patron in line"""
        # TODO implement last()
        last = self.patrons[-1]
        # last in line is -1, returns the name of the last patron in the queue 
        return last

    def is_empty(self) -> bool:
        """returns True if the patrons list is empty, and false otherwise"""
        # TODO implement is_empty()
        if self.patrons == []:
            return True
        # if the list self patrons is empty returns the bool true 