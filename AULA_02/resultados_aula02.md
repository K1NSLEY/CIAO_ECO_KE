# AULA 02 — Resultados e Considerações

**Disciplina:** CIAO_ECO_2026  
**Atividade:** AC-1 — Etapa 1  
**Dupla:** Kinsley Chinda Amadi (97399) e Eduardo Lima (105764)

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

Com cinco itens, testar tudo ainda é tranquilo: são só 32 combinações. A
melhor escolha usou toda a capacidade da mochila e deixou de fora apenas os
itens que não ajudavam a aumentar o valor final.

O problema escala rápido. Com 15 itens já seriam 32.768 possibilidades, o que
mostra por que procurar todas as combinações deixa de ser uma boa ideia em
casos maiores. A mesma lógica serve, por exemplo, para montar uma carga de
veículo sem ultrapassar o peso permitido.

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

Os números deixam o problema bem claro: com quatro, cinco e seis cidades o
programa ainda termina rápido, mas o total de rotas cresce em fatorial. Para
dez cidades já seriam 362.880 rotas; para quinze, mais de 87 bilhões.

Por isso, força bruta funciona para entender o problema e conferir exemplos
pequenos, mas não é uma saída prática para roteamento real. Nesses casos,
heurísticas passam a fazer mais sentido.

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

O método guloso é rápido porque toma decisões locais, mas isso não garante a
melhor mochila possível. Foi justamente para enxergar essa diferença que o
gap foi calculado em cada instância.

Se a instância for pequena e a resposta ótima for indispensável, vale usar um
método exato. Quando o conjunto cresce, aceitar uma resposta um pouco pior em
troca de velocidade pode ser a escolha mais realista.

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

Esse laboratório ajudou a colocar a modelagem em termos mais concretos: cada
produto vira uma posição no vetor, o orçamento vira restrição e a utilidade é
o que queremos maximizar. Uma lista que cabe no orçamento é válida, mas isso
não quer dizer que seja a melhor lista possível - essa foi a diferença mais
importante observada no exercício.

---

# Conclusão da AULA 02

Os quatro laboratórios formaram uma sequência coerente: primeiro foi possível
testar todas as alternativas; depois apareceu o custo desse tipo de busca; em
seguida, a comparação com a heurística mostrou o preço de ganhar velocidade;
e, por fim, o mesmo raciocínio foi aplicado a uma situação cotidiana.

Em resumo, métodos exatos são ótimos quando o problema cabe no tempo de
execução. Quando não cabe, é preciso aceitar soluções aproximadas e medir bem
o quanto se perdeu em qualidade.
