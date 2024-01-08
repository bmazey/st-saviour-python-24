from oop.video_games import VideoGames

class Arcade(VideoGames):

    def __init__(self, title):
        super().__init__(title)
        self.coins = True

    def play(self, coins: int)->int:
        return self.title + "the" + str(self.__class__.__name__) + "uses" + coins + "amount of coins!"