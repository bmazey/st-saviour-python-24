from oop.music.music import Music

class Lyrical(Music):

    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool):
        super().__init__(title, bpm, instruments, True)
        self.lyrics = lyrics
        self.has_lyrics = has_lyrics
        self.has_lyrics = True 

    def sing(self):
        return 'artist sings ' + self.title + ' with lyrics: ' + self.lyrics
