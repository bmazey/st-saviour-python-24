from oop.music.music import Music

class Instrumental(Music):

    def __init__(self, title: str, bpm: int, instruments: [], leading_instrument: str, has_lyrics: bool):
        super().__init__(title, bpm, instruments, False)
        self.leading_instrument = leading_instrument
        self.has_lyrics = has_lyrics
        self.has_lyrics = False

    def beats(self):
        return 'the song ' + self.title + ' has a bpm of ' + self.bpm + 
    