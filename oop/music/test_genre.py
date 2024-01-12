from oop.music.electro import Electro
from oop.music.bossa_nova import Bossa_Nova
from oop.music.instrumental_song import Instrumental
from oop.music.lyrical_songs import Lyrical
from oop.music.music import Music

def test_electro():
    daft_punk = Electro('Get Lucky', 90, ['synthetizer, percussion, piano'], 'synthetizer', False)
    assert daft_punk.beatbox() == 'Get Lucky is an electro song because its leading instrument is a synthetizer'

    assert isinstance(daft_punk, Instrumental)
    assert isinstance(daft_punk, Music)
    
    assert str(daft_punk) == 'title: Get Lucky bpm: 90 instruments: [\'synthetizer, percussion, piano\'] leading instrument: synthetizer'

    assert daft_punk.bpm == 90
    assert daft_punk.has_lyrics == False

   
def test_bossa():
    astrud = Bossa_Nova('girl from impanema', 40, ['guitar, saxophone, percussion'], 'acoustic guitar', 'tall and tan and young and lovely', True, 'womp womp')
    assert astrud.gilberto() == 'girl from impanema is a bossa nova song because of its acoustic guitar and lyrics'
    
    assert isinstance(astrud, Lyrical)
    assert isinstance(astrud, Music)

    assert astrud.bpm == 40
    assert astrud.has_lyrics == True
