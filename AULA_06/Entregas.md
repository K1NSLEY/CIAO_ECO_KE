# Aula 06 - Resultados

## Laboratório 01

### Output

```text
Matriz inicial de feromônio:
[[1. 1. 1. 0. 0. 0.]
 [1. 1. 1. 1. 0. 0.]
 [1. 1. 1. 1. 1. 0.]
 [0. 1. 1. 1. 1. 1.]
 [0. 0. 1. 1. 1. 1.]
 [0. 0. 0. 1. 1. 1.]]

Vizinhos do nó 0: [1, 2]
Vizinhos do nó 2: [0, 1, 3, 4]

Rotas encontradas:
Formiga 1: [0, 2, 1, 3, 4, 5]
Formiga 2: [0, 1, 2, 4, 3, 5]
Formiga 3: [0, 1, 2, 3, 4, 5]
Formiga 4: [0, 1, 2, 3, 4, 5]
Formiga 5: [0, 1, 2, 4, 3, 5]

Rota: [0, 1, 2, 3, 4, 5]
Custo: 8.0

========== RESULTADO ==========
Melhor rota encontrada: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

---

## Laboratório 02

### Experimento 1 - Influência do ALPHA

#### ALPHA = 1.0, BETA = 2.0

```text
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

#### ALPHA = 0.1, BETA = 2.0

```text
Número de formigas: 20
Número de iterações: 50
ALPHA: 0.1
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

#### ALPHA = 5.0, BETA = 2.0

```text
Número de formigas: 20
Número de iterações: 50
ALPHA: 5.0
BETA: 2.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

### Resposta

Quando aumentamos o ALPHA, aumenta a influência do feromônio acumulado pelas formigas. Dessa forma, o algoritmo passa a dar mais importância à experiência adquirida durante as iterações.

Nos três testes realizados, a melhor rota e o melhor custo permaneceram os mesmos: `[0, 1, 2, 3, 4, 5]`, com custo `8.0`.

### Experimento 2 - Influência do BETA

Os testes com `BETA = 0.5` e `BETA = 5.0` foram realizados no Laboratório 03.

### Resultado

* `BETA = 0.5`: melhor rota `[0, 1, 2, 3, 4, 5]`, custo `8.0`.
* `BETA = 5.0`: melhor rota `[0, 1, 2, 3, 4, 5]`, custo `8.0`.

### Resposta

Com BETA baixo, o custo da conexão exerce menor influência na escolha do próximo nó. Com BETA alto, caminhos de menor custo tornam-se mais atrativos para as formigas.

---

### Experimento 3 - Evaporação

O teste realizado com `TAXA_EVAPORACAO = 0.9` apresentou:

```text
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 5.0
Taxa de evaporação: 0.9
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

### Resposta

Com uma taxa de evaporação maior, o algoritmo perde mais rapidamente o feromônio acumulado anteriormente. Isso reduz a influência das experiências antigas e permite que novas rotas tenham maior oportunidade de influenciar a busca.

---

### Experimento 4 - Número de formigas

Foram realizados testes com:

* `NUM_FORMIGAS = 5`
* `NUM_FORMIGAS = 50`

Em ambos os casos, a melhor rota encontrada foi:

```text
[0, 1, 2, 3, 4, 5]
```

com custo:

```text
8.0
```

### Resposta

Aumentar o número de formigas aumenta a quantidade de soluções exploradas a cada iteração. Isso pode melhorar a exploração do espaço de busca, porém também aumenta o custo computacional do algoritmo.

---

## Laboratório 03

### Desafio 1 - Atratividade

**BETA = 0.5**

```text
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 0.5
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

### Desafio 2 - Evaporação

**BETA = 5.0**

```text
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 5.0
Taxa de evaporação: 0.5
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

### Desafio 3 - Depósito

**TAXA_EVAPORACAO = 0.9**

```text
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 5.0
Taxa de evaporação: 0.9
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

### Desafio 4 - Construção da rota

A construção da rota considera os nós vizinhos disponíveis, excluindo aqueles que já foram visitados. As atratividades são calculadas utilizando o feromônio e o custo da conexão, transformadas em probabilidades e utilizadas para realizar a escolha probabilística do próximo nó.

---

## Laboratório 04

### Resultado

Foram realizados testes variando o número de formigas.

#### Teste 1

```text
NUM_FORMIGAS = 5
NUM_ITERACOES = 50
ALPHA = 1.0
BETA = 5.0
TAXA_EVAPORACAO = 0.9

Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

#### Teste 2

```text
NUM_FORMIGAS = 50
NUM_ITERACOES = 50
ALPHA = 1.0
BETA = 5.0
TAXA_EVAPORACAO = 0.9

Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0
```

### Pergunta 1

O feromônio funciona como uma memória coletiva das formigas. Quando uma rota apresenta um bom resultado, ela recebe uma quantidade maior de feromônio. Nas próximas iterações, essa concentração aumenta a probabilidade de outras formigas escolherem o mesmo caminho, fazendo com que boas soluções sejam reforçadas.

### Pergunta 2

Explorar novos caminhos significa experimentar possibilidades diferentes para descobrir soluções potencialmente melhores. Aproveitar caminhos já conhecidos significa dar maior preferência às rotas que já apresentaram bons resultados. O ACO busca equilibrar esses dois comportamentos por meio da escolha probabilística e da atualização do feromônio.

### Pergunta 3

Para uma rede muito maior, eu investigaria inicialmente a quantidade de formigas e o número de iterações, pois esses parâmetros influenciam diretamente a quantidade de caminhos avaliados e o custo computacional. Também seria importante avaliar ALPHA, BETA e a taxa de evaporação para encontrar um equilíbrio entre exploração de novas rotas e aproveitamento das melhores soluções encontradas.
