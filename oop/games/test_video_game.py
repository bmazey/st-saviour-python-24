from oop.games.shooter import Shooter
from oop.games.rhythm import Rythym
from oop.games.instrument import Instrument
from oop.games.dance import Dance
from oop.games.piano import Piano
from oop.games.just_dance import Just_Dance
from oop.games.fps import Fps
from oop.games.borderlands import Borderlands

# ^importing all the classes so the test runs ୨୧

# new test for shooter
def test_new_shooter():
    # bl is the shortened version of borderlands 
    # showing that it is a shooter, and has a title
    # the true is for the bool
    # (note to Erika . ݁₊ ⊹ . ݁˖ . ݁) remember how in the () after the __init__ you add the properties and instances?
    # like title: str, and multiplayer: bool??
    # you basically add the examples of those in the () when you start the test
    # like how in the other file self.title was a str
    # here the title of the games is borderlands and you add it in '' cause its a str
    # (end of note to Erika ⋆ ˚｡⋆୨୧˚)
    bl = Shooter('Borderlands', True)
    # list had empty [] so its 0
    assert len(bl.guns) == 0
    # and guns and add the name of the gun (str)
    bl.add_guns('Lady Fist')
    # now theres a gun in the list!. ݁₊ ⊹ . ݁˖ . ݁
    assert len(bl.guns) == 1

# new test for rhythm
def test_new_rhythm():
    # variable representing the example and then the data for it
    ddr = Rythym('Dance Dance Revolution', True)
    # empty list is 0
    assert len(ddr.tracks) == 0
    # add track and song name (str)
    ddr.add_track('Baby One More Time')
    # now theres a track in the sound track! . ݁₊ ⊹ . ݁˖ . ݁-
    assert len(ddr.tracks) == 1
    # ddr instead of the self cause thats the new instance/example
    # then add the name as an str cause we said that self.name: str . ݁₊ ⊹ . ݁˖ . ݁
    assert ddr.title == 'Dance Dance Revolution'

    guitar_hero = Rythym('Guitar Hero', True)
    assert len(guitar_hero.tracks) == 0

    guitar_hero.add_track('Paint it Black')
    assert len(guitar_hero.tracks) == 1

    assert guitar_hero.title == 'Guitar Hero'

# new test for dance⋆ ˚｡⋆୨୧˚
def test_new_dance():
    # put in the data for just dance
    # cause it has the properties
    just_dance = Dance('Just Dance', True, [])
    # empty list
    assert len(just_dance.step) == 0
    # add to list
    # cha cha real smooth ⋆ ˚｡⋆୨୧˚. ݁₊ ⊹ . ݁˖ . ݁
    just_dance.add_step('slide to left') 
    # now the len is one! quick maths
    assert len(just_dance.step) == 1
    # title :3
    assert just_dance.title == 'Just Dance'

# new test
def test_new_instrument():
    # instance of the game and how it fits into the properties that define the class
    rocksmith = Instrument('Rocksmith', True, 2)
    # length of list is 0 (empty)
    assert len(rocksmith.note) == 0
    # add to list
    rocksmith.add_note('middle c')
    # now there is one note in the list
    assert len(rocksmith.note) == 1
    # title . ݁₊ ⊹ . ݁˖ . ݁
    assert rocksmith.title == 'Rocksmith'

    

# new test
def test_new_just_dance():
    # new instance and its properties and data types
    just_dance_2014 = Just_Dance('Just Dance', True, 2, [])
    # empty list
    assert len(just_dance_2014.console) == 0
    # so cool how we already specified add_console is like the same thing as doing an append
    just_dance_2014.add_console('Xbox One')
    # now the lenght is one
    assert len(just_dance_2014.console) == 1

# new test for piano
def test_new_piano():
    # new exaple of an instance of piano game
    # featuring the data types of its properties
    # properties like the title and if its multipayer or not come from one of the parent classes
    piano_keys = Piano('Piano Keys', False, 2, [])
    # empty list
    assert len(piano_keys.scale) == 0
    # adding time!
    piano_keys.add_scale('D Major')
    # no more empty . ݁₊ ⊹ . ݁˖ . ݁⋆ ˚｡⋆୨୧˚
    assert len(piano_keys.scale) == 1

# create new test ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
def test_new_fps():
    # show how the example has the properties
    bl = Fps('Borderlands', True, [])
    # empty list is as long as 0
    assert len(bl.arena) == 0
    # adding time!༄ؘ ۪۪۫۫ ▹▫◃ ۪۪۫۫ ༄ؘ
    bl.add_arena('Fyrestone Coliseum')
    # new length is 1 <3
    assert len(bl.arena) == 1

# create new test ✧༺♥༻∞
def test_new_borderlands():
    # show how example has same properties from the ideal instance of the class
    bl = Borderlands('Borderlands', True, [], [])
    # empty list is 0
    assert len(bl.enemies) == 0
    # adding time!! 
    bl.add_enemies('skag')
    # new length 1 ｡･:*:･ﾟ★,｡･:*:･ﾟ☆
    assert len(bl.enemies) == 1
    
