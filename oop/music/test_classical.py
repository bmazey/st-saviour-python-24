from oop.music.music import Music 
from oop.music.beats import Beats
from oop.music.classical import Classical
from oop.music.lyrics import Lyrics


def test_classical(): 
    """ verify instance of Classical music """
    star_wars = Classical('Imperial March', 103, ['tuba'], False, True, 'trombone')
    assert star_wars.play() == 'Imperial March is a song that plays at 103 beats per minute with tuba'
    assert star_wars.headbop() == 'it is False that the song Imperial March has lyrics'
    assert star_wars.conduct() == 'the song Imperial March has the brass instrument trombone'

    assert star_wars.bpm == 103 
    assert star_wars.no_lyrics == False
    assert star_wars.brass == True
    assert isinstance(star_wars, Music)
    assert isinstance(star_wars, Beats)
    assert isinstance(star_wars, Classical)