from oop.video_games.arcade import Arcade

class Retro(Arcade):
    def __init__(self, name):
        super().__init__(name)
    
        self.maze = []
    
    def empty_maze(self)-> bool:
        return len(self.maze) == 0