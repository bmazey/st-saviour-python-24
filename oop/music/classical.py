from oop.music.beats import Beats

class Classical(Beats):
    def __init__(self, title: str, bpm: int, instruments: [], no_lyrics: bool, brass: bool, brass_instrument: str):
        super().__init__(title, bpm, instruments, no_lyrics)
        self.brass = brass
        self.brass = True
        self.brass_instrument = brass_instrument

def conduct(self) -> str:
    return 'the song ' + self.title + ' has the brass instrument ' + self.brass_instrument