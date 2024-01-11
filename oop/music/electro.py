from oop.music.instrumental_song import Instrumental

class Electro(Instrumental):
    """A class that defines all music in the electro genre"""

    # Assigning all properties of Music and Instrumental to the Electro class
    # Instances of Electro have a synthetizer as a leading instrument
    def __init__(self, title: str, bpm: int, instrument: [], leading_instrument: str, has_lyrics: bool):
        super().__init__(title, bpm, instrument, leading_instrument, has_lyrics)

        self.leading_instrument = leading_instrument
        leading_instrument = 'synthetizer'
        self.has_lyrics = has_lyrics
        has_lyrics = False

    def __str__(self):
        return f'title: {self.title} bpm: {self.bpm} instruments: {self.instruments} leading instrument: {self.leading_instrument}'
         

    def beatbox(self):
        return self.title + ' is an electro song because its leading instrument is a ' + self.leading_instrument
        