# Passo 3 — Jornada do utilizador e processo de tickets

**Objetivo:** Descrever o percurso de um pedido de suporte informático, desde a comunicação do problema até ao fecho do ticket.

## 1. Sequência narrativa — Problema de impressora

| Etapa | Responsável | Ação | Estado do ticket |
|---|---|---|---|
| 1 | **Ana Martins** | A impressora não funciona. Ana acede ao SmartDesk e cria um ticket na categoria Equipamento, descrevendo o problema. | Aberto |
| 2 | **Sofia Almeida** | Consulta os pedidos pendentes e atribui o ticket a Miguel, tendo em conta a distribuição do trabalho. | Aberto |
| 3 | **Miguel Costa** | Consulta o ticket atribuído e inicia a análise do problema. | Em tratamento |
| 4 | **Miguel Costa** | Verifica a impressora, identifica a causa e realiza a intervenção necessária. | Em tratamento |
| 5 | **Miguel Costa** | Regista a solução aplicada e assinala o ticket como resolvido. | Resolvido |
| 6 | **Ana Martins** | Consulta o SmartDesk e verifica se a impressora já funciona. | Resolvido |
| 7 | **Sofia Almeida** | Acompanha o resultado e, estando a resolução confirmada, fecha o ticket. | Fechado |

## 2. Principais decisões do processo

- **Quem trata o pedido?** Sofia atribui o ticket a um técnico e pode reatribuí-lo se necessário.
- **O problema foi resolvido?** Se não, Miguel continua o tratamento.
- **A resolução funcionou?** Se Ana indicar que o problema persiste, o ticket regressa de Resolvido a Em tratamento.
- **O ticket pode ser fechado?** Sofia confirma a resolução antes de o fechar.
- **Um ticket fechado pode ser reaberto?** Não. Um novo problema exige um novo ticket.

## 3. Fluxograma ASCII — Jornada do ticket

```text
┌───────────────────────────────────┐
│ ANA — Cria ticket: Impressora     │
│ Estado: ABERTO                    │
└─────────────────┬─────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│ SOFIA — Atribui a Miguel          │◄──────────┐
│ (pode reatribuir a outro técnico) │           │
└─────────────────┬─────────────────┘           │
                  │                             │
                  ▼                             │
┌───────────────────────────────────┐           │
│ MIGUEL — Analisa e intervém       │           │
│ Estado: EM TRATAMENTO             │◄──────┐   │
└─────────────────┬─────────────────┘       │   │
                  │                         │   │
                  ▼                         │   │
          ┌─────────────────┐               │   │
          │ Problema        │               │   │
          │ resolvido?      │               │   │
          └─────┬─────┬─────┘               │   │
               NÃO   SIM                    │   │
                │     │                     │   │
                └─────┼─────────────────────┘   │
                      │                         │
                      ▼                         │
┌───────────────────────────────────┐           │
│ MIGUEL — Regista a solução        │           │
│ Estado: RESOLVIDO                 │           │
└─────────────────┬─────────────────┘           │
                  │                             │
                  ▼                             │
          ┌─────────────────┐                   │
          │ ANA — Confirma  │                   │
          │ que funciona?   │                   │
          └─────┬─────┬─────┘                   │
               NÃO   SIM                       │
                │     │                        │
                │     ▼                        │
                │  ┌────────────────────────┐  │
                │  │ SOFIA — Fecha o ticket │  │
                │  │ Estado: FECHADO        │  │
                │  └────────────────────────┘  │
                │                              │
                └──► EM TRATAMENTO ────────────┘
                     (Sofia pode manter
                      ou reatribuir técnico)
```

**Nota:** Se Miguel ainda não resolveu o problema, o ticket permanece em Em tratamento. Se Ana indicar que a resolução não funcionou, o ticket regressa de Resolvido a Em tratamento. Sofia pode reatribuir o ticket durante o tratamento.

## 4. Resultado esperado

No final, o SmartDesk permite saber quem comunicou o problema, quem ficou responsável pelo tratamento, qual a solução aplicada e em que estado se encontra o pedido.
