from oop.music.lyric_songs import Lyrics

class Pop(Lyrics):
    """a class that identifies pop music"""
    def __init__(self,title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool, cachy: bool, memorable_lyrics: str):
        super().__init__(title, bpm, instruments, lyrics, has_lyrics)
        self.cachy = cachy
        self.cachy
        self.memorable_lyrics = memorable_lyrics