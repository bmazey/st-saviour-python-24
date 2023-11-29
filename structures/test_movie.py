"""test suite for python queues"""
from structures.movie import Movie

"""verify movie queue implementation"""
five_nights_at_freddys = Movie()

    # add a patron to the queue
five_nights_at_freddys.enqueue('freddy fazbear')

    # ensure that patrons queue is not empty
assert not five_nights_at_freddys.is_empty()

    # add more patrons to the patrons queue
five_nights_at_freddys.enqueue('bonnie')
five_nights_at_freddys.enqueue('chica')
five_nights_at_freddys.enqueue('foxy')

    # ensure freddy is still in front and foxy is last
assert five_nights_at_freddys.first() == 'freddy fazbear'
assert five_nights_at_freddys.last() == 'foxy'

    # start admitting patrons to the movie
assert five_nights_at_freddys.dequeue() == 'freddy fazbear'
assert five_nights_at_freddys.dequeue() == 'bonnie'

    # ensure that chica is next and foxy is still last
assert five_nights_at_freddys.first() == 'chica'
assert five_nights_at_freddys.last() == 'foxy'

    # admit all patrons in line
assert five_nights_at_freddys.dequeue() == 'chica'
assert five_nights_at_freddys.dequeue() == 'foxy'

    # ensure no patrons are left in the queue
assert five_nights_at_freddys.is_empty()

    # attempt to dequeue from an empty patrons list
assert five_nights_at_freddys.dequeue() == ''
