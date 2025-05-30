from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_root_deve_retornar_ola_mundo():
    """Esse teste tem 3 etapas (AAA)
    - A: Arrange    - Arranjo
    - A: Act        - Executa o Suit
    - A: Assert     - Garanta que A seja igual A"""

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'Message': 'Olá mundo'}
    assert response.status_code == HTTPStatus.OK


def test_root_deve_retornar_ola_mundo_html():
    """Esse teste tem 3 etapas (AAA)
    - A: Arrange    - Arranjo
    - A: Act        - Executa o Suit
    - A: Assert     - Garanta que A seja igual A"""

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/olamundo')

    # Assert
    assert '<h1>Olá Mundo</h1>' in response.text
    assert response.status_code == HTTPStatus.OK
