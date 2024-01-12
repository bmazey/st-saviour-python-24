from oop.music.music import Music

def test_music():
    """ identifying music """
    instruments = ['kazoo']
    jam = Music('lent', 106, instruments, True)
    play = jam.play()
    assert play == 'lent is a song that plays at 106 beats per minute with kazoo'

