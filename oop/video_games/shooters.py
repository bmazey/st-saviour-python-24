from oop.video_games import VideoGames

# creates the class: Shooters
class Shooters(VideoGames):

    def __init__(self, title):
         # calls back to the properties of a video game
        super().__init__(title)
        # sees if the game has guns
        self.guns = True
        # adds guns to the game
    def add_guns(self, type: str):

        def play(self, players: int)->int:
        # states the amount of players 
            return self.title + "the" + str(self.__class__.__name__) + "has" + players + "amount of players!"
        # returns the title, the class and the amount of players
    