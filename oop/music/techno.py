from oop.music.beats import Beats

class Techno(Beats):
    """a class that identifies techno music"""
    def __init__(self, title: str, bpm: int, instruments: [], no_lyrics: bool, futuristic_themes: bool, synthesizers: str):
        super().__init__(title, bpm, instruments,no_lyrics)
        self.futuristic_themes = futuristic_themes
        self.futuristic_themes = True
        self.synthesizers = synthesizers

    def produce(self) -> str:
        return 'the song ' + self.title + ' creates futuristic themes by using the ' + self.synthesizers