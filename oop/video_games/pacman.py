from oop.video_games.arcade import Arcade

class Pac_Man(Arcade):

    def spawn_berry(self, name: str):
        """adds a berry to the maze"""
        berry = Pac_Man(name)
        # names the berry that spawns
        self.maze.append(berry)

    def eat(self):
        """removes and returns first berry in maze using list.pop()"""
        # check to see if berries were eaten
        if self.empty_maze():
            return ''

        return self.maze.pop(0)
