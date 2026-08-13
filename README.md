# Alunos: KINSLEY CHINDA AMADI e EDUARDO LIMA


# AULA 02 — Resultados e Considerações

**Disciplina:** CIAO_ECO_2026  
**Atividade:** AC-1 — Etapa 1  
**Dupla/Trio:** PREENCHER COM OS NOMES  
**Repositório:** PREENCHER COM O LINK DO REPOSITÓRIO

---

# Laboratório 1 — Problema da Mochila

## Resultado da execução

O programa avaliou todas as combinações possíveis para os 5 itens.

| Informação | Resultado |
|---|---:|
| Número de itens | 5 |
| Capacidade da mochila | 5 |
| Soluções avaliadas | 32 |
| Melhor valor | 9 |
| Peso da solução ótima | 5 |
| Combinação ótima | (1, 1, 0, 1, 1) |

A combinação escolhida corresponde a:

- Livro — peso 2, valor 3
- Fone — peso 1, valor 2
- Carregador — peso 1, valor 3
- Chocolate — peso 1, valor 1

Total:

- Peso = 5
- Valor = 9

O tempo de execução deve ser preenchido com o valor mostrado pelo notebook,
pois depende do computador utilizado.

## Considerações

O resultado confirma que, com 5 itens, a enumeração completa é totalmente
viável. Cada item possui duas possibilidades, escolhido ou não escolhido,
resultando em `2^5 = 32` combinações.

O experimento também mostra que o número de possibilidades cresce
exponencialmente. Com 15 itens seriam `2^15 = 32.768` combinações.

Um problema semelhante no mundo real é selecionar produtos para transportar
em um veículo com limite de peso, buscando maximizar o valor dos produtos.

---

# Laboratório 2 — Caixeiro Viajante

## Resultados

| Cidades | Rotas avaliadas | Melhor custo | Tempo |
|---:|---:|---:|---:|
| 4 | 6 | 80 | preencher após execução |
| 5 | 24 | 36 | preencher após execução |
| 6 | 120 | 92 | preencher após execução |

O número de rotas segue a fórmula:

`(n - 1)!`

Assim:

- 4 cidades → `3! = 6`
- 5 cidades → `4! = 24`
- 6 cidades → `5! = 120`
- 10 cidades → `9! = 362.880`
- 15 cidades → `14! = 87.178.291.200`

## Considerações

O crescimento é fatorial e, portanto, extremamente rápido.

Para 10 cidades já existem 362.880 rotas. Para 15 cidades são mais de
87 bilhões de possibilidades.

Isso explica por que a força bruta é adequada apenas para instâncias pequenas.
Em problemas reais de roteamento, normalmente são necessários métodos mais
eficientes, heurísticas ou técnicas de otimização.

---

# Laboratório 3 — Heurística Gulosa + Gap

## Método utilizado

Foram geradas 20 instâncias aleatórias da mochila.

Para cada instância foram calculados:

1. valor ótimo por força bruta;
2. valor obtido pela heurística gulosa;
3. gap percentual.

A fórmula utilizada foi:

`gap = ((valor_otimo - valor_heuristica) / valor_otimo) * 100`

Quando o valor ótimo é zero, o gap é definido como zero para evitar divisão
por zero.

## Resultados

Os resultados completos das 20 instâncias estão registrados na saída do
notebook `lab03_aula02.ipynb`.

| Estatística | Resultado |
|---|---:|
| Número de instâncias | 20 |
| Gap médio | preencher após execução |
| Gap mínimo | preencher após execução |
| Gap máximo | preencher após execução |
| Desvio padrão | preencher após execução |

## Considerações

A heurística gulosa é uma alternativa interessante porque encontra soluções
rapidamente. Entretanto, ela não garante a solução ótima para a mochila 0/1.

Quando a instância é pequena e a qualidade da solução é muito importante,
podemos utilizar um método exato.

Quando a instância é grande e o tempo de processamento é uma preocupação,
uma heurística pode ser uma escolha melhor, aceitando eventualmente uma
solução um pouco pior em troca de uma execução muito mais rápida.

O gap permite medir quantitativamente essa diferença.

---

# Laboratório 4 — Problema Real

## Problema escolhido

Foi escolhido o problema de montar uma lista de compras mensal com orçamento
limitado.

O objetivo é escolher produtos tentando maximizar sua utilidade sem ultrapassar
o orçamento disponível.

## Representação da solução

A solução é representada por um vetor binário.

Exemplo:

`[1, 0, 1, 0, ...]`

Cada posição corresponde a um produto.

- `1` = produto escolhido;
- `0` = produto não escolhido.

## Espaço de busca

Existem 10 produtos.

Portanto:

`2^10 = 1024`

soluções possíveis.

## Função objetivo

Maximizar:

`utilidade total = soma das utilidades dos produtos escolhidos`

## Restrição

O custo total deve satisfazer:

`custo total <= R$ 80,00`

## Código

O notebook gera uma solução aleatória, calcula o custo total, calcula a
utilidade total e verifica se a solução respeita o orçamento.

## Classificação

O problema é uma variação da Mochila 0/1.

Com poucos produtos, testar todas as combinações é possível. Porém, como cada
novo produto aproximadamente dobra o espaço de busca, o problema pode se
tornar computacionalmente difícil para instâncias maiores.

## Considerações finais

A atividade mostrou como um problema cotidiano pode ser transformado em um
problema de otimização.

Foi possível identificar:

- uma representação para as soluções;
- um espaço de busca;
- uma função objetivo;
- uma restrição;
- uma forma de verificar a factibilidade.

A atividade também reforçou a importância de distinguir entre encontrar uma
solução válida e encontrar a melhor solução possível.

---

# Conclusão da AULA 02

Os quatro laboratórios permitiram observar diferentes estratégias para
problemas de otimização.

No Laboratório 1, a força bruta foi utilizada para enumerar todas as soluções
da mochila.

No Laboratório 2, observamos a explosão combinatória do TSP, cujo número de
rotas cresce de forma fatorial.

No Laboratório 3, comparamos uma heurística gulosa com a solução ótima e
utilizamos o gap para medir a diferença de qualidade.

No Laboratório 4, aplicamos os conceitos em um problema cotidiano, mostrando
como modelar uma situação real como um problema de otimização.

De maneira geral, os experimentos mostram que métodos exatos são muito úteis
para problemas pequenos, mas que o crescimento do espaço de busca exige
heurísticas e outras técnicas para problemas maiores.
