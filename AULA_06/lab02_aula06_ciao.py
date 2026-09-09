# LABORATÓRIO 02 — EXPERIMENTANDO O ACO

# Objetivo: compreender, por meio de experimentos, como os principais parâmetros do ACO influenciam a busca por uma boa rota.

# Neste laboratório, o código principal já está pronto. O trabalho será modificar os parâmetros, executar novamente e registrar os resultados.

# 1. Código

# Use como base o código completo do Laboratório 01. Para facilitar os experimentos, acrescente no início:

# # ============================================================
# PARÂMETROS DO EXPERIMENTO
# ============================================================

NUM_FORMIGAS = 20
NUM_ITERACOES = 50

ALPHA = 1.0
BETA = 2.0

TAXA_EVAPORACAO = 0.5
Q = 100

# E, ao final da execução:

print("\n========== RESULTADO DO EXPERIMENTO ==========")
print("Número de formigas:", NUM_FORMIGAS)
print("Número de iterações:", NUM_ITERACOES)
print("ALPHA:", ALPHA)
print("BETA:", BETA)
print("Taxa de evaporação:", TAXA_EVAPORACAO)
print("Melhor rota:", melhor_rota)
print("Melhor custo:", melhor_custo)
# 2. Experimento 1 — Influência do ALPHA

# Execute inicialmente:

ALPHA = 1.0
BETA = 2.0

# Depois teste:

ALPHA = 0.1

# e:

ALPHA = 5.0

# Mantenha os demais parâmetros iguais.

# Observe:

# melhor rota;
# melhor custo;
# curva de convergência;
# concentração do feromônio.

# Pergunta para discussão:

# Quando aumentamos o ALPHA, a influência da experiência acumulada pelas formigas aumenta ou diminui?

# 3. Experimento 2 — Influência do BETA

# Volte para:

ALPHA = 1.0

# Agora teste:

BETA = 0.5

# Depois:

BETA = 5.0

# Observe o comportamento.

# A ideia é perceber que:

# BETA baixo
# → o custo influencia menos

# BETA alto
# → caminhos de menor custo ficam mais atrativos
# 4. Experimento 3 — Evaporação

# Teste:

TAXA_EVAPORACAO = 0.1

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
Formiga 1: [0, 1, 2, 4, 3, 5]
Formiga 2: [0, 1, 2, 4, 3, 5]
Formiga 3: [0, 1, 2, 3, 4, 5]
Formiga 4: [0, 1, 2, 3, 4, 5]
Formiga 5: [0, 1, 2, 3, 4, 5]

Rota: [0, 2, 1, 3, 4, 5]
Custo: 13.0

========== RESULTADO ==========
Melhor rota encontrada: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

========== RESULTADO DO EXPERIMENTO ==========
Número de formigas: 20
Número de iterações: 50
ALPHA: 1.0
BETA: 5.0
Taxa de evaporação: 0.1
Melhor rota: [0, 1, 2, 3, 4, 5]
Melhor custo: 8.0

# Depois:

TAXA_EVAPORACAO = 0.9

# Compare os resultados.

# A pergunta principal é: O que acontece quando o algoritmo esquece rapidamente as experiências anteriores?

# 5. Experimento 4 — Número de formigas

# Teste:

# NUM_FORMIGAS = 5

# Depois:

# NUM_FORMIGAS = 50

# Compare o comportamento.
