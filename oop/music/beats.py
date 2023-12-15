from oop.music.music import Music

class Beats(Music):
    """a new class that identifies music that doesn't have lyrics"""
    def __init__(self, title: str, bpm: int, instruments: [], no_lyrics: bool):
        self.no_lyrics = no_lyrics
        # we are teling the code that there should be lyrics in the music in Lyrics
        self.no_lyrics = False
        super().__init__(title, bpm, instruments, False)

    def sing(self) -> str:
        return 'it is  ' + str(self.no_lyrics) + ' that the song ' + self.title + ' has lyrics'