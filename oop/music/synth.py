from oop.music.lyrics import Lyrics

class Synth(Lyrics):
    """ a class that identifies Indie music """
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool):
        super().__init__(title, bpm, instruments, lyrics, True)
        self.lyrics = lyrics
        self.has_lyrics = has_lyrics
        self.has_lyrics = True

def electronic(self) -> str:
    return self.title + ' having lyrics is ' + self.has_lyrics

