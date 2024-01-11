from oop.music.music import Music

class Lyrics(Music):
    """a new class that identifies that music has lyrics"""
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool):
        super().__init__(title, bpm, instruments, lyrics, True)
        self.lyrics = lyrics 
        self.has_lyrics = has_lyrics

        # identifies that a song with lyrics is a bool returning True. 
        self.has_lyrics = True

    def listen(self) -> str:
        return 'the song ' + self.title + ' has the lyrics ' + self.lyrics