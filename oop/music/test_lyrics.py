from oop.music.lyrics import Lyrics
from oop.music.music import Music
from oop.music.beats import Beats


def test_lyrics():
    listen = Lyrics('Rip', 80, ['bass'], 'Rest in peace, you and me', True)
    assert listen.play() == 'Rip is a song that plays at 80 beats per minute with bass'
    assert listen.listen() == 'The song Rip has the lyrics Rest in peace, you and me'

    assert listen.has_lyrics == True
    assert isinstance(listen, Music)

def test_beats():
    headbop = Beats('Hyperion', 125, ['keyboard'], False)
    assert headbop.play() == 'Hyperion is a song that plays at 125 beats per minute with keyboard'
    assert headbop.headbop() == 'it is False that the song Hyperion has lyrics'

    assert headbop.no_lyrics == False
    assert isinstance(headbop, Music)