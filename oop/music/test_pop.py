from oop.music.pop import Pop

def test_pop():
    dance = Pop('Believer',125 , ['drums'], 'Pain! You break me down, you build me up Believer, Believer', True, True, 'Pain! You made me a, you made me a believer, believer')
    assert dance.sing() == 'the song Believer has the lyrics: Pain! You break me down, you build me up Believer, Believer'
    assert dance.play() == 'Believer is a song that plays at 125 beats per minute with drums'
    assert dance.belt() == 'the song Believer has the cachy lyrics: Pain! You made me a, you made me a believer, believer'