from oop.music.music import Music
from oop.music.lyrics import Lyrics
from oop.music.indie import Indie
from oop.music.synth import Synth

def test_indie():
    autoheart = Indie('Juggernaut', 124, ['vocals'], 'Like a juggernaut, see it coming', True)
    assert autoheart.play() == 'Juggernaut is a song that plays at 124 beats per minute with vocals'
    assert autoheart.listen() == 'The song Juggernaut has the lyrics Like a juggernaut, see it coming'
    assert autoheart.words() == 'it is True that Juggernaut has lyrics'

    assert autoheart.bpm == 124
    assert autoheart.has_lyrics == True
    assert isinstance (autoheart, Music)
    assert isinstance (autoheart, Lyrics)
    assert isinstance (autoheart, Indie)

def test_synth():
    depeche_mode = Synth('Strangelove', 117, ['synthesizers'], 'Strangelove, strange highs and strange lows', True)
    assert depeche_mode.play() == 'Strangelove is a song that plays at 117 beats per minute with synthesizers'
    assert depeche_mode.listen() == 'The song Strangelove has the lyrics Strangelove, strange highs and strange lows' 
    assert depeche_mode.electronic() == 'Strangelove having lyrics is True'

    assert depeche_mode.bpm == 117 
    assert depeche_mode.has_lyrics == True
    assert isinstance (depeche_mode, Music)
    assert isinstance (depeche_mode, Lyrics)
    assert isinstance (depeche_mode, Synth)