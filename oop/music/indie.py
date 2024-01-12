from oop.music.lyrics import Lyrics

class Indie(Lyrics): 
    """ is a class that identifies Indie music """
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool):
        super().__init__(title, bpm, instruments, lyrics, True)
        self.lyrics = lyrics
        self.has_lyrics = has_lyrics 
        self.has_lryics = True

    def words(self) -> str:
        return 'it is ' + str(self.has_lryics) + ' that ' + self.title + ' has lyrics'
        