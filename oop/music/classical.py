from oop.music.beats import Beats

class Classical(Beats):
    """a class that identifies classical music"""
    def __init__(self, title: str, bpm: int, instruments: [], no_lyrics: bool, woodwind: bool, woodwinds:str):
        super().__init__(title, bpm, instruments,no_lyrics)
        self.woodwind = woodwind
        self.woodwind = True
        self.woodwinds = woodwinds

    def conduct(self) -> str:
        return 'the song ' + self.title + ' has the woodwind instrument: ' + self.woodwinds