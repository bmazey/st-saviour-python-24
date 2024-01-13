from oop.games.shooter import Shooter

# new class inherting from shooter *:･ﾟ✧*:･ﾟ✧
class Fps(Shooter):
    # def __init__ used to show the ideal instances and properties
    def __init__ (self, title: str, multiplayer: bool, arena: []):
        # super shows properties inherted from parent class
        super().__init__(title, multiplayer)
        # the ideal arena is represented by arena
        self.arena = arena
    # method created to add arenas
    def add_arena(self, setting: str):
        # since arenas are a place/setting in the game it goes in the list of arenas ♥*♡∞:｡.｡
        self.arena.append(setting)
