from oop.video_games.fps import FPS

class Borderlands(FPS):

    def spawn_enemy(self, type: str):
        enemy = Borderlands(type)
        self.arena.append(enemy)

    def kill(self):
        if self.empty_arena():
            return ''

        return self.arena.pop(0)