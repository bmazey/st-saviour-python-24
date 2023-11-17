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
        #use of append to add a patron to the back of the queue
        self.patrons.append(patron)

        return None

    def dequeue(self) -> str:
        """
        removes a patron from the patrons list, returns the patron name.
        dequeue() should return an empty string instead of an error if
        someone tries to dequeue from an empty patrons list
        """
        # TODO implement dequeue()
        #establish that the function must return an empty string if queue is empty
        if self.is_empty():
            return ''
        #If queue is not empty, establish patron as being the first element of the list
        else:
            patron = self.patrons[0]
        #remove the first element from the list and return patron
            self.patrons.pop(0)
            return patron
            
        
            
        

    def first(self) -> str:
        """reads and returns the name of the first patron in line"""
        # TODO implement first()
        #return first element of the list
        return self.patrons[0]

    def last(self) -> str:
        """reads and returns the name of the last patron in line"""
        # TODO implement last()
        #return last element of the list
        last = self.patrons[-1]
        return last

    def is_empty(self) -> bool:
        """returns True if the patrons list is empty, and false otherwise"""
        # TODO implement is_empty()
        #establish that an empty string will is assigned to true in a boolean
        if self.patrons == []:
            return True
