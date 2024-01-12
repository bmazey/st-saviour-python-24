from oop.video_games.videogames import VideoGames

# creates the class: Shooters
class Shooters(VideoGames):
   # calls back to the properties of a video game
    def __init__(self, title: str, multiplayer: bool):
        super().__init__(title, multiplayer)
        # empty list of guns
        self.guns = []
        # adds guns to the game
    def add_guns(self, type: str):
        self.guns.append(type)

    # states the amount of players 
    def play(self, players: int)->int:
        # returns the title, the class and the amount of players
        return self.title + "the" + str(self.__class__.__name__) + "has" + players + "amount of players!"