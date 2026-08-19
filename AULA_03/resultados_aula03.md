# AULA 03 — AC-1 PARTE 2

## Identificação da dupla

| Aluno | RA |
|---|---:|
| Kinsley Chinda Amadi | 97399 |
| Eduardo Lima | 105764 |

---

# LAB-01 — Compreensão e Execução

## Output

```text
==================================================
ALGORITMO GENÉTICO PASSO A PASSO
==================================================

População inicial: [[0, 0, 0, 0, 1], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 1, 1], [0, 0, 0, 1, 1], [0, 1, 0, 0, 1]]

==================== GERAÇÃO 0 ====================

Avaliação dos indivíduos:
  [0, 0, 0, 0, 1] → x= 1 → f(x)=  1
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [0, 0, 0, 0, 0] → x= 0 → f(x)=  0
  [1, 0, 0, 1, 1] → x=19 → f(x)=361
  [0, 0, 0, 1, 1] → x= 3 → f(x)=  9
  [0, 1, 0, 0, 1] → x= 9 → f(x)= 81

 Melhor: x = 27 → f(x) = 729

==================== GERAÇÃO 1 ====================

Avaliação dos indivíduos:
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 0, 1, 1, 1] → x=23 → f(x)=529
  [1, 1, 0, 1, 0] → x=26 → f(x)=676
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 0, 0, 1, 1] → x=19 → f(x)=361

 Melhor: x = 27 → f(x) = 729

==================== GERAÇÃO 2 ====================

Avaliação dos indivíduos:
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 0, 0, 1, 1] → x=19 → f(x)=361
  [1, 0, 0, 1, 0] → x=18 → f(x)=324

 Melhor: x = 27 → f(x) = 729

==================== GERAÇÃO 3 ====================

Avaliação dos indivíduos:
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 0, 0] → x=24 → f(x)=576
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 0, 1, 1, 0] → x=22 → f(x)=484

 Melhor: x = 27 → f(x) = 729

==================== GERAÇÃO 4 ====================

Avaliação dos indivíduos:
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 0, 1, 1, 0] → x=22 → f(x)=484
  [1, 1, 0, 0, 0] → x=24 → f(x)=576
  [1, 1, 0, 1, 1] → x=27 → f(x)=729

 Melhor: x = 27 → f(x) = 729

==================== GERAÇÃO 5 ====================

Avaliação dos indivíduos:
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 0, 1] → x=25 → f(x)=625
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 1, 0] → x=26 → f(x)=676
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 0, 0, 1] → x=25 → f(x)=625

 Melhor: x = 27 → f(x) = 729

==================== GERAÇÃO 6 ====================

Avaliação dos indivíduos:
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 0, 0, 1] → x=25 → f(x)=625
  [0, 1, 0, 0, 1] → x= 9 → f(x)= 81
  [1, 1, 0, 0, 1] → x=25 → f(x)=625
  [1, 1, 0, 0, 1] → x=25 → f(x)=625

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 7 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 0, 0, 0] → x=24 → f(x)=576
  [1, 1, 0, 0, 1] → x=25 → f(x)=625
  [1, 1, 0, 0, 1] → x=25 → f(x)=625
  [1, 1, 0, 0, 1] → x=25 → f(x)=625
  [0, 1, 0, 0, 1] → x= 9 → f(x)= 81

 Melhor: x = 31 → f(x) = 961

==================================================
RESULTADO FINAL
==================================================

Melhor indivíduo: [1, 1, 1, 1, 1]
x = 31
f(x) = 961

Ótimo global: x = 31, f(x) = 961
Erro: 0

<Figure size 1000x400 with 1 Axes>
```


## Considerações da dupla

No LAB-01 analisamos a aplicação de um Algoritmo Genético para
maximizar a função f(x) = x² no intervalo [0,31].

A solução é representada por um cromossomo binário de 5 bits.
O fitness corresponde ao valor da função objetivo, portanto
indivíduos com valores maiores de x possuem maior fitness.

O algoritmo utiliza mecanismos de seleção, crossover, mutação
e elitismo. O elitismo permite preservar o melhor indivíduo
encontrado, enquanto crossover e mutação permitem explorar
novas soluções.

O ótimo global conhecido é x = 31, com f(x) = 961.

Como existem operações aleatórias, diferentes execuções podem
produzir resultados diferentes.


---

# LAB-02 — Execução do código pronto

## Output

```text
==================================================
ONEMAX - AG com 30 indivíduos, 50 gerações
==================================================
Geração   0: Melhor = 13/20, Média = 9.63
Geração  10: Melhor = 20/20, Média = 18.03
Geração  20: Melhor = 20/20, Média = 19.47
Geração  30: Melhor = 20/20, Média = 19.80
Geração  40: Melhor = 20/20, Média = 19.73

 MELHOR FITNESS: 20/20
   Ótimo = 20 (todos os bits são 1)

<Figure size 1200x400 with 2 Axes>


==================================================
DESAFIO: Mude os parâmetros e veja o que acontece!
==================================================
1. Aumente a TAXA_MUT para 0.1. O que acontece?
2. Diminua POPULACAO para 10. O que acontece?
3. Aumente GERACOES para 100. O que acontece?
4. Mude ELITE para 0. O que acontece?
```


## Considerações da dupla

No LAB-02 analisamos o problema OneMax. O objetivo é maximizar
a quantidade de bits iguais a 1 em um cromossomo.

Nesse problema, o fitness corresponde diretamente ao número
de bits 1. Portanto, para um cromossomo de tamanho 20, o ótimo
global é fitness igual a 20.

Foram observados os mecanismos de seleção por torneio,
crossover, mutação e elitismo.

Os parâmetros utilizados pelo Algoritmo Genético influenciam
seu comportamento. Alterações na população, quantidade de
gerações, taxa de mutação e elitismo podem modificar a
velocidade de convergência e a qualidade das soluções.


---

# LAB-03 — Execução do código semi-pronto

## Output

```text
(Nenhuma saída textual foi produzida.)
```


## Considerações da dupla

No LAB-03 foram implementadas as funções solicitadas no código
semi-pronto.

A função bits_para_x transforma o cromossomo binário de 8 bits
em um valor real no intervalo [X_MIN, X_MAX].

A função fitness utiliza o valor de x para calcular a função
objetivo, que deve ser maximizada.

A função mutacao implementa a mutação bit-flip. Cada bit possui
uma probabilidade definida por TAXA_MUT de ser invertido.

Depois dessas implementações, o Algoritmo Genético consegue
avaliar os indivíduos, realizar seleção, crossover e mutação,
buscando uma solução com alto valor de fitness.

Devido à natureza aleatória do algoritmo, os valores encontrados
podem variar entre execuções.

