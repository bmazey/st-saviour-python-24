
from oop.music.lyrical_songs import Lyrical
from oop.music.instrumental_song import Instrumental

def test_lyrics():
    last_chrismas = Lyrical('Last Christmas', 60, ['vocals'], 'The very next day you threw it away.', True)
    assert last_chrismas.sing() == 'artist sings Last Christmas with lyrics: The very next day you threw it away.'
    assert last_chrismas.play() == 'This song is called Last Christmas. This song plays at 60 bpm with vocals'

def test_instrumental():
    cello_song = Instrumental('Cello Song', 80, ['saxophone, percussion, guitar'], 'cello', False )
    assert cello_song.beats() == 'artist sings Cello Song which has no lyrics but plays a cello as a leading instrument'
    assert cello_song.play() == 'This song is called Cello Song. This song plays at 80 bpm with saxophone, percussion, guitar'