from oop.music.music import Music

def test_music():
    instruments = ['saxophone']
    aiwfc=  play.aiwfc(30, instruments)
    #songg =aiwfc.songg
    assert aiwfc.play('song name') == 'some string'


