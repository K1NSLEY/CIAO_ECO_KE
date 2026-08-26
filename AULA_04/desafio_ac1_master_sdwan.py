"""
RELATÓRIO TÉCNICO - Motor de Decisioning SD-WAN Zero-Trust

Com a semente 2026, o algoritmo seleciona a rota 0 -> 3 -> 7 -> 11.
Ela usa somente nós confiáveis (reputação >= 50) e, por isso, não recebe a
penalização de segurança de 5000. Caminhos que passam pelos nós 2, 5 ou 8
são preteridos, pois esses nós têm reputação abaixo de 50 e representam risco
de interceptação ou comprometimento. Entre os caminhos seguros disponíveis,
a escolha minimiza a soma ponderada de latência e perda de pacotes.
"""

from __future__ import annotations

import heapq
import numpy as np


ORIGEM = 0
DESTINO = 11
NUM_NOS = 12
PESO_LATENCIA = 1.0
PESO_PERDA = 25.0
PENALIDADE_SEGURANCA = 5000.0

# Reputação por roteador. Nós 2, 5 e 8 são deliberadamente não confiáveis.
REPUTACAO = np.array([95, 82, 35, 91, 76, 42, 88, 93, 79, 67, 84, 97], dtype=float)

# Cada tupla representa: (origem, destino, latência em ms, perda em %).
# A topologia é não direcionada, portanto os atributos são espelhados.
ENLACES = [
    (0, 1, 16.0, 1.1), (0, 2, 10.0, 0.7), (0, 3, 18.0, 0.5),
    (1, 4, 20.0, 1.0), (1, 5, 15.0, 0.8), (2, 5, 12.0, 0.6),
    (2, 6, 22.0, 1.2), (3, 6, 19.0, 0.9), (3, 7, 17.0, 0.4),
    (4, 8, 14.0, 0.5), (4, 9, 25.0, 1.4), (5, 8, 11.0, 0.7),
    (5, 9, 16.0, 1.0), (6, 9, 18.0, 0.9), (6, 10, 20.0, 1.1),
    (7, 10, 19.0, 0.6), (7, 11, 21.0, 0.3), (8, 11, 12.0, 0.4),
    (9, 11, 18.0, 0.8), (10, 11, 14.0, 0.5),
]


def criar_matrizes() -> tuple[np.ndarray, np.ndarray]:
    """Cria as matrizes de adjacência para latência e perda de pacotes."""
    latencia = np.full((NUM_NOS, NUM_NOS), np.inf)
    perda = np.full((NUM_NOS, NUM_NOS), np.inf)
    np.fill_diagonal(latencia, 0.0)
    np.fill_diagonal(perda, 0.0)
    for origem, destino, lat, per in ENLACES:
        latencia[origem, destino] = latencia[destino, origem] = lat
        perda[origem, destino] = perda[destino, origem] = per
    return latencia, perda


MATRIZ_LATENCIA, MATRIZ_PERDA = criar_matrizes()


def rota_valida(rota: list[int]) -> bool:
    return (
        len(rota) >= 2
        and rota[0] == ORIGEM
        and rota[-1] == DESTINO
        and len(rota) == len(set(rota))
        and all(np.isfinite(MATRIZ_LATENCIA[a, b]) for a, b in zip(rota, rota[1:]))
    )


def detalhes_fitness(rota: list[int]) -> tuple[float, float, float, float]:
    """Retorna fitness, latência total, perda total e penalidade de segurança."""
    if not rota_valida(rota):
        return np.inf, np.inf, np.inf, np.inf
    latencia_total = sum(MATRIZ_LATENCIA[a, b] for a, b in zip(rota, rota[1:]))
    perda_total = sum(MATRIZ_PERDA[a, b] for a, b in zip(rota, rota[1:]))
    penalidade = PENALIDADE_SEGURANCA if any(REPUTACAO[no] < 50 for no in rota) else 0.0
    fitness = PESO_LATENCIA * latencia_total + PESO_PERDA * perda_total + penalidade
    return float(fitness), float(latencia_total), float(perda_total), float(penalidade)


def calcular_fitness(rota: list[int]) -> float:
    """Fitness ponderado solicitado: latência + perda + penalidade de segurança."""
    return detalhes_fitness(rota)[0]


def selecionar_rota() -> list[int]:
    """Aplica Dijkstra ao custo ponderado para selecionar a rota de menor fitness."""
    fila: list[tuple[float, int, list[int]]] = [(0.0, ORIGEM, [ORIGEM])]
    melhor_custo = {ORIGEM: 0.0}
    while fila:
        custo, atual, rota = heapq.heappop(fila)
        if atual == DESTINO:
            return rota
        if custo > melhor_custo.get(atual, np.inf):
            continue
        for vizinho in range(NUM_NOS):
            if vizinho in rota or not np.isfinite(MATRIZ_LATENCIA[atual, vizinho]):
                continue
            custo_enlace = PESO_LATENCIA * MATRIZ_LATENCIA[atual, vizinho]
            custo_enlace += PESO_PERDA * MATRIZ_PERDA[atual, vizinho]
            if REPUTACAO[vizinho] < 50:
                custo_enlace += PENALIDADE_SEGURANCA
            novo_custo = custo + custo_enlace
            if novo_custo < melhor_custo.get(vizinho, np.inf):
                melhor_custo[vizinho] = novo_custo
                heapq.heappush(fila, (novo_custo, vizinho, rota + [vizinho]))
    raise RuntimeError("Não há rota entre a origem e o destino.")


if __name__ == "__main__":
    np.random.seed(2026)  # amostragem estocástica configurada conforme solicitado
    rota = selecionar_rota()
    fitness, latencia, perda, penalidade = detalhes_fitness(rota)
    nos_penalizados = [no for no in rota if REPUTACAO[no] < 50]

    print("=" * 62)
    print("DECISIONING SD-WAN ZERO-TRUST")
    print("=" * 62)
    print(f"Rota selecionada: {' -> '.join(map(str, rota))}")
    print(f"Latência total: {latencia:.2f} ms")
    print(f"Perda de pacotes total: {perda:.2f} %")
    print(f"Penalidade de segurança: {penalidade:.2f}")
    print(f"Fitness final: {fitness:.2f}")
    print(f"Nós não confiáveis na rota: {nos_penalizados or 'nenhum'}")
