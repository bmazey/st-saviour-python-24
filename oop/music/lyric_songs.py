from oop.music.music import Music

class Lyrics(Music):
    """a new class that identifies music that has lyrics"""
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool):
        super().__init__(title, bpm, instruments, True)
        self.lyrics = lyrics
        self.has_lyrics = has_lyrics
        # we are teling the code that there should be lyrics in the music in Lyrics
        self.has_lyrics = True

    def sing(self) -> str:
        return 'the song ' + self.title + ' has the lyrics: ' + self.lyrics