# Athena Life Balance RL

Projeto acadêmico de Aprendizado por Reforço usando Q-learning.

O agente aprende a equilibrar uma rotina simulada de múltiplas responsabilidades, considerando energia, saúde, estresse e pendências.

## Objetivo

Demonstrar como um agente pode aprender, por tentativa e erro, estratégias de equilíbrio entre produtividade e bem-estar.

## Agente

Athena, uma agente autônoma de decisão.

## Ambiente

Uma semana simulada com 7 dias e 3 períodos por dia: manhã, tarde e noite.

## Estado

- energia
- saúde
- estresse
- pendências
- período do dia

## Ações

- trabalhar
- estudar
- descansar
- exercitar
- cuidar da família
- tarefa doméstica

## Recompensas

O agente recebe recompensa quando mantém equilíbrio entre produtividade, saúde e energia.

Recebe penalidade quando aumenta estresse, reduz saúde, acumula pendências ou entra em burnout.

## Burnout

Se a energia chega a zero, o episódio termina imediatamente.

## Algoritmo

Q-learning.
