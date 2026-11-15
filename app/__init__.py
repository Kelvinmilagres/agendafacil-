"""AgendaFácil - fábrica da aplicação (composição dos módulos)."""
import os
from flask import Flask
from app.persistencia.repositorio import RepositorioSQL
from app.dominio.servico import ServicoAgenda
from app.web.rotas import criar_blueprint


def create_app(database_url: str | None = None) -> Flask:
    app = Flask(__name__)
    url = database_url or os.environ.get("DATABASE_URL", "sqlite:///agendafacil.db")
    repo = RepositorioSQL(url)
    servico = ServicoAgenda(repo)
    app.register_blueprint(criar_blueprint(servico))
    return app
