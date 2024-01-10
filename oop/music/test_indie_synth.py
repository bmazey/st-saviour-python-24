from oop.music.music import Music
from oop.music.lyrics import Lyrics
from oop.music.indie import Indie
from oop.music.synth import Synth

def test_indie():
    words = Indie('Juggernaut', 124, ['vocals'], 'Like a juggernaut, see it coming', True)
    assert words.play == 'Juggernaut is a song that plays at 124 beats per minute with vocals'
    assert words.listen == 'the song Juggernaut has the lyrics Like a juggernaut, see it coming'
    assert words.words == 'it is True that Juggernaut has lyrics'

    assert isinstance (words, Music)
    assert isinstance (words, Lyrics)
    assert isinstance (words, Indie)

def test_synth():
    depeche_mode = Synth('Strangelove', 117, ['synthesizers'], 'Strangelove, strange highs and strange lows', True)
    assert depeche_mode.play == 'Strangelove is a song that plays at 117 beats per minute with synthesizers'
    assert depeche_mode.listen == '' 
    assert depeche_mode.electronic == ''

    assert isinstance (depeche_mode, Music)
    assert isinstance (depeche_mode, Lyrics)
    assert isinstance (depeche_mode, Synth)