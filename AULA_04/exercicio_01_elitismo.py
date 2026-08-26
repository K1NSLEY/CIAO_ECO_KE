"""Exercício 1 - comparação da estabilidade com e sem elitismo."""

import numpy as np


def calcular_custo(rota: np.ndarray, matriz: np.ndarray) -> float:
    """Calcula o custo de uma rota fechada."""
    return sum(
        matriz[rota[i], rota[(i + 1) % len(rota)]] for i in range(len(rota))
    )


def executar_ag(usar_elitismo: bool, matriz: np.ndarray, geracoes: int = 80) -> list[float]:
    """Executa o AG e devolve o melhor custo encontrado por geração."""
    tamanho_populacao = 40
    populacao = [np.random.permutation(len(matriz)) for _ in range(tamanho_populacao)]
    historico = []

    for _ in range(geracoes):
        custos = [calcular_custo(individuo, matriz) for individuo in populacao]
        melhor_idx = int(np.argmin(custos))
        historico.append(float(custos[melhor_idx]))

        nova_populacao = []
        if usar_elitismo:
            nova_populacao.append(populacao[melhor_idx].copy())

        while len(nova_populacao) < tamanho_populacao:
            i1, i2 = np.random.choice(tamanho_populacao, 2, replace=False)
            pai = populacao[i1] if custos[i1] < custos[i2] else populacao[i2]
            filho = pai.copy()
            if np.random.rand() < 0.3:
                idx1, idx2 = np.random.choice(len(matriz), 2, replace=False)
                filho[idx1], filho[idx2] = filho[idx2], filho[idx1]
            nova_populacao.append(filho)
        populacao = nova_populacao

    return historico


if __name__ == "__main__":
    # A mesma matriz e as mesmas sementes tornam a comparação justa e reproduzível.
    num_nos = 8
    np.random.seed(2026)
    matriz_teste = np.random.uniform(10, 100, (num_nos, num_nos))
    np.fill_diagonal(matriz_teste, 0.0)

    np.random.seed(2026)
    com_elitismo = executar_ag(True, matriz_teste)
    np.random.seed(2026)
    sem_elitismo = executar_ag(False, matriz_teste)

    print("[Exercício 1] Comparação de elitismo")
    print(f"Menor custo com elitismo: {min(com_elitismo):.2f}")
    print(f"Menor custo sem elitismo: {min(sem_elitismo):.2f}")
    print(f"Última geração com elitismo: {com_elitismo[-1]:.2f}")
    print(f"Última geração sem elitismo: {sem_elitismo[-1]:.2f}")
