from oop.video_games.rhythm import Rhythm
from oop.video_games.shooters import Shooters

def test_shooters():
    borderlands = Shooters('Borderlands', True)
    assert len(bl.gun) == 0

    bl.add_gun('Lady Fist')
    assert len(bl.gun) == 1

    from oop.video_games.rhythm import Rhythm

def test_new_rhythm():
    ddr = Rhythm('Dance Dance Revolution', True)
    assert len(ddr.tracks) == 0

    ddr.add_track('Baby One More Time')
    assert len(ddr.tracks) == 1

    assert ddr.title == 'Dance Dance Revolution'

    guitar_hero = Rhythm('Guitar Hero', True)
    assert len(guitar_hero.tracks) == 0

    guitar_hero.add_track('Paint it Black')
    assert len(guitar_hero.tracks) == 1