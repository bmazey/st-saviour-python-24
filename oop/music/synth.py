from oop.music.lyrics import Lyrics

class Synth(Lyrics):
    """ a class that identifies Indie music """
    def __init__(self, title: str, bpm: int, instruments: [], lryics: str, has_lyrics: bool):
        self.lyrics = lryics
        self.has_lyrics = has_lyrics
        self.has_lyrics = True

def electronic(self) -> str:
    return self.title + ' having lyrics is ' + self.has_lyrics

