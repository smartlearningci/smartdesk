# SmartDesk — Sistema de Gestão de Pedidos de Suporte

Projeto pedagógico da NexaServ: aplicação FastAPI, HTML simples e SQLite. Nesta sessão utiliza-se **Docker e Docker Compose**; não é necessário instalar Python, FastAPI ou SQLite no computador.

A [especificação aprovada](docs/produto/03_mvp_backlog_e_aceitacao.md), os [testes e a rastreabilidade](docs/qualidade/01_testes_e_rastreabilidade.md) e os [cenários Gherkin](features/tickets.feature) permanecem como referência.

## Funcionalidades do MVP

- **Ana**, colaboradora: cria e consulta os próprios tickets; comunica quando um problema Resolvido persiste.
- **Miguel**, técnico: consulta tickets atribuídos, inicia o tratamento e regista a resolução.
- **Sofia**, responsável de TI: consulta todos os tickets, atribui ou reatribui técnicos e fecha os Resolvidos depois de verificar a solução (sem confirmação formal obrigatória de Ana).
- Estados: **Aberto → Em tratamento → Resolvido → Fechado**; **Resolvido → Em tratamento** é permitido; **Fechado** não reabre.
- Categorias: **Equipamento, Software, Acessos**. Título, descrição e categoria são obrigatórios.

## Preparar e executar — apenas Docker Compose

**Pré-requisito:** Docker com Docker Compose disponível e a funcionar (contentores Linux). Os comandos seguintes são executados na pasta do projeto. Não é necessário Python local.

### 1. Obter o repositório

```bash
git clone https://github.com/smartlearningci/smartdesk.git
cd smartdesk
```

Se já tiver o repositório clonado, entre na pasta e execute `git pull`.

### 2. Preparar a configuração local

```bash
cp .env.example .env
```

O exemplo já contém uma **chave de sessão fictícia** com mais de 32 caracteres. Não é necessário gerar outra chave para esta demonstração local. A chave `SMARTDESK_SESSION_SECRET` serve para assinar os cookies da aplicação; **não é uma palavra-passe de utilizador**. O ficheiro `.env` é ignorado pelo Git e pelo build Docker.

### 3. Construir a imagem

```bash
docker compose build
```

O `Dockerfile` instala as dependências Python **dentro da imagem**, incluindo Jinja2 para os templates HTML.

### 4. Criar os utilizadores de demonstração dentro do Docker

**Executar antes do primeiro login:**

```bash
docker compose run --rm --no-deps -it web python -m scripts.create_demo_users
```

O script solicita interativamente uma palavra-passe para cada conta. Escolha uma palavra-passe simples **com pelo menos oito caracteres**, apenas para o laboratório. O terminal não apresenta os caracteres enquanto escreve; prima Enter após cada palavra-passe. Pode usar a mesma palavra-passe nas três contas de teste, se preferir, mas não utilize palavras-passe reais.

| Perfil | Email de login |
|---|---|
| Ana Martins — colaboradora | `ana@nexaserv.test` |
| Miguel Costa — técnico | `miguel@nexaserv.test` |
| Sofia Almeida — responsável TI | `sofia@nexaserv.test` |

As palavras-passe de login são guardadas como hashes na base de dados SQLite do volume Docker, **não** no `.env`, no `Dockerfile` ou no GitHub. Se as contas já existirem, o script não as recria.

### 5. Iniciar a aplicação

```bash
docker compose up -d
```

Abrir **http://localhost:8080/login**. A porta está publicada apenas em `127.0.0.1:8080`, pelo que o acesso se destina ao próprio computador.

### 6. Consultar logs

```bash
docker compose logs -f web
```

Prima Ctrl+C para sair da visualização dos logs sem parar a aplicação.

### 7. Executar os testes dentro do Docker

```bash
docker compose run --rm --no-deps web python -m scripts.run_validation
```

O comando executa separadamente testes unitários, integração HTTP e cenários Gherkin com `pytest-bdd`, gerando `reports/index.html` e ficheiros JUnit XML/HTML por conjunto. **A existência dos testes não significa que tenham sido executados ou aprovados.** T-11 (desempenho) e T-12 (Chrome/Edge) permanecem explicitamente ignorados até à validação real. Consulte `docs/qualidade/03_plano_validacao.md` para condições iniciais, ações e resultados esperados.

### 8. Parar

```bash
docker compose down
```

Este comando remove os contentores e a rede, mas **preserva o volume** `smartdesk_data` com os utilizadores e tickets. Não use `docker compose down -v` se quiser manter os dados.

## Ficheiros e responsabilidades

| Caminho | Função |
|---|---|
| `Dockerfile` | Imagem Python 3.12-slim, dependências e arranque Uvicorn |
| `compose.yaml` | Serviço `web`, porta local 8080 e volume SQLite |
| `.dockerignore` | Exclui ficheiros locais e segredos do contexto de build |
| `.env.example` | Chave de sessão fictícia, pronta a copiar |
| `requirements.txt` | Dependências Python, incluindo Jinja2 |
| `src/main.py` | Interface HTTP e rotas FastAPI |
| `src/services.py` | Regras de negócio e permissões |
| `src/auth.py` | Autenticação e hashes de palavras-passe |
| `src/database.py` | Ligação e esquema SQLite; usa `SMARTDESK_DB` |
| `src/templates/`, `src/static/` | Interface HTML e CSS |
| `scripts/create_demo_users.py` | Criação interativa de contas fictícias |
| `tests/` | Testes unitários, integração e BDD |\n| `scripts/run_validation.py` | Executa os conjuntos e gera relatórios JUnit/HTML |\n| `scripts/generate_report.py` | Consolida os resultados sem considerar não executados como aprovados |\n| `reports/` | Resultados locais, excluídos do Git |
| `docs/`, `features/` | Requisitos, critérios e cenários aprovados |

## Limites da demonstração

Um único serviço web, sem novos endpoints ou funcionalidades de negócio. A base SQLite é persistida num volume Docker. Não foi acrescentado `/health` porque ainda não foi aprovado. A aplicação **não está preparada para exposição pública**: faltam proteção CSRF e configuração HTTPS/cookies seguros. A chave de sessão de exemplo é deliberadamente fictícia e exclusiva deste laboratório.

**Validação:** estes comandos são o procedimento previsto; a publicação do código, por si só, não comprova que Docker ou os testes tenham sido executados.
