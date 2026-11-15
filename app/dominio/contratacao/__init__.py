"""Módulo contratacao (H04, H05; RN02, RN03, RN04). Segredo: regras de sinal, prazo e
cancelamento por tipo de evento. Implementado na Etapa 3/4 (padrão Strategy)."""
from typing import Protocol


class PoliticaContratacao(Protocol):
    """Porta Strategy para regras de sinal e prazo por tipo de evento (ADR-004)."""
    def percentual_sinal(self) -> float: ...
    def dias_antecedencia_cancelamento(self) -> int: ...