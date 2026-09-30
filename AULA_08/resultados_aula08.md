# Alunos: KINSLEY CHINDA AMADI (97399) e EDUARDO LIMA (RA: 105764)

# AULA 08 — Resultados e Considerações

Disciplina: CIAO_ECO_2026  
Atividade: Fechamento da AC-2 — etapa 2 da fase final

## Reprodutibilidade e fonte dos dados

Os resultados abaixo foram obtidos pela execução local dos arquivos `lab01_aula08.py`, `lab02_aula08.py` e `lab03_aula08.py`, em 30/09/2026, com as sementes fixas existentes nos próprios códigos. Os gráficos foram gerados na mesma execução.

O roteiro não fornece a tabela oficial com Valor de Negócio, RAM e CPU dos 15 microsserviços, nem a matriz oficial de latências `D` (10×10). Portanto:

- o LAB 02 usa a base determinística `SERVICOS` declarada em `lab02_aula08.py`;
- o LAB 03 usa a matriz `D` determinística calculada a partir das coordenadas declaradas em `lab03_aula08.py`.

Logo, os números desses dois laboratórios são resultados reais da execução dessas bases de teste, mas não devem ser interpretados como resultados de uma eventual base oficial que não foi disponibilizada no roteiro.

## Laboratório 1 — PSO para balanceamento dinâmico de carga

O PSO foi executado com 100 iterações para populações de 10, 30 e 50 partículas. Em cada atualização, os pesos são normalizados, preservando `sum(W) = 1`. Nenhum coeficiente de aquecimento ultrapassa o limite crítico de 75 °C; por isso, a penalidade externa foi zero em todos os casos.

| População | Melhor W = [w1, w2, w3, w4, w5, w6] | sum(W) | Temperatura média ponderada |
|---:|---|---:|---:|
| 10 | [0, 0, 0, 1, 0, 0] | 1,000000000000 | 30,000000 °C |
| 30 | [0, 0, 0, 1, 0, 0] | 1,000000000000 | 30,000000 °C |
| 50 | [0, 0, 0, 1, 0, 0] | 1,000000000000 | 30,000000 °C |

O resultado é coerente com a função objetivo: como `C = [42, 35, 58, 30, 50, 65]`, o menor coeficiente é o da quarta AZ (30 °C). Sem uma restrição adicional de capacidade ou de distribuição mínima por AZ, concentrar todo o peso nessa AZ minimiza a média ponderada.

Gráfico gerado: `lab01_evolucao_fitness.png`.

## Laboratório 2 — AG binário para seleção de microsserviços

Foram executadas 100 gerações, com população 60, seleção por torneio, crossover de ponto único, elitismo e mutação binária de 2%.

| Estratégia | Serviços selecionados | Valor | RAM (GB) | CPU (cores) | Fitness | Situação |
|---|---|---:|---:|---:|---:|---|
| A — penalidade rígida | svc01, svc03, svc04, svc05, svc09, svc10, svc11, svc14 | 619,00 | 16,00 / 16,00 | 8,00 / 8,00 | 619,00 | Viável |
| B — penalidade proporcional | svc01, svc02, svc04, svc05, svc08, svc10, svc11, svc14, svc15 | 663,00 | 16,00 / 16,00 | 8,50 / 8,00 | 621,56 | **Inviável** |

| Métrica na última geração | Estratégia A | Estratégia B |
|---|---:|---:|
| Média do fitness | 555,5167 | 587,7396 |
| Desvio-padrão do fitness | 154,2857 | 76,1325 |
| Diversidade genética (Hamming média) | 0,0477 | 0,0477 |

As duas estratégias terminaram com a mesma diversidade genética medida. A estratégia B obteve maior fitness médio, mas a melhor solução que ela reteve viola o limite de CPU; portanto, para o requisito de respeitar simultaneamente 16 GB de RAM e 8 cores de CPU, a combinação final válida desta execução é a da estratégia A, com valor de negócio 619,00.

Gráficos gerados: `lab02_fitness.png` e `lab02_diversidade.png`.

## Laboratório 3 — ACO para topologia de rede de baixa latência

O ACO foi executado com 40 formigas, 100 iterações e evaporação `rho = 0,2`. A topologia encontrada possui 9 arestas, não forma ciclos e conecta os 10 switches; portanto, é uma árvore geradora válida.

**Arestas da topologia ACO:**

```text
[(0, 9), (9, 8), (9, 1), (1, 4), (9, 2), (8, 3), (8, 5), (3, 7), (1, 6)]
```

**Matriz de adjacência final (10×10):**

```text
[[0 0 0 0 0 0 0 0 0 1]
 [0 0 0 0 1 0 1 0 0 1]
 [0 0 0 0 0 0 0 0 0 1]
 [0 0 0 0 0 0 0 1 1 0]
 [0 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 1 0]
 [0 1 0 0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0 0]
 [0 0 0 1 0 1 0 0 0 1]
 [1 1 1 0 0 0 0 0 1 0]]
```

| Medida | Resultado |
|---|---:|
| Árvore válida | Sim |
| Custo das arestas selecionadas | 28,181000 |
| Latência acumulada entre pares — ACO | 343,543000 |
| Latência acumulada entre pares — árvore aleatória | 792,464000 |
| Redução de latência | 56,65% |

O percentual foi calculado diretamente por `(latência_aleatória - latência_ACO) / latência_aleatória × 100` para a árvore aleatória gerada com a mesma semente do código.

Gráfico gerado: `lab03_convergencia.png`.

## Conclusão

O LAB 01 confirmou a convergência do PSO para a AZ com menor coeficiente de aquecimento, dado o objetivo sem restrições adicionais de balanceamento. No LAB 02, a penalidade rígida produziu a melhor seleção viável observada; a penalidade proporcional manteve uma solução com fitness maior, porém fora do limite de CPU. No LAB 03, o ACO construiu uma árvore válida e reduziu a latência acumulada em 56,65% em relação à árvore aleatória usada na execução.
