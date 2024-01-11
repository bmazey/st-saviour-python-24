from oop.music.music import Music

class Lyrical(Music):
    """A class that defines music with lyrics"""

    # Assigning previous properties of music to new Lyrical class. 
    # Adding a string with lyrics
    def __init__(self, title: str, bpm: int, instruments: [], lyrics: str, has_lyrics: bool):
        super().__init__(title, bpm, instruments, True)
        
        self.lyrics = lyrics
        self.has_lyrics = has_lyrics
        self.has_lyrics = True 

    # Sing is an instance of Lyrical
    def sing(self):
        return 'artist sings ' + self.title + ' with lyrics: ' + self.lyrics
