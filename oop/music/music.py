
class Music:
    def __init__(self, title: str, bpm: int, instruments: [], lyrical: bool):
        self.title = title
        self.bpm = bpm
        self.instruments = instruments
        self.lyrical = lyrical
        
    
    def play(self):
        play = 'This song is called ' + self.title + '. This song plays at ' + str(self.bpm) + ' bpm with '
        for instrument in self.instruments:
            play += instrument 
            play += ', '
        return play[:-2]