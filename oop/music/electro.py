from oop.music.instrumental_song import Instrumental

class Electro(Instrumental):

    def __init__(self, title: str, bpm: int, instrument: [], leading_instrument: str, has_lyrics: bool):
        super().__init__(title, bpm, instrument, leading_instrument, has_lyrics)

        self.leading_instrument = leading_instrument
        leading_instrument = 'synthetizer'
        self.has_lyrics = has_lyrics
        has_lyrics = False
         

    def beatbox(self):
        return self.title + ' is an electro song because its leading instrument is a ' + self.leading_instrument
        