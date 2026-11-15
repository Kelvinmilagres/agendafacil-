"""Casos de uso da agenda. Depende só da interface Repositorio (porta)."""
from typing import Protocol
from app.dominio.apresentacao import Apresentacao
from app.dominio.conflitos import ha_conflito


class Repositorio(Protocol):
    def salvar(self, a: Apresentacao) -> Apresentacao: ...
    def listar(self) -> list[Apresentacao]: ...


class ErroDominio(Exception):
    pass


class ServicoAgenda:
    def __init__(self, repo: Repositorio):
        self._repo = repo

    def cadastrar(self, a: Apresentacao) -> Apresentacao:
        if not a.local or a.fim <= a.inicio or a.cache < 0:
            raise ErroDominio("Dados da apresentação inválidos.")
        if a.situacao == "confirmada" and ha_conflito(a, self._repo.listar()):
            raise ErroDominio("Conflito de horário com outro show confirmado.")
        return self._repo.salvar(a)

    def listar(self) -> list[Apresentacao]:
        return sorted(self._repo.listar(), key=lambda x: x.inicio)
