from oop.music.electro import Electro

def test_genre():
    daft_punk = Electro('Get Lucky', 90, ['synthetizer, percussion, piano'], 'synthetizer', False)
    assert daft_punk.beatbox() == 'Get Lucky is an electro song because its leading instrument is a synthetizer'