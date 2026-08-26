# ============================================================
# ATIVIDADE 3 - Heuristica Gulosa + Gap de Otimalidade
# CIAO_ECO_2026
# ============================================================

import numpy as np
import itertools


def mochila_otima(pesos, valores, capacidade):
    """Encontra o valor ótimo por força bruta."""

    n = len(pesos)
    melhor = 0

    for comb in itertools.product([0, 1], repeat=n):

        peso = sum(
            pesos[i]
            for i in range(n)
            if comb[i] == 1
        )

        if peso <= capacidade:

            valor = sum(
                valores[i]
                for i in range(n)
                if comb[i] == 1
            )

            if valor > melhor:
                melhor = valor

    return melhor


def mochila_gulosa(pesos, valores, capacidade):
    """
    Heurística gulosa baseada na densidade valor/peso.
    """

    n = len(pesos)

    densidade = [
        (valores[i] / pesos[i], i)
        for i in range(n)
    ]

    densidade.sort(reverse=True)

    valor_total = 0
    peso_atual = 0

    for dens, i in densidade:

        if peso_atual + pesos[i] <= capacidade:

            peso_atual += pesos[i]
            valor_total += valores[i]

    return valor_total


def calcular_gap(valor_heuristica, valor_otimo):
    """
    Calcula o gap percentual entre a heurística e o ótimo.

    gap = ((ótimo - heurística) / ótimo) * 100

    Quando o ótimo é zero, retorna zero.
    """

    if valor_otimo == 0:
        return 0.0

    return (
        (valor_otimo - valor_heuristica)
        / valor_otimo
    ) * 100


# ------------------------------------------------------------
# EXPERIMENTO
# ------------------------------------------------------------

np.random.seed(42)

n_itens = 12
capacidade = 30
n_instancias = 20

gaps = []
resultados = []

print("Rodando", n_instancias, "instancias...\n")

for k in range(n_instancias):

    pesos = np.random.randint(
        1, 15, size=n_itens
    )

    valores = np.random.randint(
        10, 50, size=n_itens
    )

    otimo = mochila_otima(
        pesos,
        valores,
        capacidade
    )

    heur = mochila_gulosa(
        pesos,
        valores,
        capacidade
    )

    gap = calcular_gap(
        heur,
        otimo
    )

    gaps.append(gap)

    resultados.append({
        "instancia": k + 1,
        "otimo": int(otimo),
        "gulosa": int(heur),
        "gap": float(gap)
    })

    print(
        f"Instancia {k + 1:2d} | "
        f"Otimo: {otimo:4d} | "
        f"Gulosa: {heur:4d} | "
        f"Gap: {gap:5.1f}%"
    )


print("\n===== RESUMO =====")

print(f"Gap medio     : {np.mean(gaps):.2f}%")
print(f"Gap minimo    : {np.min(gaps):.2f}%")
print(f"Gap maximo    : {np.max(gaps):.2f}%")
print(f"Desvio padrao : {np.std(gaps):.2f}%")


print("""
CONCLUSAO

A heurística gulosa é rápida e simples, sendo adequada quando
precisamos obter uma boa solução em pouco tempo.

Entretanto, ela não garante a solução ótima para o problema da
mochila 0/1. Quando a qualidade da solução é crítica e a instância
é pequena o suficiente para permitir força bruta ou outro método
exato, vale a pena gastar mais tempo para encontrar o ótimo.

Para problemas grandes, nos quais a enumeração completa seria
inviável, uma heurística pode representar um compromisso adequado
entre qualidade da solução e tempo de processamento.
""")
