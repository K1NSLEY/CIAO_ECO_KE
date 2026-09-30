"""
LAB 02 — AG Binário para Seleção de Microsserviços em Edge
AULA 08 — Otimização de Sistemas Computacionais e Resiliência de Redes

Implementação do Algoritmo Genético do zero.

IMPORTANTE:
O enunciado fornecido não informa os 15 valores de negócio/RAM/CPU.
Os dados abaixo são uma BASE DE TESTE DETERMINÍSTICA para permitir execução.
Se a aula disponibilizar uma tabela oficial, substitua somente SERVICOS.
"""

import numpy as np
import matplotlib.pyplot as plt

SERVICOS = [
    ("svc01", 82, 2.0, 1.0),
    ("svc02", 75, 1.5, 1.5),
    ("svc03", 91, 3.0, 2.0),
    ("svc04", 64, 1.0, 0.5),
    ("svc05", 88, 2.5, 1.0),
    ("svc06", 70, 2.0, 2.0),
    ("svc07", 95, 4.0, 2.5),
    ("svc08", 55, 1.0, 1.0),
    ("svc09", 79, 2.0, 1.5),
    ("svc10", 68, 1.5, 0.5),
    ("svc11", 86, 3.0, 1.0),
    ("svc12", 73, 2.0, 1.5),
    ("svc13", 97, 4.0, 2.0),
    ("svc14", 61, 1.0, 0.5),
    ("svc15", 84, 2.5, 1.5),
]

RAM_MAX = 16.0
CPU_MAX = 8.0


def consumo(individuo):
    ram = sum(g * s[2] for g, s in zip(individuo, SERVICOS))
    cpu = sum(g * s[3] for g, s in zip(individuo, SERVICOS))
    valor = sum(g * s[1] for g, s in zip(individuo, SERVICOS))
    return valor, ram, cpu


def fitness(individuo, estrategia):
    valor, ram, cpu = consumo(individuo)
    excesso_ram = max(0.0, ram - RAM_MAX)
    excesso_cpu = max(0.0, cpu - CPU_MAX)

    if estrategia == "A":
        if excesso_ram > 0 or excesso_cpu > 0:
            return 0.0
        return float(valor)

    # Estratégia B: redução proporcional ao excesso relativo.
    penalidade_ram = excesso_ram / RAM_MAX
    penalidade_cpu = excesso_cpu / CPU_MAX
    fator = max(0.0, 1.0 - (penalidade_ram + penalidade_cpu))
    return float(valor * fator)


def diversidade(populacao):
    """Média da distância de Hamming para todos os pares."""
    if len(populacao) < 2:
        return 0.0
    distancias = []
    for i in range(len(populacao)):
        for j in range(i + 1, len(populacao)):
            distancias.append(np.mean(populacao[i] != populacao[j]))
    return float(np.mean(distancias))


class AlgoritmoGenetico:
    def __init__(self, estrategia, tamanho=60, geracoes=100,
                 taxa_mutacao=0.02, seed=42):
        self.estrategia = estrategia
        self.tamanho = tamanho
        self.geracoes = geracoes
        self.taxa_mutacao = taxa_mutacao
        self.rng = np.random.default_rng(seed)

        self.populacao = self.rng.integers(
            0, 2, size=(tamanho, len(SERVICOS))
        )

        self.media = []
        self.desvio = []
        self.diversidade = []
        self.melhor = None
        self.melhor_fitness = -np.inf

    def selecionar_torneio(self, fitnesses, k=3):
        indices = self.rng.choice(len(self.populacao), size=k, replace=False)
        vencedor = indices[np.argmax(fitnesses[indices])]
        return self.populacao[vencedor].copy()

    def crossover(self, p1, p2):
        ponto = self.rng.integers(1, len(SERVICOS))
        return (
            np.concatenate([p1[:ponto], p2[ponto:]]),
            np.concatenate([p2[:ponto], p1[ponto:]])
        )

    def mutar(self, individuo):
        mascara = self.rng.random(len(individuo)) < self.taxa_mutacao
        individuo[mascara] = 1 - individuo[mascara]
        return individuo

    def executar(self):
        for _ in range(self.geracoes):
            fitnesses = np.array([
                fitness(ind, self.estrategia) for ind in self.populacao
            ])

            self.media.append(float(np.mean(fitnesses)))
            self.desvio.append(float(np.std(fitnesses)))
            self.diversidade.append(diversidade(self.populacao))

            idx = np.argmax(fitnesses)
            if fitnesses[idx] > self.melhor_fitness:
                self.melhor_fitness = float(fitnesses[idx])
                self.melhor = self.populacao[idx].copy()

            nova = []
            elite = self.populacao[idx].copy()
            nova.append(elite)

            while len(nova) < self.tamanho:
                p1 = self.selecionar_torneio(fitnesses)
                p2 = self.selecionar_torneio(fitnesses)
                f1, f2 = self.crossover(p1, p2)
                nova.extend([self.mutar(f1), self.mutar(f2)])

            self.populacao = np.array(nova[:self.tamanho])

        return self.melhor, self.melhor_fitness


def imprimir_resultado(nome, melhor, fit):
    valor, ram, cpu = consumo(melhor)
    selecionados = [
        SERVICOS[i][0] for i, bit in enumerate(melhor) if bit
    ]

    print("\n" + "=" * 70)
    print(nome)
    print("=" * 70)
    print("Indivíduo:", melhor.tolist())
    print("Serviços:", selecionados)
    print(f"Valor de negócio: {valor:.2f}")
    print(f"RAM: {ram:.2f} / {RAM_MAX:.2f} GB")
    print(f"CPU: {cpu:.2f} / {CPU_MAX:.2f} cores")
    print(f"Fitness: {fit:.2f}")


def main():
    ag_a = AlgoritmoGenetico("A", seed=42)
    melhor_a, fit_a = ag_a.executar()

    ag_b = AlgoritmoGenetico("B", seed=42)
    melhor_b, fit_b = ag_b.executar()

    imprimir_resultado("ESTRATÉGIA A — PENALIDADE RÍGIDA", melhor_a, fit_a)
    imprimir_resultado("ESTRATÉGIA B — PENALIDADE PROPORCIONAL", melhor_b, fit_b)

    print("\nComparação final:")
    print(f"A — média final: {ag_a.media[-1]:.4f}")
    print(f"A — desvio final: {ag_a.desvio[-1]:.4f}")
    print(f"A — diversidade final: {ag_a.diversidade[-1]:.4f}")
    print(f"B — média final: {ag_b.media[-1]:.4f}")
    print(f"B — desvio final: {ag_b.desvio[-1]:.4f}")
    print(f"B — diversidade final: {ag_b.diversidade[-1]:.4f}")

    plt.figure(figsize=(10, 6))
    plt.plot(ag_a.media, label="Estratégia A — média")
    plt.plot(ag_b.media, label="Estratégia B — média")
    plt.fill_between(
        range(len(ag_a.media)),
        np.array(ag_a.media) - np.array(ag_a.desvio),
        np.array(ag_a.media) + np.array(ag_a.desvio),
        alpha=0.15,
    )
    plt.fill_between(
        range(len(ag_b.media)),
        np.array(ag_b.media) - np.array(ag_b.desvio),
        np.array(ag_b.media) + np.array(ag_b.desvio),
        alpha=0.15,
    )
    plt.title("LAB 02 — Média do fitness por geração")
    plt.xlabel("Geração")
    plt.ylabel("Fitness")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("lab02_fitness.png", dpi=150)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(ag_a.diversidade, label="Estratégia A")
    plt.plot(ag_b.diversidade, label="Estratégia B")
    plt.title("LAB 02 — Diversidade genética")
    plt.xlabel("Geração")
    plt.ylabel("Distância de Hamming média")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("lab02_diversidade.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
