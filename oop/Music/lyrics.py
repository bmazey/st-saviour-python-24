from oop.music.music import Music

class Lyrics(Music):
    """a new class that identifies that music has lyrics"""
    def __init__(self, name):
        super().__init__(name)

# identifies that a song with lyrics is a bool returning True. 
        self.lyrics = True