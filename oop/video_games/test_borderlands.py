from oop.video_games.borderlands import Borderlands

def test_new_borderlands():
    enemy = Borderlands('Borderands 2', multiplayer = True)
    # start by asserting empty arena
    assert enemy.empty_arena()

    # add some enemies to the arena!
    enemy.spawn_enemy('skag whelp')
    enemy.spawn_enemy('skag')
    enemy.spawn_enemy('spitter skag')

    # attempt to kill
    skag = enemy.kill()

    # assert properties of a skag
    assert isinstance(skag, Borderlands)
    assert skag.name == 'Skag'

    # assert properties of all skags in the arena
    for enemy in enemy.arena:
        assert enemy.guns
        assert isinstance(enemy, Borderlands)

    # kill all enemies
    enemy.kill()
    enemy.kill()

    # check corner case using kill() on empty arena
    assert enemy.kill() == ''

    # verify arena is empty
    assert enemy.empty_arena()
