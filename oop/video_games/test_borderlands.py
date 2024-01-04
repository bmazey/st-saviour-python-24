from oop.shooters.borderlands import Borderlands

def test_new_borderlands():
    skag = Borderlands('Skag')

    # start by asserting empty arena
    assert enemy.empty_arena()

    # add some enemies to the arena!
    enemy.spawn_enemy('skag whelp')
    enemy.spawn_enemy('skag')
    enemy.spawn_enemy('adult skag')

    # attempt to kill
    skag = enemy.kill()

    # assert properties of a skag
    assert isinstance(skag, Borderlands)
    assert skag.name == 'Skag'

    # assert properties of all eggs in emma's nest
    for enemy in enemy.arena:
        assert enemy.gun
        assert isinstance(enemy, Borderlands)

    # kill all enemies
    enemy.kill()
    enemy.kill()

    # check corner case using hatch() on empty nest
    assert enemy.kill() == ''

    # verify arena is empty
    assert enemy.empty_arena()
