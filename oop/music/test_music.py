from oop.music.music import Music

def test_music():
    instruments = ['drums']
    bops = Music('runaway', 168, instruments, True)
    # bops.name = 'runaway'
    play = bops.play()
    assert play == 'runaway is a song that plays at 168 beats per minute with drums'