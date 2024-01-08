from oop.music.music import Music 
from oop.music.beats import Beats
from oop.music.classical import Classical

def test_classical(): 
    conduct = Classical('Imperial March', 103, ['tuba'], False, True, 'trombone')
    assert conduct.play == ''
    assert conduct.listen == ''
    assert conduct.conduct == ''

    assert conduct.bpm == 103 
    assert isinstance(conduct, Music)
    assert isinstance(conduct, Beats)
    assert isinstance(conduct, Classical)