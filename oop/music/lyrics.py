from oop.music.music import Music

class Lyrics(Music):
    """ a class that identifies Lyrics in Music """
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool):
        super().__init__(title, bpm, instruments, True)
        self.lyrics = lyrics 
        self.has_lyrics = has_lyrics

        # identifies that a song with lyrics is a bool returning True. 
        self.has_lyrics = True

    def listen(self) -> str:
        return 'The song ' + self.title + ' has the lyrics ' + self.lyrics