"""Módulo pagamentos (H06; RN05). Segredo: como o valor restante do cachê é calculado.
Implementado na Etapa 3."""
from dataclasses import dataclass


@dataclass
class ResumoPagamento:
    """Estrutura planejada para acompanhamento de cachê, valor pago e restante (RN05)."""
    valor_total: float
    valor_pago: float

    @property
    def valor_restante(self) -> float:
        return max(0.0, self.valor_total - self.valor_pago)