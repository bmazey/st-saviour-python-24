from oop.music.lyrics import Lyrics
from oop.music.music import Music
from oop.music.beats import Beats


def test_lyrics():
    listen = Lyrics('rip', 80, ['singing'],'', True)
    assert listen.play == ''
    assert listen.listen == ''

    assert isinstance(listen, Music)

def test_beats():
    listen = Beats('', )
    assert listen.play == ''
    assert listen.listen == ''

    assert isinstance(listen, Music)