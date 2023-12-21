from oop.music.lyrical_songs import Lyrical

class Bossa_Nova(Lyrical):

    def __init__(self, title: str, bpm: int, instruments: [], leading_instrument: str, lyrics: str, has_lyrics: bool, improv_lyrics: str):
        super().__init__(title, bpm, instruments, lyrics, has_lyrics)

        self.improv_lyrics = improv_lyrics
        self.leading_instrument = leading_instrument
        leading_instrument = 'acoustic guitar'

    def gilberto(self):
        return self.title