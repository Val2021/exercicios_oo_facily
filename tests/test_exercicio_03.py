import pytest
from src.exercicio_03 import Pair

@pytest.mark.parametrize('input,result',[
    (5,False)
])

def test_verificar_numero_par(input,result):
    par = Pair()
    assert par.is_par(input) == result
    

    