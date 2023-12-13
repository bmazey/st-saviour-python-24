class Music:
    def __init__(self, bpm: int, instruments: str, lyrics: bool, name: str):
        self.bpm = bpm
        self.instruments = instruments 
        self.lyrics = lyrics 
        self.name = name

    def play(self, song: str):
        return song + self.name + 'is a song that plays at' + self.bpm + 'bpm with' + self.instruments