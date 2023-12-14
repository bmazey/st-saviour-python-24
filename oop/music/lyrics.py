from oop.music.music import Music

class Lyrics(Music):
    """a new class that identifies that music has lyrics"""
    def __init__(self, title):
        super().__init__(title)

# identifies that a song with lyrics is a bool returning True. 
        self.lyrics = True

def play(self) -> str:
        return 'it is' + self.lyrics + 'that' + self.title + 'has lyrics'