from oop.music.lyrics import Lyrics


def test_lyrics():
    listen = Lyrics('rip', 80, instruments, True)
    instruments = str('piano and guitar')
    play = listen.play()
    assert play == 'it is True that rip has lyrics and plays with piano and guitar at 80 beats per minute' 