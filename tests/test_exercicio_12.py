import pytest
from src.exercicio_12 import DateBirthday
from datetime import datetime,date

# @pytest.mark.parametrize('input', [
#     ( datetime.strptime( "11/8/2001", "%d/%m/%Y").date())
# ])
@pytest.mark.parametrize('input', [
    (( "11/8/2001"))
])

def test_verificar_data(input):
    app = DateBirthday()
    assert app.get_birthdate(input) == (11,8,2001)


def test_verificar_input(input = "20-09-1980"):
    with pytest.raises(ValueError):
        app = DateBirthday()
        assert app.get_birthdate(input) 