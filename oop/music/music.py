
class Music:
    def __init__(self, name: str, bpm: int, instruments: [], lyrical: bool):
        self.bpm = bpm
        self.instruments = instruments
        self.lyrical = lyrical
        self.name = name
    
    def play(self):
        play = 'This song is called ' + self.name + '. This song plays at ' + str(self.bpm) + ' bpm with '
        for instrument in self.instruments:
            play += instrument 
            play += ', '
        return play[:-2]