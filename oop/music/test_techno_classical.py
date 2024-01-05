from oop.music.music import Music
from oop.music.beats import Beats
from oop.music.techno import Techno
from oop.music.classical import Classical

def test_techno():
    rave = Techno('Technologic', 127, ['turntables'], False, True, 'electric piano')
    assert rave.sing() == 'it is False that the song Technologic has lyrics'
    assert rave.play() == 'Technologic is a song that plays at 127 beats per minute with turntables'
    assert rave.produce() == 'the song Technologic creates futuristic themes by using the electric piano'

    assert rave.bpm == 127
    assert isinstance(rave, Music)
    assert isinstance(rave, Beats)
    assert isinstance(rave, Techno)

def test_classical():
    listen = Classical('Avengers', 120, ['piano'], False, True, 'trumpet')
    assert listen.sing() == 'it is False that the song Avengers has lyrics'
    assert listen.play() == 'Avengers is a song that plays at 120 beats per minute with piano'
    assert listen.conduct() == 'the song Avengers has the woodwind instrument: trumpet'

    assert listen.bpm == 120
    assert isinstance(listen, Music)
    assert isinstance(listen, Beats)
    assert isinstance(listen, Classical)
