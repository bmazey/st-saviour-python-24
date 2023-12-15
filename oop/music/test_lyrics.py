
from oop.music.lyrical_songs import Lyrical

def test_lyrics():
    last_chrismas = Lyrical('Last Christmas', 60, ['vocals'], 'The very next day you threw it away.', True)
    assert last_chrismas.sing() == 'artist sings Last Christmas with lyrics: The very next day you threw it away.'
    assert last_chrismas.play() == 'This song is called Last Christmas. This song plays at 60 bpm with vocals'