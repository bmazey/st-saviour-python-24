
class Music:
    def __init__(name: str, self, bpm: int, instruments: [], lyrical: bool):
        self.bpm = bpm
        self.instruments = instruments
        self.lyrical = lyrical
        self.name = name
    
    def play(self, song: str):
        return 'This song is called ' + self.name + ' is a song that plays at ' + self.bpm + ' with ' + self.instruments 