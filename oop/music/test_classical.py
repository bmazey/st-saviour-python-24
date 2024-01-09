from oop.music.music import Music 
from oop.music.beats import Beats
from oop.music.classical import Classical
from oop.music.indie import Indie
from oop.music.lyrics import Lyrics

def test_classical(): 
    conduct = Classical('Imperial March', 103, ['tuba'], False, True, 'trombone')
    assert conduct.play == 'Imperial March is a song that plays at 103 beats per minute with tuba'
    assert conduct.listen == 'it is False that Imperial March has lyrics'
    assert conduct.conduct == 'the song Imperial March has the brass instrument trombone'

    assert conduct.bpm == 103 
    assert isinstance(conduct, Music)
    assert isinstance(conduct, Beats)
    assert isinstance(conduct, Classical)


def test_indie():
    words = Indie('Juggernaut', 124, ['vocals'], 'Like a juggernaut, see it coming', True)
    assert words.play == 'Juggernaut is a song that plays at 124 beats per minute with vocals'
    assert words.listen == 'the song Juggernaut has the lyrics Like a juggernaut, see it coming'
    assert words.words == 'it is True that Juggernaut has lyrics'

    assert isinstance (words, Music)
    assert isinstance (words, Lyrics)
    assert isinstance (words, Indie)