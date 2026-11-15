"""Adaptador de persistência (segredo: qual banco é usado e como mapear)."""
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool
from app.dominio.apresentacao import Apresentacao

Base = declarative_base()


class ApresentacaoModel(Base):
    __tablename__ = "apresentacoes"
    id = Column(Integer, primary_key=True)
    local = Column(String(200), nullable=False)
    inicio = Column(DateTime, nullable=False)
    fim = Column(DateTime, nullable=False)
    cache = Column(Float, nullable=False)
    situacao = Column(String(20), nullable=False, default="pendente")


class RepositorioSQL:
    """Implementação SQLAlchemy da porta Repositorio (protege C03; suporta MySQL e SQLite)."""

    def __init__(self, url: str):
        kwargs = {}
        if url.startswith("sqlite") and ":memory:" in url:
            kwargs = {"connect_args": {"check_same_thread": False}, "poolclass": StaticPool}
        self._engine = create_engine(url, **kwargs)
        Base.metadata.create_all(self._engine)
        self._Session = sessionmaker(bind=self._engine)

    def salvar(self, a: Apresentacao) -> Apresentacao:
        with self._Session() as s:
            m = ApresentacaoModel(local=a.local, inicio=a.inicio, fim=a.fim,
                                  cache=a.cache, situacao=a.situacao)
            s.add(m)
            s.commit()
            a.id = m.id
        return a

    def listar(self) -> list[Apresentacao]:
        with self._Session() as s:
            return [Apresentacao(m.local, m.inicio, m.fim, m.cache, m.situacao, m.id)
                    for m in s.query(ApresentacaoModel).all()]