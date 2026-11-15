from datetime import datetime, timedelta
from app.dominio.apresentacao import Apresentacao
from app.dominio.conflitos import ha_conflito


def show(h1, h2, sit="confirmada"):
    d = datetime(2026, 12, 5)
    return Apresentacao("Local", d + timedelta(hours=h1), d + timedelta(hours=h2), 1000, sit)


def test_sobreposicao_gera_conflito():
    assert ha_conflito(show(20, 23), [show(22, 24)])


def test_limite_exato_nao_conflita():
    assert not ha_conflito(show(22, 24), [show(20, 22)])


def test_show_cancelado_nao_bloqueia():
    assert not ha_conflito(show(20, 23), [show(20, 23, "cancelada")])


def test_show_pendente_nao_bloqueia():
    assert not ha_conflito(show(20, 23), [show(20, 23, "pendente")])


def test_show_dentro_de_outro_gera_conflito():
    assert ha_conflito(show(21, 22), [show(20, 23)])
  
