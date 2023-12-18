from oop.music.music import Music

def test_music():
    instruments = str('kazoo and guitar')
    jam = Music('lent', 106, instruments)
    play = jam.play()
    assert play == 'lent is a song that plays at 106 beats per minute with kazoo and guitar'

