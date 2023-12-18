from oop.video_games.shooters import Shooters

class FPS(Shooters):
    def __init__(self, name):
        super().__init__(name)
    
        self.arena = []
    
    def empty_arena(self)-> bool:
        return len(self.arena) == 0