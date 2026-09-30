"""
LAB 03 — ACO para Projeto de Topologia de Rede de Baixa Latência
AULA 08 — Otimização de Sistemas Computacionais e Resiliência de Redes

Implementação do ACO do zero.

IMPORTANTE:
O enunciado fornecido não informa a matriz D 10x10.
A matriz abaixo é uma BASE DE TESTE DETERMINÍSTICA, simétrica,
gerada a partir de coordenadas fixas. Substitua D pela matriz oficial
da aula caso ela tenha sido fornecida em outro material.
"""

import numpy as np

N = 10
RHO = 0.2
FORMIGAS = 40
ITERACOES = 100
SEED = 42


def gerar_matriz_teste():
    coordenadas = np.array([
        [0, 0], [2, 5], [5, 1], [7, 6], [1, 8],
        [9, 2], [4, 9], [8, 8], [6, 4], [3, 3]
    ], dtype=float)

    d = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j:
                d[i, j] = np.linalg.norm(coordenadas[i] - coordenadas[j])
    return np.round(d, 3)


D = gerar_matriz_teste()


def aresta_existe(edges, a, b):
    return any((x == a and y == b) or (x == b and y == a) for x, y in edges)


def forma_ciclo(edges, a, b):
    """Union-find para verificar se adicionar (a,b) criaria ciclo."""
    parent = list(range(N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    for x, y in edges:
        union(x, y)

    return find(a) == find(b)


def arvore_valida(edges):
    if len(edges) != N - 1:
        return False

    parent = list(range(N))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra

    raiz = find(0)
    return all(find(i) == raiz for i in range(N))


def custo_arvore(edges):
    return float(sum(D[a, b] for a, b in edges))


def latencia_pares(edges):
    """
    Soma das menores latências entre todos os pares de switches.
    Como a solução é uma árvore, existe um único caminho entre cada par.
    """
    adj = [[] for _ in range(N)]
    for a, b in edges:
        adj[a].append((b, D[a, b]))
        adj[b].append((a, D[a, b]))

    total = 0.0

    for origem in range(N):
        dist = [np.inf] * N
        dist[origem] = 0.0
        fila = [origem]

        while fila:
            u = fila.pop(0)
            for v, peso in adj[u]:
                novo = dist[u] + peso
                if novo < dist[v]:
                    dist[v] = novo
                    fila.append(v)

        for destino in range(origem + 1, N):
            total += dist[destino]

    return float(total)


class ACO:
    def __init__(self, formigas=FORMIGAS, iteracoes=ITERACOES,
                 rho=RHO, seed=SEED):
        self.formigas = formigas
        self.iteracoes = iteracoes
        self.rho = rho
        self.rng = np.random.default_rng(seed)
        self.tau = np.ones((N, N), dtype=float)
        self.melhor_global = None
        self.melhor_custo = np.inf
        self.historico = []

    def construir_arvore(self):
        edges = []

        # Começa pelo switch 0 e expande uma árvore sem ciclos.
        conectados = {0}
        restantes = set(range(1, N))

        while restantes:
            candidatos = []
            pesos = []

            for a in conectados:
                for b in restantes:
                    if not forma_ciclo(edges, a, b):
                        candidatos.append((a, b))
                        pesos.append(
                            self.tau[a, b] ** 1.0
                            * (1.0 / (D[a, b] + 1e-9)) ** 2.0
                        )

            pesos = np.array(pesos, dtype=float)
            pesos /= pesos.sum()

            idx = self.rng.choice(len(candidatos), p=pesos)
            a, b = candidatos[idx]

            edges.append((a, b))
            conectados.add(b)
            restantes.remove(b)

        return edges

    def executar(self):
        for _ in range(self.iteracoes):
            solucoes = []

            for _ in range(self.formigas):
                arvore = self.construir_arvore()
                custo = latencia_pares(arvore)
                solucoes.append((custo, arvore))

            solucoes.sort(key=lambda x: x[0])

            melhor_iteracao = solucoes[0]
            if melhor_iteracao[0] < self.melhor_custo:
                self.melhor_custo = melhor_iteracao[0]
                self.melhor_global = melhor_iteracao[1].copy()

            # Evaporação.
            self.tau *= (1.0 - self.rho)

            # Depósito apenas pelas melhores topologias da iteração.
            elite = solucoes[:max(1, self.formigas // 5)]
            for custo, edges in elite:
                deposito = 1.0 / (custo + 1e-9)
                for a, b in edges:
                    self.tau[a, b] += deposito
                    self.tau[b, a] += deposito

            self.historico.append(self.melhor_custo)

        return self.melhor_global, self.melhor_custo


def arvore_aleatoria(seed=SEED):
    rng = np.random.default_rng(seed)
    edges = []
    conectados = {0}
    restantes = set(range(1, N))

    while restantes:
        a = rng.choice(list(conectados))
        b = rng.choice(list(restantes))
        edges.append((int(a), int(b)))
        conectados.add(int(b))
        restantes.remove(int(b))

    return edges


def matriz_adjacencia(edges):
    matriz = np.zeros((N, N), dtype=int)
    for a, b in edges:
        matriz[a, b] = 1
        matriz[b, a] = 1
    return matriz


def main():
    aco = ACO()
    melhor, custo = aco.executar()

    aleatoria = arvore_aleatoria()
    lat_aco = latencia_pares(melhor)
    lat_random = latencia_pares(aleatoria)
    ganho = 100.0 * (lat_random - lat_aco) / lat_random

    print("\n" + "=" * 70)
    print("LAB 03 — RESULTADOS")
    print("=" * 70)
    print("Matriz D:")
    print(D)
    print("\nArestas da topologia ACO:")
    print(melhor)
    print(f"\nÁrvore válida: {arvore_valida(melhor)}")
    print(f"Custo das arestas: {custo_arvore(melhor):.6f}")
    print(f"Latência acumulada entre pares: {lat_aco:.6f}")

    print("\nMatriz de Adjacência final (10x10):")
    print(matriz_adjacencia(melhor))

    print("\nTopologia aleatória:")
    print(aleatoria)
    print(f"Latência aleatória: {lat_random:.6f}")
    print(f"Ganho percentual: {ganho:.2f}%")

    # Gráfico simples da convergência sem depender de bibliotecas adicionais.
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 6))
        plt.plot(aco.historico)
        plt.title("LAB 03 — Convergência do ACO")
        plt.xlabel("Iteração")
        plt.ylabel("Latência acumulada")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("lab03_convergencia.png", dpi=150)
        plt.show()
    except ImportError:
        print("\nMatplotlib não instalado; gráfico não foi gerado.")


if __name__ == "__main__":
    main()
