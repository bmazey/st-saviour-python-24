
class Music:
    def __init__(self, bpm: int, instruments: str, lyrical: bool):
        self.bpm = bpm
        self.instruments = instruments
        self.lyrical = lyrical
    
    def play(self, song: str):
        return song + 'is a song that plays at' + self.bpm + 'with' + self.instruments 