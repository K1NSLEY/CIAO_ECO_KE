# Alunos: KINSLEY CHINDA AMADI (97399) e EDUARDO LIMA (RA: 105764)

# AULA 08 — Fechamento da AC-2

Disciplina: CIAO_ECO_2026  
Atividade: Fechamento da AC-2 — etapa 2 da fase final

## Observação sobre os dados

Os três programas foram executados em 30/09/2026 com as sementes definidas nos arquivos. Os gráficos incluídos na pasta foram gerados nessa execução.

O enunciado apresenta os limites do LAB 02 e descreve a matriz do LAB 03, mas não traz a tabela com os 15 microsserviços nem a matriz de latências 10×10. Por isso, os scripts trabalham com os dados fixos que estão neles:

- no LAB 02, a lista `SERVICOS` de `lab02_aula08.py`;
- no LAB 03, a matriz `D` calculada a partir das coordenadas de `lab03_aula08.py`.

Assim, os valores registrados aqui são os que os programas realmente retornaram para essas bases, e não uma tentativa de completar dados que não foram fornecidos.

## Laboratório 1 — PSO para balanceamento dinâmico de carga

Foram feitas 100 iterações para populações de 10, 30 e 50 partículas. A normalização foi aplicada em cada iteração; por isso, a soma dos pesos permaneceu igual a 1. Nenhum dos coeficientes de aquecimento passa de 75 °C, então a penalidade não entrou no cálculo nesta execução.

| População | Melhor W = [w1, w2, w3, w4, w5, w6] | sum(W) | Temperatura média ponderada |
|---:|---|---:|---:|
| 10 | [0, 0, 0, 1, 0, 0] | 1,000000000000 | 30,000000 °C |
| 30 | [0, 0, 0, 1, 0, 0] | 1,000000000000 | 30,000000 °C |
| 50 | [0, 0, 0, 1, 0, 0] | 1,000000000000 | 30,000000 °C |

O resultado faz sentido para a função usada. Em `C = [42, 35, 58, 30, 50, 65]`, o menor valor é 30, na quarta AZ. Como não há limite de carga por AZ nem peso mínimo para as demais, o melhor caso é colocar todo o peso nessa zona.

Gráfico gerado: `lab01_evolucao_fitness.png`.

## Laboratório 2 — AG binário para seleção de microsserviços

O AG foi executado por 100 gerações, com população de 60 indivíduos, torneio, crossover de um ponto, elitismo e mutação de 2%.

| Estratégia | Serviços selecionados | Valor | RAM (GB) | CPU (cores) | Fitness | Situação |
|---|---|---:|---:|---:|---:|---|
| A — penalidade rígida | svc01, svc03, svc04, svc05, svc09, svc10, svc11, svc14 | 619,00 | 16,00 / 16,00 | 8,00 / 8,00 | 619,00 | Viável |
| B — penalidade proporcional | svc01, svc02, svc04, svc05, svc08, svc10, svc11, svc14, svc15 | 663,00 | 16,00 / 16,00 | 8,50 / 8,00 | 621,56 | **Inviável** |

| Métrica na última geração | Estratégia A | Estratégia B |
|---|---:|---:|
| Média do fitness | 555,5167 | 587,7396 |
| Desvio-padrão do fitness | 154,2857 | 76,1325 |
| Diversidade genética (Hamming média) | 0,0477 | 0,0477 |

As duas populações chegaram à mesma diversidade final. A estratégia B teve média de fitness maior, mas seu melhor indivíduo usa 8,5 cores e ultrapassa o limite de 8. Portanto, considerando as duas restrições, a melhor solução válida desta execução é a da estratégia A, com valor de negócio 619,00.

Gráficos gerados: `lab02_fitness.png` e `lab02_diversidade.png`.

## Laboratório 3 — ACO para topologia de rede de baixa latência

O ACO foi executado com 40 formigas, 100 iterações e `rho = 0,2`. A solução tem 9 arestas, conecta os 10 switches e não possui ciclo. Ela atende, portanto, à condição de árvore geradora.

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

O ganho foi calculado por `(latência aleatória - latência ACO) / latência aleatória × 100`, usando a árvore aleatória criada pelo próprio programa com a mesma semente.

Gráfico gerado: `lab03_convergencia.png`.

## Fechamento

No LAB 01, o PSO encontrou a AZ com menor coeficiente de aquecimento. No LAB 02, a penalidade rígida foi a que entregou a melhor combinação que respeita RAM e CPU; a proporcional favoreceu uma solução que excedeu CPU. Por fim, no LAB 03, o ACO montou uma árvore válida e reduziu em 56,65% a latência acumulada quando comparada à árvore aleatória usada no teste.
