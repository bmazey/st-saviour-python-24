class Music:
    def __init__(self, title: str, bpm: int, instruments: []):
        self.title = title
        self.bpm = bpm
        self.instruments = instruments

    def play(self)-> str:
        return self.title + ' is a song that plays at ' + str(self.bpm) + ' beats per minute with ' + str(self.instruments)
        play += instruments
        play += ', '