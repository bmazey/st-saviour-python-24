from oop.music.music import Music

def test_play():
    instruments = ['saxophone', 'flute']
    work_song = Music('work song', 80, instruments, True)
    assert work_song.play() == 'This song is called work song. This song plays at 80 bpm with saxophone, flute'


