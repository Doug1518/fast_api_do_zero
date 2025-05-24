from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_do_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """Esse teste tem 3 etapas (AAA)
        - A: Arrange    - Arranjo
        - A: Act        - Executa o Suit
        - A: Assert     - Garanta que A seja igual A"""

    # Arrange
    client = TestClient(app)

    # Act
    reponse = client.get('/')

    # Assert
    assert reponse.json() == {'Message': 'Olá mundo'}
    assert reponse.status_code == HTTPStatus.OK
