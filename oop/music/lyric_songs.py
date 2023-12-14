from oop.music.music import Music

class Lyrics(Music):
    """a new class that identifies music that has lyrics"""
    def __init__(self, title):
        super().__init__(title)

        # we are teling the code that there should be lyrics in the music in Lyrics
        self.lyrics = True

    def play(self) -> str:
        return 'it is ' + self.lyrics + ' that ' + self.title + ' has lyrics'