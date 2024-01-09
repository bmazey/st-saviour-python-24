from oop.music.lyrics import Lyrics

class Indie(Lyrics): 
    """ Is a class that identifies Indie music """
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool):
        self.lyrics = lyrics
        self.has_lyrics = has_lyrics 
        self.has_lryics = True

def words(self) -> str:
    return 'it is ' + self.has_lryics + ' that ' + self.title + 'has lyrics'
        