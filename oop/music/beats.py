from oop.music.music import Music

class Beats(Music):
    def __init__(self, title: str, bpm: int, instruments: [], no_lyrics: bool):
        super().__init__(title, bpm, instruments, False)
        self.no_lyrics = no_lyrics 
        self.no_lryics = False

    def headbop(self) -> str:
        return 'it is ' + str(self.no_lryics) + ' that the song ' + self.title + ' has lyrics'