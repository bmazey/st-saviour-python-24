from oop.video_games.fps import FPS

def tst_new_fps():
    bl = FPS('Borderlands', True, [])
    assert len(bl.arena) == 0
    bl.add_arena('Fyrestone Coliseum')
    assert len(bl.arena) == 1