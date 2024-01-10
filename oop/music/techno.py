from oop.music.beats import Beats

class Techno(Beats):
    """a class that identifies techno music"""
    def __init__(self, title: str, bpm: int, instruments: [], no_lyrics: bool, synthesizers: str):
        super().__init__(title, bpm, instruments,no_lyrics)
        self.futuristic_themes = True
        self.synthesizers = synthesizers

    def __str__(self):
        return f'title: {self.title} bpm: {self.bpm} instruments: {self.instruments} no lyrics: {self.no_lyrics} synthesizers: {self.synthesizers}'