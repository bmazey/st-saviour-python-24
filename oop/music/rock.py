from oop.music.lyric_songs import Lyrics

class Rock(Lyrics):
    """a class that identifies rock music"""
    def __init__(self,title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool, ):
        super().__init__(title, bpm, instruments, lyrics, has_lyrics)
        