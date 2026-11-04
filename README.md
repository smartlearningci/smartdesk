# SmartDesk — Gestão de Pedidos de Suporte Informático

**Projeto pedagógico | NexaServ | Especificação inicial concluída**

## 1. O projeto

O **SmartDesk** é uma aplicação web de gestão de pedidos de suporte informático, desenvolvida progressivamente numa formação prática em desenvolvimento de software, testes, Docker e automação.

A empresa fictícia **NexaServ** tem 60 colaboradores e uma equipa de TI com três técnicos e uma responsável. Os pedidos são atualmente recebidos por email, telefone e mensagens e acompanhados numa caixa de correio partilhada e numa folha de cálculo. O SmartDesk pretende centralizar o processo.

## 2. Objetivos

- Registar pedidos de suporte informático.
- Identificar o técnico responsável por cada pedido.
- Acompanhar pedidos desde a abertura até ao fecho.
- Facilitar a comunicação entre colaboradores e TI.
- Melhorar a organização e supervisão do suporte.

## 3. Utilizadores

| Persona | Perfil | Responsabilidade |
|---|---|---|
| Ana Martins | Colaboradora | Cria e acompanha os seus tickets. |
| Miguel Costa | Técnico | Consulta, trata e resolve tickets atribuídos. |
| Sofia Almeida | Responsável de TI | Atribui, reatribui, supervisiona e fecha tickets. |

## 4. Funcionamento

Categorias: **Equipamento, Software e Acessos**.

Percurso principal: **Aberto → Em tratamento → Resolvido → Fechado**.

Exemplo: Ana cria um ticket porque a impressora não funciona; Sofia atribui-o a Miguel; Miguel trata o problema e regista a solução; Sofia verifica a resolução e fecha o ticket.

Se Ana comunicar que o problema persiste, o ticket regressa de **Resolvido** a **Em tratamento**. Sofia pode reatribuir durante o tratamento. Apenas Sofia pode fechar tickets após verificar a resolução, **sem exigir confirmação formal de Ana**. Tickets Fechados não podem ser reabertos.

## 5. MVP

Inclui autenticação por email e palavra-passe; criação e consulta de tickets; atribuição e reatribuição; tratamento, resolução e fecho; supervisão; permissões; validações dos campos obrigatórios **título, descrição e categoria**.

A aplicação deverá funcionar no **Chrome** e no **Edge**. A meta provisória é de **até três segundos** de resposta para as páginas principais, em condições de teste documentadas.

As prioridades **P0/P1** são prioridades de desenvolvimento do backlog, **não** prioridades dos tickets.

**Fora do MVP:** aplicação móvel, SMS, integração automática com email, resolução automática por IA e gestão avançada de SLA.

## 6. Estrutura do repositório

```text
smartdesk/
├── README.md
├── docs/
│   ├── negocio/
│   │   ├── 01_problema_e_objetivos.md
│   │   └── 02_stakeholders_e_personas.md
│   ├── produto/
│   │   ├── 01_jornada_e_processo.md
│   │   ├── 02_requisitos_e_user_stories.md
│   │   └── 03_mvp_backlog_e_aceitacao.md
│   ├── arquitetura/
│   │   └── 01_arquitetura_inicial.md
│   └── qualidade/
│       └── 01_testes_e_rastreabilidade.md
└── features/
    └── tickets.feature
```

## 7. Documentação aprovada

| Etapa | Documento |
|---|---|
| 1 — Problema e objetivos | [Consultar](docs/negocio/01_problema_e_objetivos.md) |
| 2 — Personas | [Consultar](docs/negocio/02_stakeholders_e_personas.md) |
| 3 — Jornada e processo | [Consultar](docs/produto/01_jornada_e_processo.md) |
| 4 — Requisitos e User Stories | [Consultar](docs/produto/02_requisitos_e_user_stories.md) |
| 5 — MVP e backlog | [Consultar](docs/produto/03_mvp_backlog_e_aceitacao.md) |
| 6 — Arquitetura inicial | [Consultar](docs/arquitetura/01_arquitetura_inicial.md) |
| 6 — Testes e rastreabilidade | [Consultar](docs/qualidade/01_testes_e_rastreabilidade.md) |
| Critérios de aceitação | [Cenários Gherkin](features/tickets.feature) |

## 8. Arquitetura inicial

- **Frontend:** interface web, formulários, listas e ações.
- **Backend:** autenticação, permissões, validações e regras de negócio.
- **Base de dados:** utilizadores, tickets, atribuições e resoluções.

Tecnologias propostas: **HTML/CSS e templates**, **Python/FastAPI** e **SQLite**, privilegiando a simplicidade.

## 9. Qualidade e testes

| Elemento | Total |
|---|---:|
| Requisitos funcionais | 9 |
| Requisitos não funcionais | 4 |
| User Stories | 12 |
| Cenários principais Gherkin | 12 |
| Testes previstos | 20 |

Os testes verificam os percursos funcionais, permissões, transições de estado, validação de dados, compatibilidade e desempenho. A matriz de rastreabilidade relaciona requisitos, User Stories e testes.

**Os testes ainda não foram implementados nem executados.**

## 10. Próximas etapas da formação

| Etapa | Objetivo |
|---|---|
| Desenvolvimento do MVP | Transformar os requisitos numa aplicação funcional. |
| Testes e validação | Executar testes, corrigir falhas e produzir relatório global. |
| Docker | Criar imagem, executar contentores e usar Docker Compose. |
| Persistência e redes | Explorar volumes, comunicação entre serviços e evolução da base de dados. |
| CI/CD | Introduzir automatização de testes, construção e entrega. |
| Cloud e observabilidade | Explorar evolução e acompanhamento da aplicação. |

Cada conceito será explicado antes de ser aplicado.

## 11. Estado do projeto

**Especificação inicial concluída. Implementação ainda não iniciada.**

Os documentos descrevem problema, utilizadores, jornada, requisitos, MVP, arquitetura e testes. O desenvolvimento deverá preservar as decisões e a rastreabilidade entre requisitos, código e testes. As condições de medição do desempenho serão concretizadas antes da execução dos testes.

**Do problema de negócio à aplicação em funcionamento.**
