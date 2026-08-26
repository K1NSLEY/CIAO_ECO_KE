# AULA 04 - AC-1 Parte Final

## Exercício 1 - Elitismo

Foi executado o mesmo cenário duas vezes, com a mesma matriz de distâncias e
com sementes idênticas: uma execução preservando o melhor indivíduo e outra
sem elitismo. O melhor custo com elitismo foi **250,37**, enquanto a execução
sem elitismo obteve **272,22**. Nesse experimento, o elitismo preservou a melhor
solução e produziu uma convergência mais estável.

## Exercício 2 - Penalidades de SLA

Com `np.random.seed(15)` e a rota `[0, 1, 2, 3, 4, 5]`, o custo final foi
**1160,00 ms**. O cálculo soma a latência de cada enlace e adiciona 1000 ms
para cada enlace que excede o limite operacional de 50 ms.

## Desafio 3 - Alocação de servidores

As 20 tarefas totalizam 541 segundos. Como há quatro servidores, o limite
inferior para o makespan é `ceil(541 / 4) = 136` segundos. O algoritmo
genético encontrou a distribuição de cargas abaixo, atingindo esse limite e,
portanto, uma solução ótima para essa instância.

| Servidor | Carga | Tarefas |
|---:|---:|---|
| 0 | 135 s | 9, 13, 15 |
| 1 | 135 s | 3, 4, 8, 17 |
| 2 | 136 s | 2, 5, 6, 10, 16 |
| 3 | 135 s | 1, 7, 11, 12, 14, 18, 19, 20 |

**Makespan: 136 s.**

## Desafio de Fechamento - Motor SD-WAN Zero-Trust

O motor selecionou a rota **0 -> 3 -> 7 -> 11**. A rota possui latência total
de **56,00 ms**, perda de pacotes total de **1,20%**, penalidade de segurança
igual a **0** e fitness final de **86,00**.

Os roteadores 2, 5 e 8 têm reputação abaixo de 50 e recebem penalidade de
segurança de 5000 quando pertencem a uma rota. A rota escolhida desvia desses
nós não confiáveis, mantendo a decisão alinhada ao requisito Zero-Trust.
