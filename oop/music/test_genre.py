from oop.music.electro import Electro
from oop.music.bossa_nova import Bossa_Nova

def test_electro():
    daft_punk = Electro('Get Lucky', 90, ['synthetizer, percussion, piano'], 'synthetizer', False)
    assert daft_punk.beatbox() == 'Get Lucky is an electro song because its leading instrument is a synthetizer'

def test_bossa():
    astrud = Bossa_Nova('girl from impanema', 40, ['guitar, saxophone, percussion'], 'acoustic guitar', 'tall and tan and young and lovely', True, 'womp womp')
    assert astrud.gilberto() == 'girl from impanema is a bossa nova song because of its acoustic guitar and lyrics'