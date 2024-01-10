from oop.music.music import Music 
from oop.music.beats import Beats
from oop.music.classical import Classical
from oop.music.indie import Indie
from oop.music.lyrics import Lyrics
from oop.music.synth import Synth

def test_classical(): 
    conduct = Classical('Imperial March', 103, ['tuba'], False, True, 'trombone')
    assert conduct.play == 'Imperial March is a song that plays at 103 beats per minute with tuba'
    assert conduct.listen == 'it is False that Imperial March has lyrics'
    assert conduct.conduct == 'the song Imperial March has the brass instrument trombone'

    assert conduct.bpm == 103 
    assert isinstance(conduct, Music)
    assert isinstance(conduct, Beats)
    assert isinstance(conduct, Classical)