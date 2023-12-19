from oop.music.lyric_songs import Lyrics
from oop.music.beats import Beats

def test_lyrics():
    grooves = Lyrics('Here', 120, ['vocals'], 'I ask myself what am I doing here', True)
    assert grooves.sing() == 'the song Here has the lyrics: I ask myself what am I doing here'
    assert grooves.play() == 'Here is a song that plays at 120 beats per minute with vocals'

def test_beats():
    jams = Beats('snowman', 105, ['woodwinds'], False)
    assert jams.sing() == 'it is False that the song snowman has lyrics'
    assert jams.play() == 'snowman is a song that plays at 105 beats per minute with woodwinds'