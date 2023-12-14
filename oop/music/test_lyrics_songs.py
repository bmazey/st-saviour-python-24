from oop.music.music import Music
from oop.music.music import Lyrics

def test_lyrics():
    # here = Lyrics('here')
    grooves = Lyrics('here', True)
    play = grooves.play
    assert play == 'it is True that here has lyrics'
    # test for properties
    # assert here.title == 'here'
    # assert here.lyrics == True

