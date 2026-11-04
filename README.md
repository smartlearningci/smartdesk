# SmartDesk — MVP de Gestão de Suporte

Aplicação pedagógica da NexaServ. Especificação aprovada em [docs](docs/) e cenários em [features/tickets.feature](features/tickets.feature).

## Executar localmente (Python 3.11+)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SMARTDESK_SESSION_SECRET="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
python -m scripts.create_demo_users
uvicorn src.main:app --reload
```

Abrir http://127.0.0.1:8000/login. Contas: `ana@nexaserv.test`, `miguel@nexaserv.test`, `sofia@nexaserv.test`; palavras-passe escolhidas no script.

## Testes

```bash
pytest -v
```

A implementação inicial inclui testes de regras de negócio. **Não foram ainda executados nesta publicação**. Permanecem por implementar/validar a suíte completa de 20 testes, os 12 cenários BDD, medição RNF-002 e compatibilidade Chrome/Edge. A sessão é assinada, mas a versão local não tem ainda proteção CSRF nem configuração de HTTPS: **não expor à Internet**.

## Estrutura

- `src/main.py`: interface HTML e rotas FastAPI.
- `src/services.py`: permissões e estados dos tickets.
- `src/database.py`: SQLite.
- `src/auth.py`: hash de palavras-passe e autenticação.
- `scripts/create_demo_users.py`: contas fictícias.
- `tests/test_mvp.py`: testes iniciais.
- `docs/` e `features/`: requisitos e aceitação aprovados.

## Próximos passos

Completar e executar testes unitários, integração e BDD, elaborar relatório global e só depois avançar para Docker, Compose, CI/CD e cloud. Não há funcionalidades de negócio fora do MVP.
