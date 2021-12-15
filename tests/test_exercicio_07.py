import pytest
from src.exercicio_07 import Data


@pytest.mark.parametrize('input, result', [
    ((11,8,2001), "11/8/2001")
])
def test_verificar_se_o_texto_esta_certo(input, result):
    assert Data(input[0],input[1],input[2]).__str__() == result
    

@pytest.mark.parametrize('input, result', [
    ((11,8,2001), 3)
])
def test_verificar_se_existem_3_entradas(input, result):
    assert len(input) == result