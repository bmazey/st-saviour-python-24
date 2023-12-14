from oop.music.music import Music

class Instrumental(Music):

    def __init__(self, name):
        super().__init__(name)

        self.has_lyrics = False
    