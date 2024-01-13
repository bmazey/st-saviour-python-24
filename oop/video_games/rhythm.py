from oop.video_games.videogames import VideoGames

# creates the class: Rhythm
class Rhythm(VideoGames):
    def __init__(self, title: str, multiplayer: bool):
         # calls back to the properties of a video game
        super().__init__(title, multiplayer)
        # makes an empty list
        self.tracks = []
        # adds songs to the game
    def add_tracks(self, music: str):
        self.tracks.append(music)