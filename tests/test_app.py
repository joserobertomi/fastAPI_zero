from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organizacao do teste)

    response = client.get('/')  # Act (acao)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Fala comigo mundo!'}  # Assert
