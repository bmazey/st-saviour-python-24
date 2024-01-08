from oop.video_games import VideoGames

class Shooters(VideoGames):
# creates the class: Shooters
    def __init__(self, title):
        super().__init__(title)
        # calls back to the properties of a video game
        self.guns = True
        # sees if the game has guns

    def play(self, players: int)->int:
        # states the amount of players 
        return self.title + "the" + str(self.__class__.__name__) + "has" + players + "amount of players!"
        # returns the title, the class and the amount of players