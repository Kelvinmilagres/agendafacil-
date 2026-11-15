"""Fluxo ponta a ponta: HTTP -> domínio -> persistência (banco SQLite em memória)."""
import pytest
from app import create_app


@pytest.fixture
def client():
    return create_app("sqlite:///:memory:").test_client()


PAYLOAD = {"local": "Salão Fictício", "inicio": "2026-12-05T20:00:00",
           "fim": "2026-12-05T23:00:00", "cache": 1500.0, "situacao": "confirmada"}


def test_cadastra_e_lista(client):
    assert client.post("/apresentacoes", json=PAYLOAD).status_code == 201
    r = client.get("/apresentacoes")
    assert r.status_code == 200 and r.get_json()[0]["local"] == "Salão Fictício"


def test_bloqueia_conflito(client):
    client.post("/apresentacoes", json=PAYLOAD)
    r = client.post("/apresentacoes", json={**PAYLOAD, "inicio": "2026-12-05T22:00:00",
                                            "fim": "2026-12-06T01:00:00"})
    assert r.status_code == 409
