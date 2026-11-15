# AgendaFácil (CSI410 - UFOP/ICEA)
Sistema de agenda, contratações e pagamentos para a banda "6 do Samba". Protótipo acadêmico com dados fictícios.

Equipe: Diego Henrique Marques Magalhães, Kelvin Fernando Milagres de Castro, Laura Andrade Pires.

## Como executar
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
flask --app app run            # SQLite local
DATABASE_URL="mysql+pymysql://user:senha@localhost/agendafacil" flask --app app run   # MySQL
```
## Testes
```
pytest --cov=app
```
O pipeline (GitHub Actions) roda build e testes a cada push em `main` e a cada pull request.

## Estrutura (espelha a visão de módulos)
- `app/dominio`: regras de negócio (sem Flask nem banco)
- `app/persistencia`: adaptador de banco (SQLAlchemy; MySQL ou SQLite)
- `app/web`: rotas HTTP/JSON
- `docs/adr`: registros de decisão
