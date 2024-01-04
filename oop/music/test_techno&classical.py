from oop.music.techno import Techno

def test_techno():
    rave = Techno('Technologic', 127, ['Turntables'], False, True, ['electric piano'])
    assert rave.sing() == 'it is False that the song Technologic has lyrics'
    assert rave.play() == 'Technologic is a song that plays at 127 beats per minute with turntables'
    assert rave.produce() == 'The song Technologic creates futuristic themes by using the electric piano'