from oop.music.music import Music

class Lyrical(Music):

    def __init__(self, name: str, bpm: int, instruments: [], lyrics: str):
        super().__init__(name, bpm, instruments, True)
        self.lyrics = lyrics
        self.has_lyrics = True 

    def sing(self):
        return 'artist sings ' + self.name + ' with lyrics: ' + self.lyrics
