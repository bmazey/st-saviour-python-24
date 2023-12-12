from oop.music.music import Music

class Lyrics(Music):
    """a new class that identifies music that has lyrics"""
    def __init__(self, name):
        super().__init__(name)