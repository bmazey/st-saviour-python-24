from oop.video_games.rhythm import Rhythm
from oop.video_games.shooters import Shooters

def test_shooters():
    borderlands = Shooters('Borderlands', True)
    assert len(borderlands.guns) == 0

    borderlands.add_guns('Lady Fist')
    assert len(borderlands.guns) == 1


def test_new_rhythm():
    ddr = Rhythm('Dance Dance Revolution', True)
    assert len(ddr.tracks) == 0

    ddr.add_tracks('Baby One More Time')
    assert len(ddr.tracks) == 1

    assert ddr.title == 'Dance Dance Revolution'

    guitar_hero = Rhythm('Guitar Hero', True)
    assert len(guitar_hero.tracks) == 0

    guitar_hero.add_tracks('Paint it Black')
    assert len(guitar_hero.tracks) == 1