"""Exercício 2 - custo de rota com penalidades por descumprimento de SLA."""

import numpy as np


def calcular_custo_com_sla(
    rota: np.ndarray, matriz: np.ndarray, limite_sla: float = 50.0
) -> float:
    """Soma as latências e 1000 ms por enlace acima do limite de SLA."""
    custo_total = 0.0
    penalidade = 0.0
    for i in range(len(rota) - 1):
        latencia_enlace = matriz[rota[i], rota[i + 1]]
        custo_total += latencia_enlace
        if latencia_enlace > limite_sla:
            penalidade += 1000.0
    return custo_total + penalidade


if __name__ == "__main__":
    np.random.seed(15)
    matriz_latencia = np.random.uniform(5, 80, (6, 6))
    rota_teste = np.array([0, 1, 2, 3, 4, 5])
    custo_final = calcular_custo_com_sla(rota_teste, matriz_latencia)
    print(f"[Exercício 2] Custo Total (Com Penalizações de SLA): {custo_final:.2f} ms")
