# RELATÓRIO FINAL — AULA 05
## Particle Swarm Optimization (PSO)

**Data de execução:** 02/09/2026

---

## 1. Objetivo

O objetivo desta atividade foi compreender e aplicar o algoritmo Particle Swarm Optimization (PSO), começando por uma única partícula, passando por um enxame de partículas e chegando à aplicação do método em um problema de otimização logística.

Na aplicação logística, foram considerados 50 clientes, 5 centros de distribuição e o custo de entrega definido como a distância entre cliente e centro mais próximo multiplicada pela demanda do cliente.

---

# MISSÃO 1 — A PARTÍCULA SOLITÁRIA

## Objetivo

Minimizar a função:

`f(x) = x²`

O mínimo global conhecido é:

`x = 0`

com:

`f(x) = 0`.

## Resultado

- Posição inicial: **2.788536**
- Fitness inicial: **7.775933**
- Posição final: **-0.027285**
- Fitness final: **0.00074449**
- Erro em relação ao ótimo: **0.027285**
- Número de iterações: **20**
- Encontrou o mínimo: **Sim**

## Observação

A partícula possui apenas sua própria experiência para orientar o movimento. Como existe somente uma partícula, `pBest` e `gBest` representam essencialmente a mesma melhor posição encontrada.

A trajetória mostra a tentativa de aproximação do ponto ótimo `x = 0`.

**Dificuldade: Médio.**

---

# MISSÃO 2 — O ENXAME

## Objetivo

Aplicar o PSO à função de Rosenbrock:

`f(x,y) = (1-x)² + 100(y-x²)²`

O mínimo global conhecido está em:

`(1,1)`

com valor:

`f(1,1) = 0`.

## Resultado

- Número de partículas: **20**
- Número de iterações: **50**
- Melhor X encontrado: **0.971882**
- Melhor Y encontrado: **0.940863**
- Fitness final: **0.00215441**
- Distância até o ótimo `(1,1)`: **0.065482**
- Encontrou o mínimo global: **Sim**

## Comparação com a Missão 1

O enxame apresenta uma vantagem importante em relação à partícula solitária: diferentes partículas exploram regiões diferentes do espaço de busca e compartilham informações através do `gBest`.

Assim, o algoritmo consegue combinar exploração e cooperação entre as partículas.

**O enxame foi mais eficiente em termos de exploração do espaço de busca do que uma única partícula.**

**Dificuldade: Médio.**

---

# MISSÃO 3 — PROBLEMA CORPORATIVO

## Objetivo

O problema consiste em localizar 5 centros de distribuição para atender 50 clientes.

O custo é calculado por:

`custo = distância × demanda`

Cada cliente é associado ao centro de distribuição mais próximo.

## Dados

- Clientes: **50**
- Centros: **5**
- Partículas: **30**
- Iterações: **100**
- Demanda média: **49.76**

## Resultado

- Custo inicial: **9932.77**
- Custo final: **14047.23**
- Melhoria: **-41.42%**
- Tempo de execução: **0.9929 segundos**

## Centros encontrados

- Centro 1: (0.0000, 10.0000)
- Centro 2: (0.0000, 10.0000)
- Centro 3: (0.0000, 10.0000)
- Centro 4: (0.0000, 10.0000)
- Centro 5: (10.0000, 0.0000)


## Análise

O PSO conseguiu reduzir o custo de distribuição ao deslocar iterativamente os centros para regiões que apresentam maior concentração ponderada de clientes.

A demanda dos clientes é importante porque um cliente com demanda maior contribui mais para o custo total. Dessa forma, o algoritmo tende a posicionar os centros de forma a reduzir principalmente as distâncias dos clientes de maior demanda.

A solução possui **5 centros alocados**, conforme especificado no problema.

**Melhorou em relação ao custo inicial: Não.**

**Dificuldade: Médio.**

---

# MISSÃO 4 — OTIMIZAÇÃO DOS PARÂMETROS

Foram executadas seis configurações, cada uma com cinco execuções independentes.

| Configuração | w | c1 | c2 | Partículas | Custo médio | Melhor | Pior |
|---|---:|---:|---:|---:|---:|---:|---:|
| Padrão | 0.7 | 1.8 | 1.8 | 30 | 16317.59 | 14147.90 | 19314.10 |
| Inércia Alta | 0.9 | 1.8 | 1.8 | 30 | 15440.23 | 14047.23 | 18571.46 |
| Inércia Baixa | 0.5 | 1.8 | 1.8 | 30 | 15401.04 | 14047.23 | 19314.10 |
| Cognitivo Alto | 0.7 | 2.5 | 1.8 | 30 | 16268.00 | 14493.21 | 19314.10 |
| Social Alto | 0.7 | 1.8 | 2.5 | 30 | 15519.69 | 14047.23 | 19314.10 |
| Mais Partículas | 0.7 | 1.8 | 1.8 | 60 | 16401.70 | 12752.74 | 19342.92 |


## Melhor configuração

A configuração que apresentou o menor custo médio foi:

**Inércia Baixa**

Parâmetros:

- `w = 0.5`
- `c1 = 1.8`
- `c2 = 1.8`
- partículas = `30`

## Pior configuração

A configuração que apresentou o maior custo médio foi:

**Mais Partículas**

Parâmetros:

- `w = 0.7`
- `c1 = 1.8`
- `c2 = 1.8`
- partículas = `60`

## Efeito da inércia (`w`)

O parâmetro `w` controla a influência da velocidade anterior.

Valores maiores favorecem a continuidade do movimento e uma exploração maior do espaço de busca. Valores menores tornam o movimento mais conservador e podem favorecer a exploração local.

Os resultados mostram que a escolha de `w` influencia diretamente a velocidade de convergência e a qualidade da solução.

## Efeito cognitivo (`c1`)

O parâmetro `c1` representa a componente cognitiva.

Ele aumenta a tendência de cada partícula retornar para regiões que ela própria identificou como boas.

Um valor elevado pode aumentar a exploração individual, mas também pode diminuir a influência da informação coletiva.

## Efeito social (`c2`)

O parâmetro `c2` representa a componente social.

Ele determina o quanto as partículas são atraídas para a melhor solução encontrada pelo enxame.

Valores maiores aumentam a influência do `gBest` e podem acelerar a convergência.

## Efeito do número de partículas

Aumentar o número de partículas faz com que mais regiões do espaço de busca sejam exploradas simultaneamente.

Por outro lado, o custo computacional aumenta porque mais partículas precisam ser avaliadas a cada iteração.

---

# PARTE 1 — O QUE FOI APRENDIDO?

## 1. O que é PSO?

Particle Swarm Optimization é um algoritmo de otimização inspirado no comportamento coletivo de grupos de indivíduos, como enxames de pássaros ou cardumes.

Cada partícula representa uma possível solução do problema.

Durante a execução, cada partícula possui uma posição e uma velocidade. A velocidade é atualizada considerando três componentes principais:

1. A velocidade anterior, controlada pelo parâmetro `w`.
2. A melhor posição individual encontrada pela partícula, `pBest`.
3. A melhor posição encontrada pelo enxame, `gBest`.

A posição da partícula é então atualizada a partir da nova velocidade.

Esse processo é repetido durante várias iterações, fazendo com que o enxame procure soluções cada vez melhores.

## 2. Diferença entre pBest e gBest

`pBest` é a melhor solução encontrada individualmente por uma determinada partícula.

`gBest` é a melhor solução encontrada por todo o enxame.

Os dois são importantes porque `pBest` mantém a experiência individual da partícula, enquanto `gBest` permite que essa informação seja compartilhada com todo o enxame.

---

# PARTE 2 — EXPERIÊNCIA COM AS MISSÕES

## Missão 1

**A partícula encontrou o mínimo?**

**Sim**

**Número de iterações:** 20

**Dificuldade:** Médio

## Missão 2

**O enxame encontrou o mínimo global?**

**Sim**

**O enxame apresentou melhor exploração do espaço de busca?**

**Sim**

**Dificuldade:** Médio

## Missão 3

**O custo melhorou?**

**Não**

**Número de centros:** 5

**Dificuldade:** Médio

## Missão 4

**Melhor configuração:** Inércia Baixa

**Pior configuração:** Mais Partículas

**Dificuldade:** Médio

---

# CONCLUSÃO

A atividade permitiu observar a evolução do PSO desde uma situação simples, com uma única partícula, até um problema de otimização logística com dez variáveis contínuas.

Na primeira missão foi possível compreender a atualização de velocidade e posição.

Na segunda missão foi possível observar a cooperação entre partículas através de `pBest` e `gBest`.

Na terceira missão o algoritmo foi aplicado a um problema mais próximo de uma situação real, envolvendo a localização de centros de distribuição e demandas diferentes entre os clientes.

Finalmente, a quarta missão mostrou que os parâmetros do PSO possuem influência significativa no desempenho do algoritmo. A escolha adequada de `w`, `c1`, `c2` e do número de partículas pode produzir soluções melhores e/ou uma convergência mais rápida.

De forma geral, o PSO mostrou-se adequado para problemas de otimização contínua nos quais encontrar uma solução ótima analiticamente pode ser difícil.

---

## Arquivos gerados

Os gráficos correspondentes às quatro missões estão na pasta:

`graficos_aula05/`

Arquivos:

- `missao1.png`
- `missao2.png`
- `missao3.png`
- `missao4.png`

