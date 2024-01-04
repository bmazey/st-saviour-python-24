from oop.music.pop import Pop
from oop.music.rock import Rock

def test_pop():
    dance = Pop('Believer',125 , ['drums'], 'Pain! You break me down, you build me up Believer, Believer', True, True, 'Pain! You made me a, you made me a believer, believer')
    assert dance.sing() == 'the song Believer has the lyrics: Pain! You break me down, you build me up Believer, Believer'
    assert dance.play() == 'Believer is a song that plays at 125 beats per minute with drums'
    assert dance.belt() == 'the song Believer has the cachy lyrics: Pain! You made me a, you made me a believer, believer'

def test_rock():
    mosh = Rock('T.N.T.',123 , ['electric guitar'], 'Cause Im T.N.T., Im dynamite', True, True, 'T.N.T., Im a power load T.N.T., watch me explode')
    assert mosh.sing() == 'the song T.N.T. has the lyrics: Cause Im T.N.T., Im dynamite'
    assert mosh.play() == 'T.N.T. is a song that plays at 123 beats per minute with electric guitar'
    assert mosh.rip() == 'the song T.N.T. screams the lyrics: T.N.T., Im a power load T.N.T., watch me explode'