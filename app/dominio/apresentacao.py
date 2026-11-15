"""Entidade Apresentacao. Não importa Flask nem SQLAlchemy."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Apresentacao:
    local: str
    inicio: datetime
    fim: datetime
    cache: float
    situacao: str = "pendente"  # pendente | confirmada | cancelada (RN02)
    id: int | None = None
