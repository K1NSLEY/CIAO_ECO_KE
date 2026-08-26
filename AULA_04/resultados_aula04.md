# AULA 04 - AC-1 Parte Final

## Exercício 1 - Elitismo

Rodamos o mesmo cenário duas vezes para a comparação não ficar injusta: mesma
matriz e mesma semente, mudando apenas o elitismo. Com elitismo, o menor custo
foi **250,37**; sem ele, ficou em **272,22**. Na prática, guardar o melhor
indivíduo evitou que uma solução boa se perdesse nas gerações seguintes.

## Exercício 2 - Penalidades de SLA

Para a rota `[0, 1, 2, 3, 4, 5]`, usando a semente 15, o resultado foi
**1160,00 ms**. O valor parece alto porque não é só a soma das latências:
cada enlace acima de 50 ms recebeu mais 1000 ms. Foi uma forma simples de
deixar claro que uma rota rápida no total ainda pode ser ruim se quebrar o SLA.

## Desafio 3 - Alocação de servidores

As 20 tarefas somam 541 segundos. Dividindo esse total entre quatro
servidores, ninguém conseguiria terminar antes de `ceil(541 / 4) = 136`
segundos. A distribuição encontrada chegou exatamente nesse valor, então não
há como melhorar o makespan dessa instância.

| Servidor | Carga | Tarefas |
|---:|---:|---|
| 0 | 135 s | 9, 13, 15 |
| 1 | 135 s | 3, 4, 8, 17 |
| 2 | 136 s | 2, 5, 6, 10, 16 |
| 3 | 135 s | 1, 7, 11, 12, 14, 18, 19, 20 |

**Makespan: 136 s.**

## Desafio de Fechamento - Motor SD-WAN Zero-Trust

O motor escolheu **0 -> 3 -> 7 -> 11**: 56,00 ms de latência, 1,20% de perda,
nenhuma penalidade de segurança e fitness **86,00**.

O ponto mais importante aqui não foi só chegar ao destino. Os roteadores 2, 5
e 8 têm reputação abaixo de 50; usar qualquer um deles acrescentaria 5000 ao
fitness. A rota escolhida contorna esses pontos, o que combina com a regra de
Zero-Trust proposta no desafio.
