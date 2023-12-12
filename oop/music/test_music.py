from oop.music.music import Music

def test_music():
    instruments = ['clarinet', 'sax', 'drums']
    uptown = Music(20, instruments)
    play = uptown.play()