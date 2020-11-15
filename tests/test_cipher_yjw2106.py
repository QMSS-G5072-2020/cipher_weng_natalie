from cipher_yjw2106 import cipher_yjw2106
    
def test_cipher():
    assert cipher('animal', 0) == 'animal', "Expected outcome: animal"
    assert cipher('animal', 2) == 'cpkocn', "Expected outcome: cpkocn"
    assert cipher('sum', 10) == 'DFw', "Expected outcome: DFw"