from oop.music.lyrical_songs import Lyrical

class Jazz(Lyrical):

    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool, improv_lyrics: str):
        super().__init__(title, bpm, instruments, lyrics, has_lyrics)