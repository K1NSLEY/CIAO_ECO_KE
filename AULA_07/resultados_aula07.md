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

## Considerações

O algoritmo ACO combinou busca global e refinamento local. A etapa de construção das rotas explorou o espaço de busca por meio da probabilidade baseada em feromônio e heurística, enquanto a busca local 2-opt intensificou a solução encontrada, melhorando o custo final da rota.

Esse tipo de estratégia é interessante porque permite que o algoritmo explore várias alternativas sem perder a possibilidade de corrigir e otimizar a melhor solução identificada.

Se a taxa de evaporação do feromônio fosse definida como rho = 0.0, o algoritmo perderia o mecanismo de esquecimento e o feromônio acumulado em caminhos antigos poderia dominar a busca. Isso faria a convergência ocorrer mais rapidamente, mas com maior risco de ficar preso em soluções subótimas.

# Laboratório 2 — Algoritmo Genético

## Resultado da execução

```text
=== LAB 02: Algoritmo Genetico ===
[LAB 02] Melhor Solucao: [0 1 1 1 1]
[LAB 02] Fitness: 15
[LAB 02] Peso: 8/15
```

## Considerações

O problema da mochila exige que a solução respeite a restrição de peso. A penalização do fitness foi fundamental para garantir que indivíduos inviáveis não fossem favorecidos durante a evolução. Isso força a população a convergir para respostas válidas dentro da capacidade máxima da mochila.

A mutação também desempenha papel importante porque introduz diversidade genética e ajuda a evitar que a busca fique presa em ótimos locais. No entanto, se a taxa de mutação for elevada demais, o algoritmo pode perder a estrutura evolutiva e se tornar semelhante a uma busca aleatória.

# Laboratório 3 — PSO: Inércia, Componente Cognitiva e Social

## Resultado da execução

```text
=== LAB 03: PSO ===
[LAB 03] Melhor posicao encontrada pelo Enxame (gbest): [8.29997020e-05 3.35700877e-03]
[LAB 03] Fitness do gbest: 0.000011
```

## Considerações

O PSO mostrou como a interação entre as partículas pode produzir convergência para uma boa solução. A inércia controla a influência da velocidade anterior, enquanto a componente cognitiva e a social equilibram a busca individual e coletiva.

Quando a componente cognitiva é zerada, as partículas passam a seguir principalmente o melhor global do enxame. Isso reduz a autonomia individual e aumenta o risco de convergência prematura para um mínimo local. A inércia, por sua vez, define o quanto o algoritmo continua explorando ou se concentra em refinamento local.

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

## Considerações

A evaporação do feromônio é essencial para evitar que caminhos antigos continuem dominando a busca. Sem esse mecanismo, o sistema tenderia a reforçar soluções ultrapassadas e a perder capacidade de adaptação.

A atratividade inicial dos enlaces está relacionada inversamente à latência do arco, ou seja, enlaces com menor custo tendem a receber maior valor de atratividade. Isso faz com que as formigas prefiram rotas mais curtas e eficientes, garantindo uma convergência mais consistente para soluções melhores.

# Laboratório 5 — Algoritmo Memético

## Resultado da execução

```text
=== LAB 05: Memetico ===
[LAB 05] Solucao Inicial: [ 2.5 -3.1] | Fitness: 37.7698
[LAB 05] Solucao Refinada: [ 2.53717717 -3.04875403] | Fitness: 35.9261
```

## Considerações

A busca local aplicada ao algoritmo memético foi importante para melhorar a solução inicial e intensificar a busca em torno da melhor área encontrada. Esse tipo de estratégia combina a exploração global da evolução com um refinamento local mais agressivo.

A principal vantagem do método é melhorar a qualidade da solução em comparação com um algoritmo evolutivo puro. Porém, esse ganho vem com custo computacional maior, porque a busca local precisa avaliar várias vizinhanças para cada indivíduo da população.

# Conclusão da AULA 07

Os quatro laboratórios permitiram observar diferentes formas de resolver problemas de otimização usando meta-heurísticas. No Laboratório 1, o ACO mostrou equilíbrio entre exploração e refinamento. No Laboratório 2, o Algoritmo Genético confirmou a importância da diversidade e da penalização de soluções inviáveis. No Laboratório 3, o PSO mostrou como a memória individual e o conhecimento coletivo influenciam a busca. No Laboratório 4, a evaporação do feromônio demonstrou ser essencial para manter a busca adaptativa. No Laboratório 5, o enfoque memético mostrou que a combinação entre evolução e busca local pode acelerar a convergência para boas soluções.

Em geral, a aula confirmou que diferentes meta-heurísticas são úteis em cenários distintos e que o sucesso da otimização depende diretamente do equilíbrio entre exploração, intensificação e controle de restrições.
