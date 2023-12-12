class Music:
    def __init__(self, bpm: int, instruments: str, lyrics: bool, name: str):
        self.bpm = bpm
        self.instruments = instruments 
        self.lyrics = lyrics 
        self.name = name

    def play(self, song: str):
        return song + 'is a song that plays at' + self.bpm + 'with' + self.instruments + 'has lyrics' + self.lyrics(True)