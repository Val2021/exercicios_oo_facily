import pytest
from src.exercicio_01 import Aluno, Nota


@pytest.mark.parametrize('input, result', [
    ([5, 6, 3, 7], 5.25)
])
def test_verificar_media(input, result):
    aluno = Aluno(4)
    aluno.inserir_notas(5)
    aluno.inserir_notas(6)
    aluno.inserir_notas(3)
    aluno.inserir_notas(7)
    assert aluno.get_media() == result