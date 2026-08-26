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

Neste laboratório, o cromossomo de 5 bits representa um número entre 0 e 31,
e o objetivo é fazer `x²` ficar o maior possível. A execução chegou em
`x = 31`, com fitness 961, que é justamente o melhor resultado possível no
intervalo.

Deu para perceber o papel de cada etapa do algoritmo: o torneio favorece os
melhores candidatos, o crossover mistura características e a mutação evita
que a população fique sempre igual. O elitismo ajudou a não perder o melhor
indivíduo quando ele apareceu na geração 6.


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

No OneMax a leitura é direta: quanto mais posições com valor 1, melhor. Como
o cromossomo tem 20 bits, o teto é 20. Ele já foi atingido na geração 10 e se
manteve até o final.

Também ficou evidente que os parâmetros importam. Uma mutação alta demais pode
desfazer soluções boas; população pequena reduz a variedade; e retirar o
elitismo pode fazer o melhor resultado sumir. Não há um único ajuste perfeito:
depende de quanto se quer explorar e de quanto se quer preservar.


---

# LAB-03 — Execução do código semi-pronto

## Output

```text
(Nenhuma saída textual foi produzida.)
```


## Considerações da dupla

No LAB-03 a parte principal foi completar as funções que faltavam. Primeiro,
`bits_para_x` converte os 8 bits para um valor no intervalo definido. Depois,
a função de fitness avalia esse valor, e a mutação faz a inversão de bits com
a probabilidade configurada.

Com isso preenchido, o restante do algoritmo conseguiu avaliar, selecionar e
gerar novas soluções normalmente. Como há sorteio na seleção e na mutação, é
esperado que execuções diferentes não sigam exatamente o mesmo caminho.

