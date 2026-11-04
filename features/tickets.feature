# language: pt

Funcionalidade: Gestão de tickets SmartDesk
  Como utilizador da NexaServ
  Quero gerir pedidos de suporte
  Para acompanhar a resolução de problemas informáticos

  Cenário: US-001 - Autenticação com email e palavra-passe
    Dado que Ana possui uma conta válida
    Quando introduz o email e a palavra-passe corretos
    Então consegue iniciar sessão no SmartDesk
    E é identificada com o perfil de colaboradora

  Cenário: US-001 - Recusar credenciais inválidas
    Dado que Ana possui uma conta válida
    Quando introduz uma palavra-passe incorreta
    Então o acesso é recusado
    E é apresentada uma mensagem de erro

  Cenário: US-002 - Criar ticket de equipamento
    Dado que Ana iniciou sessão
    Quando cria um ticket com o título "Impressora não funciona"
    E introduz a descrição do problema
    E seleciona a categoria "Equipamento"
    Então o ticket é registado
    E fica no estado "Aberto"

  Cenário: US-003 - Consultar os próprios tickets
    Dado que Ana iniciou sessão
    E existem tickets criados por Ana
    E existem tickets de outros colaboradores
    Quando consulta a lista de tickets
    Então visualiza apenas os seus tickets
    E consegue consultar os respetivos estados

  Cenário: US-004 - Atribuir ticket a um técnico
    Dado que Sofia iniciou sessão como responsável de TI
    E existe um ticket no estado "Aberto"
    Quando atribui o ticket a Miguel
    Então Miguel fica identificado como técnico responsável

  Cenário: US-004 - Reatribuir ticket em tratamento
    Dado que Sofia iniciou sessão como responsável de TI
    E existe um ticket atribuído a Miguel
    E o ticket está no estado "Em tratamento"
    Quando Sofia o reatribui a outro técnico
    Então o novo técnico fica identificado como responsável
    E o estado permanece "Em tratamento"

  Cenário: US-005 - Consultar tickets atribuídos
    Dado que Miguel iniciou sessão como técnico
    E existem tickets atribuídos a Miguel
    Quando consulta a lista de tickets
    Então visualiza os tickets que lhe estão atribuídos

  Cenário: US-006 - Iniciar tratamento
    Dado que Miguel possui um ticket atribuído
    E o ticket está no estado "Aberto"
    Quando Miguel inicia o tratamento
    Então o estado passa a "Em tratamento"

  Cenário: US-007 - Registar resolução
    Dado que Miguel está a tratar um ticket
    E o ticket está no estado "Em tratamento"
    Quando regista a solução aplicada
    E assinala o ticket como resolvido
    Então o estado passa a "Resolvido"
    E a solução fica registada

  Cenário: US-008 - Comunicar problema persistente
    Dado que Ana possui um ticket no estado "Resolvido"
    E o ticket está atribuído a Miguel
    Quando Ana comunica que o problema persiste
    Então o ticket regressa ao estado "Em tratamento"
    E mantém Miguel como técnico responsável
    E fica disponível para nova intervenção

  Cenário: US-009 - Acompanhar e fechar ticket
    Dado que Sofia iniciou sessão como responsável de TI
    E existe um ticket no estado "Resolvido"
    Quando consulta o ticket e a solução registada
    E confirma a resolução
    E fecha o ticket
    Então o estado passa a "Fechado"

  Cenário: US-009 - Impedir fecho por técnico
    Dado que Miguel iniciou sessão como técnico
    E existe um ticket no estado "Resolvido"
    Quando Miguel tenta fechar o ticket
    Então a operação é recusada
    E o estado permanece "Resolvido"

  Cenário: US-009 - Impedir reabertura
    Dado que existe um ticket no estado "Fechado"
    Quando um utilizador tenta reabrir o ticket
    Então a operação é recusada
    E o estado permanece "Fechado"

  Cenário: US-010 - Validar campos obrigatórios
    Dado que Ana iniciou sessão
    Quando tenta criar um ticket sem título
    Então o ticket não é criado
    E é apresentada uma mensagem clara
    E o campo obrigatório é identificado

  Cenário: US-011 - Verificar desempenho da consulta
    Dado que Miguel iniciou sessão como técnico
    E existem tickets atribuídos a Miguel
    Quando consulta a lista de tickets
    Então a página responde em até 3 segundos
    E apresenta os tickets atribuídos

  Esquema do Cenário: US-012 - Compatibilidade dos navegadores
    Dado que Ana utiliza o navegador "<navegador>"
    E possui uma conta válida
    Quando inicia sessão no SmartDesk
    E cria um ticket com os campos obrigatórios
    Então consegue registar o ticket
    E visualiza o ticket no estado "Aberto"

    Exemplos:
      | navegador |
      | Chrome    |
      | Edge      |
