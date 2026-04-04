from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    with patch("app.main.check_db_connection", new_callable=AsyncMock, return_value=True):
        with TestClient(app) as c:
            yield c


def test_health_connected(client):
    with patch("app.main.check_db_connection", new_callable=AsyncMock, return_value=True):
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "db": "connected"}


def test_health_db_unreachable(client):
    with patch("app.main.check_db_connection", new_callable=AsyncMock, return_value=False):
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["db"] == "unreachable"
