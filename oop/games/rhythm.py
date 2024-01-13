from oop.games.video_game import VideoGame

class Rythym(VideoGame):
    # title is a string, not all video games are multiplayer
    # wether a game is multiplayer is true or false makes it a bool
    def __init__(self, title: str, multiplayer: bool):
    # use super to get the title and multiplayer properties from the parent class
        super().__init__(title, multiplayer)
    # creating a list for the ideal track
    # the list represents the list of songs in the track
        self.tracks = []

    # soundtrack would be an int to represent the number of songs in the track
    def add_track(self, music: str):
    # appends music to the track, because 
        self.tracks.append(music)                                             
  