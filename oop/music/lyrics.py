from oop.music.music import Music

class Lyrics(Music):
    """a new class that identifies that music has lyrics"""
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: bool):
        super().__init__(title, bpm, instruments)

        # identifies that a song with lyrics is a bool returning True. 
        self.lyrics = True

    def play(self) -> str:
        return 'it is ' + str(self.lyrics) + ' that ' + str(self.title) + ' has lyrics and plays with ' + str(self.instruments) + ' at ' + str(self.bpm) + ' beats per minute'