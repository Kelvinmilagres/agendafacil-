"""Regra de dependência (ADR-002): o domínio não importa Flask, SQLAlchemy, web nem persistência."""
import pathlib
import re

PROIBIDOS = re.compile(r"^\s*(from|import)\s+(flask|sqlalchemy|pymysql|app\.web|app\.persistencia)", re.M)


def test_dominio_nao_depende_de_infraestrutura():
    raiz = pathlib.Path(__file__).resolve().parent.parent / "app" / "dominio"
    violacoes = [str(p) for p in raiz.rglob("*.py") if PROIBIDOS.search(p.read_text(encoding="utf-8"))]
    assert violacoes == []


def test_persistencia_nao_depende_de_web():
    raiz = pathlib.Path(__file__).resolve().parent.parent / "app" / "persistencia"
    proib_web = re.compile(r"^\s*(from|import)\s+(flask|app\.web)", re.M)
    violacoes = [str(p) for p in raiz.rglob("*.py") if proib_web.search(p.read_text(encoding="utf-8"))]
    assert violacoes == []