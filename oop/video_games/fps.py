from oop.video_games.shooters import Shooters

class FPS(Shooters):
    # creates the class that defines all first person shooters
    def __init__(self, title: str, multiplayer: bool):
        self.title = title
        self.multiplayer = multiplayer
        super().__init__(title)
    
       # these games have arenas 
        self.arena = []
    
    def empty_arena(self)-> bool:
        # gives back an empty arena
        return len(self.arena) == 0