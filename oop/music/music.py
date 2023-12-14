class Music:
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: bool):
        self.title = title
        self.bpm = bpm
        self.instruments = instruments 
        self.lyrics = lyrics 


    def play(self) -> str:
        return self.title + 'is a song that plays at' + str(self.bpm) + 'beats per minute with' + str(*self.instruments)