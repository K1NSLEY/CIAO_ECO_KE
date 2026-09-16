# Alunos: KINSLEY CHINDA AMADI (97399) e EDUARDO LIMA (RA: 105764)

# AULA 07 — Resultados e Considerações

Disciplina: CIAO_ECO_2026  
Atividade: AC2 — Parte 2: Laboratório Prático de Meta-Heurísticas

# Laboratório 1 — ACO com Busca Local

## Resultado da execução

```text
=== LAB 01: ACO com Busca Local ===
[LAB 01 - SUCESSO] Melhor Caminho: [0, 1, 3, 4, 2, 0] | Custo: 70
```

## Questões Técnicas LAB 01

**1. Como o uso da busca local 2-opt afeta o equilíbrio entre Exploration e Exploitation na busca de caminhos?**

O ACO realiza a etapa de *Exploration* ao construir diferentes rotas usando o feromônio e a heurística. Em seguida, a busca local 2-opt realiza a *Exploitation*, testando inversões de trechos da rota para encontrar uma solução de menor custo. Assim, o 2-opt intensifica a busca nas regiões promissoras sem eliminar completamente a exploração global feita pelas formigas. O custo dessa melhoria é um aumento no tempo de processamento, pois várias vizinhanças precisam ser avaliadas.

**2. O que aconteceria com a convergência do algoritmo se a taxa de evaporação (`rho`) fosse definida em 0.0, sem evaporação?**

Com `rho = 0.0`, a atualização `pheromone *= (1 - rho)` não reduziria os valores existentes. O feromônio acumulado em caminhos antigos poderia dominar as decisões das formigas, fazendo o algoritmo convergir mais rapidamente para uma rota, mas aumentando o risco de essa rota ser subótima. Sem evaporação, o ACO perderia parte de sua capacidade de esquecer escolhas ruins e explorar alternativas.

# Laboratório 2 — Algoritmo Genético

## Resultado da execução

```text
=== LAB 02: Algoritmo Genetico ===
[LAB 02] Melhor Solucao: [0 1 1 1 1]
[LAB 02] Fitness: 15
[LAB 02] Peso: 8/15
```

## Questões Técnicas LAB 02

**1. Explique qual é o papel do operador de mutação em um Algoritmo Genético e o que ocorre se a taxa de mutação for configurada em 100%.**

A mutação introduz diversidade genética na população ao inverter aleatoriamente alguns bits dos indivíduos. Ela ajuda o algoritmo a explorar novas soluções e a escapar de ótimos locais. Com uma taxa de mutação de 100%, todos os genes seriam invertidos em todas as gerações. A busca perderia grande parte da estabilidade herdada dos pais e poderia se aproximar de uma busca aleatória, dificultando a convergência.

**2. Por que a penalização do fitness, atribuindo 0 para indivíduos que ultrapassam a capacidade, é fundamental para a convergência das restrições?**

A penalização impede que soluções inviáveis sejam favorecidas apenas por apresentarem alto valor total. Ao atribuir fitness 0 aos indivíduos cujo peso ultrapassa 15, o algoritmo direciona a seleção para soluções que respeitam a capacidade da mochila. Dessa forma, a população converge para respostas válidas, e não apenas para respostas com maior valor ignorando a restrição.

# Laboratório 3 — PSO: Inércia, Componente Cognitiva e Social

## Resultado da execução

```text
=== LAB 03: PSO ===
[LAB 03] Melhor posicao encontrada pelo Enxame (gbest): [8.29997020e-05 3.35700877e-03]
[LAB 03] Fitness do gbest: 0.000011
```

## Questões Técnicas LAB 03

**1. O que acontece com o comportamento das partículas se zerarmos a componente cognitiva (`c1 = 0`)?**

As partículas deixam de considerar a própria melhor posição histórica (`pbest`) e passam a ser influenciadas principalmente pela inércia e pelo melhor resultado coletivo (`gbest`). Isso reduz a autonomia individual, concentra o enxame em torno da melhor posição global conhecida e aumenta o risco de convergência prematura para um mínimo local.

**2. Qual a função do parâmetro de inércia (`w`) na busca por mínimos globais?**

O parâmetro `w` controla quanto da velocidade anterior é mantido. Valores maiores favorecem velocidades mais persistentes e maior exploração do espaço de busca; valores menores reduzem o movimento e favorecem a intensificação perto das melhores posições. Portanto, a inércia ajuda a equilibrar exploração global e refinamento local.

# Laboratório 4 — ACO: Feromônio, Evaporação e Atratividade

## Resultado da execução

```text
=== LAB 04: ACO - Feromonio ===
[LAB 04] Matriz de Feromonio Atualizada:
 [[0.75       0.91666667 0.91666667 0.75      ]
  [0.75       0.75       0.75       1.08333333]
  [0.75       0.91666667 0.75       0.75      ]
  [0.75       0.75       0.75       0.75      ]]
```

## Questões Técnicas LAB 04

**1. Por que a evaporação do feromônio é necessária no algoritmo ACO?**

A evaporação reduz gradualmente o feromônio acumulado em arestas antigas. Isso evita que uma escolha feita no início domine todas as iterações seguintes e mantém a capacidade de explorar novas rotas. Portanto, ela ajuda a equilibrar intensificação e adaptação durante a busca.

**2. O que ocorreria em grafos complexos sem evaporação?**

Sem evaporação, os depósitos de feromônio seriam acumulados indefinidamente. Uma rota inicialmente escolhida poderia receber cada vez mais feromônio, mesmo que não fosse a melhor, levando à convergência prematura e à perda de diversidade na exploração do grafo.

**3. Qual a relação matemática entre a latência de um enlace e sua atratividade inicial (`eta`) para as formigas?**

A atratividade é inversamente proporcional à latência do enlace. No código, essa relação é representada por `eta = 1 / latencia` (ou por `(1 / latencia) ** beta` quando a influência heurística é aplicada). Assim, quanto menor a latência, maior a atratividade e a probabilidade de o enlace ser escolhido.

# Laboratório 5 — Algoritmo Memético

## Resultado da execução

```text
=== LAB 05: Memetico ===
[LAB 05] Solucao Inicial: [ 2.5 -3.1] | Fitness: 37.7698
[LAB 05] Solucao Refinada: [ 2.53717717 -3.04875403] | Fitness: 35.9261
```

## Questões Técnicas LAB 05

**1. Qual a diferença fundamental de conceito entre um Algoritmo Genético Puro e um Algoritmo Memético?**

O Algoritmo Genético Puro depende principalmente de seleção, crossover e mutação para explorar o espaço de soluções. O Algoritmo Memético acrescenta uma busca local, que refina individualmente as soluções encontradas. Assim, o método memético combina exploração global da evolução com intensificação local.

**2. Em termos de custo computacional, qual o impacto de executar a busca local sobre todos os indivíduos de uma população a cada geração?**

O custo computacional aumenta, porque cada indivíduo exige a avaliação de vários vizinhos a cada geração. Embora isso possa melhorar a qualidade e acelerar a convergência das soluções, o tempo total de execução cresce proporcionalmente ao tamanho da população, ao número de gerações e ao número de passos da busca local.

# Conclusão da AULA 07

Os cinco laboratórios permitiram observar diferentes formas de resolver problemas de otimização usando meta-heurísticas. No Laboratório 1, o ACO mostrou equilíbrio entre exploração e refinamento. No Laboratório 2, o Algoritmo Genético confirmou a importância da diversidade e da penalização de soluções inviáveis. No Laboratório 3, o PSO mostrou como a memória individual e o conhecimento coletivo influenciam a busca. No Laboratório 4, a evaporação do feromônio demonstrou ser essencial para manter a busca adaptativa. No Laboratório 5, o enfoque memético mostrou que a combinação entre evolução e busca local pode acelerar a convergência para boas soluções.

Em geral, a aula confirmou que diferentes meta-heurísticas são úteis em cenários distintos e que o sucesso da otimização depende diretamente do equilíbrio entre exploração, intensificação e controle de restrições.
