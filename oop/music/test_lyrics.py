from oop.music.music import Music
from oop.music.music import Lyrics


def test_lyrics():
    listen = Lyrics('rip',True)
    play = listen.play()
    assert play == 'it is True that rip has lyrics'