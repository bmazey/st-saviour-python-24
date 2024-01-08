from oop.video_games.shooters import Shooters

class FPS(Shooters):
    # creates the class that defines all first person shooters
    def __init__(self, name):
        super().__init__(name)
    
       # these games have arenas 
        self.arena = []
    
    def empty_arena(self)-> bool:
        # gives back an empty arena
        return len(self.arena) == 0