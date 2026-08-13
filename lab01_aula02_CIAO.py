# ============================================================
# ATIVIDADE 1 - Enumeracao completa do Problema da Mochila
# CIAO_ECO_2026
# ============================================================

import itertools
import time

nomes = ["Livro", "Fone", "Camiseta", "Carregador", "Chocolate"]
pesos = [2, 1, 2, 1, 1]
valores = [3, 2, 2, 3, 1]
capacidade = 5

n = len(pesos)

melhor_valor = -1
melhor_combinacao = None
total_avaliadas = 0

inicio = time.time()

for combinacao in itertools.product([0, 1], repeat=n):

    total_avaliadas += 1

    peso_total = 0
    valor_total = 0

    for i in range(n):
        if combinacao[i] == 1:
            peso_total += pesos[i]
            valor_total += valores[i]

    if peso_total <= capacidade:
        if valor_total > melhor_valor:
            melhor_valor = valor_total
            melhor_combinacao = combinacao

fim = time.time()

print("Total de solucoes avaliadas:", total_avaliadas)
print("Tempo de execucao: {:.6f} segundos".format(fim - inicio))
print("Melhor valor encontrado:", melhor_valor)
print("Combinacao otima (0=nao leva, 1=leva):", melhor_combinacao)

print("\nItens escolhidos:")

peso_final = 0

for i in range(n):
    if melhor_combinacao[i] == 1:
        peso_final += pesos[i]
        print(
            " -",
            nomes[i],
            "(peso:", pesos[i],
            ", valor:", valores[i], ")"
        )

print("\nPeso total:", peso_final)
print("Capacidade:", capacidade)

# ------------------------------------------------------------
# PERGUNTAS
# ------------------------------------------------------------

print("\nPERGUNTAS")

print("""
1. Por que o total de solucoes avaliadas e exatamente 32?

Cada um dos 5 itens pode ser escolhido ou nao escolhido.
Portanto, existem 2 possibilidades para cada item.
Assim, o total e 2^5 = 32 combinacoes.

2. O que aconteceria se eu colocasse 15 itens?

O numero de possibilidades seria 2^15 = 32.768.
Isso mostra como o espaco de busca cresce rapidamente.

3. Problema da vida real parecido:

Um exemplo e montar uma mochila para uma viagem escolhendo
objetos importantes sem ultrapassar o limite de peso.
Outros exemplos sao escolher produtos para transportar,
selecionar investimentos ou montar uma lista de compras
com um orcamento limitado.
""")
