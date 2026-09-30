"""
LAB 01 — PSO para Balanceamento Dinâmico de Carga em Datacenters
AULA 08 — Otimização de Sistemas Computacionais e Resiliência de Redes

Implementação do PSO contínuo do zero.
Dependências: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

C = np.array([42.0, 35.0, 58.0, 30.0, 50.0, 65.0])
LIMITE_CRITICO = 75.0
DIM = len(C)


def normalizar(p):
    """Garante pesos não negativos e soma exatamente 1."""
    p = np.maximum(p, 0.0)
    soma = np.sum(p)
    if soma <= 0:
        return np.ones(DIM) / DIM
    return p / soma


def fitness(posicao):
    """Temperatura média ponderada + penalidade externa."""
    w = normalizar(posicao)
    temperatura_media = float(np.dot(w, C))

    # Penalidade externa: aplicada se alguma temperatura de AZ ultrapassar 75 °C.
    excesso = np.maximum(C - LIMITE_CRITICO, 0.0)
    penalidade = 1000.0 * np.sum(excesso ** 2)

    return temperatura_media + penalidade


class PSOContinuo:
    def __init__(self, n_particulas, iteracoes=100, seed=42,
                 w=0.72, c1=1.49, c2=1.49):
        self.n = n_particulas
        self.iteracoes = iteracoes
        self.rng = np.random.default_rng(seed)
        self.inercia = w
        self.c1 = c1
        self.c2 = c2

        self.posicoes = self.rng.random((n_particulas, DIM))
        self.posicoes = self.posicoes / self.posicoes.sum(axis=1, keepdims=True)
        self.velocidades = self.rng.uniform(-0.05, 0.05, (n_particulas, DIM))

        self.pbest_pos = self.posicoes.copy()
        self.pbest_fit = np.array([fitness(p) for p in self.posicoes])

        idx = np.argmin(self.pbest_fit)
        self.gbest_pos = self.pbest_pos[idx].copy()
        self.gbest_fit = float(self.pbest_fit[idx])

        self.historico_gbest = [self.gbest_fit]
        self.historico_pbest = [self.pbest_fit.copy()]

    def executar(self):
        for _ in range(self.iteracoes):
            r1 = self.rng.random((self.n, DIM))
            r2 = self.rng.random((self.n, DIM))

            self.velocidades = (
                self.inercia * self.velocidades
                + self.c1 * r1 * (self.pbest_pos - self.posicoes)
                + self.c2 * r2 * (self.gbest_pos - self.posicoes)
            )

            self.posicoes += self.velocidades

            for i in range(self.n):
                self.posicoes[i] = normalizar(self.posicoes[i])

            fits = np.array([fitness(p) for p in self.posicoes])

            melhorou = fits < self.pbest_fit
            self.pbest_pos[melhorou] = self.posicoes[melhorou]
            self.pbest_fit[melhorou] = fits[melhorou]

            idx = np.argmin(self.pbest_fit)
            if self.pbest_fit[idx] < self.gbest_fit:
                self.gbest_fit = float(self.pbest_fit[idx])
                self.gbest_pos = self.pbest_pos[idx].copy()

            self.historico_gbest.append(self.gbest_fit)
            self.historico_pbest.append(self.pbest_fit.copy())

        return self.gbest_pos.copy(), self.gbest_fit


def main():
    resultados = []

    plt.figure(figsize=(10, 6))

    for n in (10, 30, 50):
        pso = PSOContinuo(n_particulas=n, iteracoes=100, seed=42 + n)
        melhor_w, melhor_fit = pso.executar()

        resultados.append((n, melhor_w, melhor_fit))
        plt.plot(pso.historico_gbest, label=f"{n} partículas")

    plt.title("LAB 01 — Evolução do fitness")
    plt.xlabel("Iteração")
    plt.ylabel("Melhor fitness")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("lab01_evolucao_fitness.png", dpi=150)
    plt.show()

    print("\n" + "=" * 70)
    print("LAB 01 — RESULTADOS")
    print("=" * 70)
    print(f"Coeficientes C: {C}")
    print(f"Limite crítico: {LIMITE_CRITICO:.1f} °C")
    print()

    for n, w, fit in resultados:
        print(f"População: {n}")
        print("W =", np.round(w, 6))
        print(f"sum(W) = {np.sum(w):.12f}")
        print(f"Temperatura média ponderada = {fit:.6f} °C")
        print("-" * 50)


if __name__ == "__main__":
    main()
