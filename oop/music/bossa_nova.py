from oop.music.lyrical_songs import Lyrical

class Bossa_Nova(Lyrical):
    """A class that defines music in the bossa nova genre"""

    # Assigning all properties of Music and Lyrical to the Bossa_Nova class
    # Instances of Bossa_Nova have an acoustic as a leading instrument
    def __init__(self, title: str, bpm: int, instruments: [], leading_instrument: str, lyrics: str, has_lyrics: bool, improv_lyrics: str):
        super().__init__(title, bpm, instruments, lyrics, has_lyrics)

        self.improv_lyrics = improv_lyrics
        self.leading_instrument = leading_instrument
        leading_instrument = 'acoustic guitar'

    def gilberto(self):
        return self.title + ' is a bossa nova song because of its ' + self.leading_instrument + ' and lyrics'