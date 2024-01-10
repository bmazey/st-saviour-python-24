from oop.music.lyrics import Lyrics
from oop.music.music import Music
from oop.music.beats import Beats


def test_lyrics():
    listen = Lyrics('rip', 80, ['bass'],'Rest in peace, you and me', True)
    assert listen.play == 'rip is a song that plays at 80 beats per minute with bass'
    assert listen.listen == 'the song rip has the lyrics Rest in peace, you and me'

    assert isinstance(listen, Music)

def test_beats():
    listen = Beats('Hyperion', 125, ['keyboard'], False)
    assert listen.play == 'Hyperion is a song that plays at 125 beats per minute with keyboard'
    assert listen.listen == 'it is False that the song Hyperion has lyrics'

    assert isinstance(listen, Music)