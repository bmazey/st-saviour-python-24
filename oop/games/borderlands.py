from oop.games.fps import Fps

# new class under parent class Fps ✧･ﾟ: *✧･ﾟ:*
class Borderlands(Fps):
    # instances and properties of the class
    def __init__ (self, title: str, multiplayer: bool, arena: [], enemies: []):
        # including the properties it inherits from the parent class
        # this is done using super ༶•┈┈⛧┈♛
        super().__init__(title, multiplayer, arena)
        # the ideal instance of the list of enemies in the game is represented by enemies
        self.enemies = enemies

    # create a method to add enemies
    def add_enemies(self, mob: str):
        # mobs are added to the list of the ideal enemies
        self.enemies.append(mob)

