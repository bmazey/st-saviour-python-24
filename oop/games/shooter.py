from oop.games.video_game import VideoGame

# new class under VideoGame
class Shooter(VideoGame):


    def __init__(self, title: str, multiplayer: bool):
        super().__init__(title, multiplayer)
        # list to represent all guns in the game
        self.guns = []

    # is an integer because there is a number of players
    def play(self,players:int) ->int:
        #  makes a statement showing the title of the game and its amount of players
        return self.title + "the" + str(self.__class__.name__) + "has" + players + "amount of players"
    
    # now new guns can be added to the list
    def add_guns(self, weapons: str):
        # adding weapons to the list of guns
        # cause guns are weapons
        self.guns.append(weapons)
        