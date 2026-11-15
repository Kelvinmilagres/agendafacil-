"""RN01: verificação de conflito de horários (segredo: como o conflito é detectado)."""
from app.dominio.apresentacao import Apresentacao


def ha_conflito(nova: Apresentacao, existentes: list[Apresentacao]) -> bool:
    """Dois shows conflitam se os intervalos se sobrepõem.
    Intervalos são [inicio, fim): terminar às 22h e começar às 22h NÃO conflita."""
    for e in existentes:
        if e.situacao != "confirmada":
            continue
        if nova.inicio < e.fim and e.inicio < nova.fim:
            return True
    return False
