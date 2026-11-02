# Passo 1 — Problema de negócio e objetivos do SmartDesk

## 1. Problema de negócio

A NexaServ é uma empresa de consultoria e serviços tecnológicos com 60 colaboradores, distribuídos entre a sede e o trabalho remoto.

Atualmente, os pedidos de suporte informático são comunicados por email, telefone ou mensagens. A equipa de TI, constituída por três técnicos e uma responsável, utiliza uma caixa de correio partilhada e uma folha de cálculo para gerir os pedidos.

Este processo apresenta três problemas principais:

- Alguns pedidos perdem-se ou não ficam devidamente registados.
- Nem sempre é claro quem é responsável por cada pedido.
- É difícil acompanhar o estado e a resolução dos problemas.

## 2. Objetivos do projeto

O SmartDesk pretende centralizar e organizar os pedidos de suporte informático numa única aplicação web interna.

Os principais objetivos são:

1. Garantir que todos os pedidos ficam registados.
2. Permitir a atribuição de tickets aos técnicos.
3. Acompanhar cada pedido desde a abertura até ao fecho.
4. Facilitar a comunicação entre colaboradores e equipa de TI.
5. Melhorar a organização e a supervisão do trabalho de suporte.

## 3. Melhorias esperadas

| Situação atual | Melhoria pretendida |
|---|---|
| Pedidos dispersos por vários canais | Pedidos centralizados no SmartDesk |
| Risco de perda de pedidos | Registo organizado dos tickets |
| Responsabilidades pouco claras | Técnico responsável identificado |
| Dificuldade em acompanhar pedidos | Estados visíveis e atualizados |
| Supervisão através de folha de cálculo | Acompanhamento centralizado pela responsável de TI |

## 4. Limites da primeira versão (MVP)

A primeira versão incluirá a gestão de tickets nas categorias Equipamento, Software e Acessos.

O percurso será: **Aberto → Em tratamento → Resolvido → Fechado**, permitindo criar, atribuir, tratar, resolver e fechar tickets.

Existirão três perfis: colaborador, técnico de suporte e responsável de TI.

Ficam excluídos do MVP a aplicação móvel, notificações SMS, resolução automática com inteligência artificial, integração com email e gestão complexa de SLA (prazos de serviço).

## 5. Decisões ainda necessárias

- Os colaboradores podem consultar apenas os seus próprios tickets?
- Quem pode fechar um ticket: o colaborador, o técnico ou ambos?
- Como serão definidos os critérios de prioridade dos pedidos?
- Que informação será obrigatória na criação de um ticket?
