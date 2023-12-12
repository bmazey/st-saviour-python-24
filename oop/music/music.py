
class Music: 
    def __init__(self, bpm: int, instruments: [], lyrics: bool, name: str):
        self.bpm = bpm
        self.instruments = instruments
        self.lyrics = lyrics
        self.name = name
    
    def play(self, song:str):
        return 'the songs name is' + self.name + ' it plays at ' + str(self.bpm) + ' beats per minute and has  ' + self.instruments + ' instruments in it.'