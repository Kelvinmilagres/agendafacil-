"""Camada web (segredo: formato HTTP/JSON). Só chama o ServicoAgenda."""
from datetime import datetime
from flask import Blueprint, jsonify, request
from app.dominio.apresentacao import Apresentacao
from app.dominio.servico import ServicoAgenda, ErroDominio


def criar_blueprint(servico: ServicoAgenda) -> Blueprint:
    bp = Blueprint("agenda", __name__)

    @bp.get("/saude")
    def saude():
        return jsonify(status="ok")

    @bp.post("/apresentacoes")
    def cadastrar():
        d = request.get_json(force=True)
        try:
            a = Apresentacao(d["local"], datetime.fromisoformat(d["inicio"]),
                             datetime.fromisoformat(d["fim"]), float(d["cache"]),
                             d.get("situacao", "pendente"))
            salvo = servico.cadastrar(a)
        except (KeyError, ValueError):
            return jsonify(erro="Requisição inválida."), 400
        except ErroDominio as e:
            return jsonify(erro=str(e)), 409
        return jsonify(id=salvo.id), 201

    @bp.get("/apresentacoes")
    def listar():
        return jsonify([{"id": a.id, "local": a.local, "inicio": a.inicio.isoformat(),
                         "fim": a.fim.isoformat(), "cache": a.cache,
                         "situacao": a.situacao} for a in servico.listar()])

    return bp
