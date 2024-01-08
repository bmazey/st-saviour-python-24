from oop.video_games.fps import FPS

class Borderlands(FPS):

 # a skag (one type of enemy) spawns in the arena
    def spawn_enemy(self, type: str):
        skag = Borderlands(type)
        self.arena.append(skag)

    # you kill the skags
    def kill(self):
        if self.empty_arena():
            return ''

    # the arena is empty 
        return self.arena.pop(0)