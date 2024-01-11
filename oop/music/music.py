
class Music:
    """A class that define music"""

    # defining that all music has a title, a bpm, and instruments
    # defining that all music has or does not have lyrics, which is a passed on boolean
    def __init__(self, title: str, bpm: int, instruments: [], lyrical: bool):
        
        self.title = title
        self.bpm = bpm
        self.instruments = instruments
        self.lyrical = lyrical
        
    # play is an instance of music 
    def play(self):
        play = 'This song is called ' + self.title + '. This song plays at ' + str(self.bpm) + ' bpm with '
        
        # converting the list of instruments into a string that is legible
        for instrument in self.instruments:
            play += instrument 
            play += ', '
        return play[:-2]