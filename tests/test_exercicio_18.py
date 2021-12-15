import pytest
from src.exercicio_18 import Carro




# @pytest.fixture
# def obter_gas():
#     go = Carro()
#     qtd_gas =  go.obterGasolina(10) 
#     return qtd_gas


@pytest.mark.parametrize('input, result', [
    (10,20)
])
def test_adiciona_gas(input,result):
    go = Carro()
    qtd =  go.adicionarGasolina(input) 
    qtd += qtd
    assert qtd == result


