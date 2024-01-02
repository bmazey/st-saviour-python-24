from oop.video_games import VideoGames

class Arcade(VideoGames):

    def __init__(self, title):
        super().__init__(title)
        self.physical = True

    def play(self, players: int)->int:
        return self.title + "the" + str(self.__class__.__name__) + "has" + players + "amount of players!"