from oop.music.lyric_songs import Lyrics

class Rock(Lyrics):
    """a class that identifies rock music"""
    def __init__(self,title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool, screaming: bool, screaming_lyrics: str):
        super().__init__(title, bpm, instruments, lyrics, has_lyrics)
        self.screaming = screaming
        self.screaming = True
        self.screaming_lyrics = screaming_lyrics

    def rip(self) -> str:
        return 'the song ' + self.title + ' screams the lyrics: ' + self.screaming_lyrics