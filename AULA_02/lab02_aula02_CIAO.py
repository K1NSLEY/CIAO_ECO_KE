# ============================================================
# ATIVIDADE 2 - Forca-bruta no Problema do Caixeiro Viajante
# CIAO_ECO_2026
# ============================================================

import itertools
import time

try:
    import numpy as np
except ImportError:
    print("Instale numpy com: pip install numpy")
    raise


def tsp_forca_bruta(matriz_distancias):
    """Resolve o TSP avaliando todas as rotas possíveis."""

    n = len(matriz_distancias)
    cidades = list(range(1, n))

    melhor_custo = float("inf")
    melhor_rota = None
    total_rotas = 0

    for permutacao in itertools.permutations(cidades):

        total_rotas += 1

        rota = (0,) + permutacao + (0,)

        custo = 0

        for i in range(n):
            cidade_atual = rota[i]
            proxima_cidade = rota[i + 1]
            custo += matriz_distancias[cidade_atual][proxima_cidade]

        if custo < melhor_custo:
            melhor_custo = custo
            melhor_rota = rota

    return melhor_custo, melhor_rota, total_rotas


dist_4 = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

dist_5 = np.array([
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 15],
    [10, 3, 0, 4, 11],
    [19, 7, 4, 0, 14],
    [8, 15, 11, 14, 0]
])

dist_6 = np.array([
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 17, 28],
    [15, 35, 0, 30, 22, 16],
    [20, 25, 30, 0, 14, 19],
    [25, 17, 22, 14, 0, 11],
    [30, 28, 16, 19, 11, 0]
])


matrizes = [dist_4, dist_5, dist_6]
nomes_cenarios = ["4 cidades", "5 cidades", "6 cidades"]

print("=" * 65)
print("RESULTADOS DA FORCA-BRUTA NO TSP")
print("=" * 65)

resultados = []

for nome, matriz in zip(nomes_cenarios, matrizes):

    inicio = time.time()

    custo, rota, total = tsp_forca_bruta(matriz)

    tempo = time.time() - inicio

    resultados.append({
        "cidades": len(matriz),
        "rotas": total,
        "custo": custo,
        "rota": rota,
        "tempo": tempo
    })

    print(f"\n>>> {nome}")
    print(f" Rotas avaliadas : {total}")
    print(f" Melhor custo    : {custo}")
    print(f" Melhor rota     : {rota}")
    print(f" Tempo (segundos): {tempo:.6f}")

print("\n" + "=" * 65)
print("RESUMO")
print("=" * 65)

for resultado in resultados:
    print(
        f"{resultado['cidades']} cidades | "
        f"{resultado['rotas']} rotas | "
        f"custo {resultado['custo']} | "
        f"{resultado['tempo']:.6f} s"
    )

print("\nO numero de rotas cresce como (n-1)!.")
print("4 cidades -> 6 rotas")
print("5 cidades -> 24 rotas")
print("6 cidades -> 120 rotas")
print("10 cidades -> 362880 rotas")
print("15 cidades -> 87178291200 rotas")

print("""
REFLEXAO

1. O crescimento e fatorial, portanto muito mais rapido que
   um crescimento linear ou quadratico.

2. Para 10 cidades existem 9! = 362.880 rotas.

3. O TSP se torna dificil porque o numero de rotas possiveis
   cresce muito rapidamente conforme aumenta o numero de cidades.
   Avaliar todas as possibilidades deixa de ser pratico para
   instancias grandes.
""")
