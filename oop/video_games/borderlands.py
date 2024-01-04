from oop.video_games.fps import FPS

class Borderlands(FPS):

    def spawn_enemy(self, type: str):
        skag = Borderlands(type)
        self.arena.append(skag)

    def kill(self):
        if self.empty_arena():
            return ''

        return self.arena.pop(0)