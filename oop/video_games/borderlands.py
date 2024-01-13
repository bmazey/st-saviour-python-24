from oop.video_games.fps import FPS

class Borderlands(FPS):
    def __init__(self, title: str, multiplayer: bool):
        super().__init__(title, multiplayer)
        self.arena = []
    # a skag (one type of enemy) spawns in the arena
    def spawn_enemy(self, enemy_type: str):
        skag = Borderlands(enemy_type, multiplayer = True)
        self.arena.append(skag)

    # you kill the skags
    def kill(self):
        if self.empty_arena():
            return "The arena is empty"

    # the arena is empty 
        return self.arena.pop(0)