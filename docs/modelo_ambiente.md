# Athena Life Balance: Modelo do Ambiente

## Objetivo

O projeto Athena Life Balance tem como objetivo investigar como um agente treinado por Aprendizado por Reforço pode aprender estratégias de equilíbrio entre produtividade, saúde, energia e responsabilidades múltiplas em um ambiente inspirado nos desafios da dupla e múltipla jornada frequentemente enfrentada por mulheres.

---

## Agente

Athena é uma agente autônoma que toma decisões ao longo de uma semana simulada.

Seu objetivo é maximizar o equilíbrio geral da rotina e minimizar a ocorrência de burnout.

---

## Ambiente

Cada episódio representa uma semana.

A semana possui:

* 7 dias
* 3 períodos por dia

  * manhã
  * tarde
  * noite

Totalizando 21 decisões por episódio.

---

## Variáveis de Estado

### Energia

Representa a disposição física e mental da agente.

Faixa:

0 a 100

---

### Saúde

Representa o bem-estar geral da agente.

Faixa:

0 a 100

---

### Estresse

Representa a pressão acumulada pelas responsabilidades.

Faixa:

0 a 100

---

### Pendências

Representa tarefas profissionais, acadêmicas ou pessoais que ainda precisam ser realizadas.

Faixa:

0 a 100

---

### Carga Invisível

Representa o acúmulo mental associado ao gerenciamento simultâneo de múltiplas responsabilidades.

Faixa:

0 a 100

---

### Período

Representa o momento atual da semana.

Valores:

* manhã
* tarde
* noite

---

## Ações Disponíveis

### TRABALHAR

Executa atividades profissionais.

### ESTUDAR

Executa atividades de formação e qualificação.

### DESCANSAR

Executa atividades de recuperação física e mental.

### EXERCITAR

Executa atividades de autocuidado e saúde.

### CUIDAR_FAMILIA

Executa atividades relacionadas ao cuidado familiar.

### TAREFA_DOMESTICA

Executa atividades relacionadas à manutenção da rotina doméstica.

---

## Dinâmica do Ambiente

No início de cada dia novas demandas podem surgir.

Essas demandas aumentam o nível de pendências da agente.

O objetivo do agente não é eliminar completamente as pendências, mas encontrar um equilíbrio sustentável entre produtividade e bem-estar.

---

## Burnout

O burnout ocorre quando:

Energia <= 0

Consequências:

* encerramento imediato do episódio;
* penalidade elevada.

---

## Recompensas

O agente recebe recompensas por:

* manter energia saudável;
* manter saúde adequada;
* controlar o estresse;
* reduzir pendências;
* reduzir carga invisível;
* concluir a semana sem burnout.

O agente recebe penalidades por:

* estresse elevado;
* excesso de pendências;
* energia baixa;
* saúde baixa;
* burnout.

---

## Hipótese H1

Um agente treinado com Q-Learning será capaz de aprender estratégias de equilíbrio entre produtividade, saúde e responsabilidades múltiplas, reduzindo a incidência de burnout ao longo dos episódios.

---

## Métricas

### Principal

* Taxa de Burnout

### Secundárias

* Recompensa média por episódio
* Energia final média
* Saúde final média
* Estresse final médio
* Pendências finais médias
* Carga invisível média
* Taxa de conclusão da semana
