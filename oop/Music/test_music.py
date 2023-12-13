from oop.music.music import Music

def test_music():
    instruments = ['guitar', 'kazoo', 'piano']
    jam = Music('lent', 106, instruments)
    play = jam.play()
    assert play == 'lent is a song that plays at 106 bpm with guitar, kazoo, piano'

