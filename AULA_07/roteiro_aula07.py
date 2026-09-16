# AC2 - PARTE 2: VALOR DE 0,25
# LABORATORIO PRAKTICO DE META-HEURISTICAS
#
# Versao corrigida para execucao em Python.
# Este arquivo pode ser executado como um roteiro de referencia e tambem como
# conjunto de exemplos resolvidos dos laboratorios da aula 07.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)


def lab01_aco_hibrido():
    print("\n=== LAB 01: ACO com Busca Local ===")
    dist_matrix = np.array([
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 35, 0, 30, 5],
        [20, 25, 30, 0, 15],
        [25, 30, 5, 15, 0]
    ])

    num_nodes = len(dist_matrix)
    num_ants = 10
    num_iterations = 50
    alpha = 1.0
    beta = 2.0
    rho = 0.1
    pheromone = np.ones((num_nodes, num_nodes))
    best_cost = float('inf')
    best_path = None
    convergence = []

    def local_search_2opt(path, matrix):
        improved = True
        best_local_path = list(path)
        best_local_cost = sum(
            matrix[best_local_path[i], best_local_path[i + 1]]
            for i in range(len(best_local_path) - 1)
        )

        while improved:
            improved = False
            for i in range(1, len(best_local_path) - 2):
                for j in range(i + 1, len(best_local_path) - 1):
                    new_path = (
                        best_local_path[:i]
                        + best_local_path[i:j + 1][::-1]
                        + best_local_path[j + 1:]
                    )
                    new_cost = sum(
                        matrix[new_path[k], new_path[k + 1]]
                        for k in range(len(new_path) - 1)
                    )
                    if new_cost < best_local_cost:
                        best_local_cost = new_cost
                        best_local_path = new_path
                        improved = True
        return best_local_path, best_local_cost

    for _ in range(num_iterations):
        paths = []
        costs = []

        for _ in range(num_ants):
            path = [0]
            unvisited = list(range(1, num_nodes))

            while unvisited:
                curr = path[-1]
                probabilities = []
                for nxt in unvisited:
                    tau = pheromone[curr][nxt] ** alpha
                    eta = (1.0 / dist_matrix[curr][nxt]) ** beta
                    probabilities.append(tau * eta)
                probabilities = np.array(probabilities)
                probabilities /= probabilities.sum()
                nxt_node = np.random.choice(unvisited, p=probabilities)
                path.append(nxt_node)
                unvisited.remove(nxt_node)

            path.append(0)
            path, cost = local_search_2opt(path, dist_matrix)
            paths.append(path)
            costs.append(cost)

            if cost < best_cost:
                best_cost = cost
                best_path = path.copy()

        pheromone *= (1 - rho)
        for path, cost in zip(paths, costs):
            for i in range(len(path) - 1):
                pheromone[path[i]][path[i + 1]] += 1.0 / cost

        convergence.append(best_cost)

    print(f"[LAB 01 - SUCESSO] Melhor Caminho: {[int(node) for node in best_path]} | Custo: {best_cost}")
    plt.plot(convergence)
    plt.xlabel("Iteracao")
    plt.ylabel("Melhor custo")
    plt.title("Convergencia do ACO Hibrido")
    plt.grid()
    plt.show()


def lab02_ag_mochila():
    print("\n=== LAB 02: Algoritmo Genetico ===")
    weights = np.array([12, 2, 1, 4, 1])
    values = np.array([4, 2, 1, 10, 2])
    max_weight = 15
    pop_size = 10
    num_genes = len(weights)
    generations = 10
    mutation_rate = 0.1
    population = np.random.randint(0, 2, size=(pop_size, num_genes))

    def calculate_fitness(ind):
        total_weight = np.sum(ind * weights)
        total_value = np.sum(ind * values)
        if total_weight > max_weight:
            return 0
        return total_value

    def tournament_selection(pop, fitnesses):
        idx1, idx2 = np.random.choice(len(pop), size=2, replace=False)
        if fitnesses[idx1] >= fitnesses[idx2]:
            return pop[idx1]
        return pop[idx2]

    def crossover(parent1, parent2):
        point = np.random.randint(1, num_genes)
        child1 = np.concatenate([parent1[:point], parent2[point:]])
        child2 = np.concatenate([parent2[:point], parent1[point:]])
        return child1, child2

    def mutate(ind):
        ind = np.copy(ind)
        for i in range(num_genes):
            if np.random.rand() < mutation_rate:
                ind[i] = 1 - ind[i]
        return ind

    for _ in range(generations):
        fitnesses = np.array([calculate_fitness(ind) for ind in population])
        new_population = []
        for _ in range(pop_size // 2):
            p1 = tournament_selection(population, fitnesses)
            p2 = tournament_selection(population, fitnesses)
            c1, c2 = crossover(p1, p2)
            new_population.extend([mutate(c1), mutate(c2)])
        population = np.array(new_population)

    final_fitnesses = np.array([calculate_fitness(ind) for ind in population])
    best_idx = np.argmax(final_fitnesses)
    best_ind = population[best_idx]
    best_fit = final_fitnesses[best_idx]
    best_weight = np.sum(best_ind * weights)
    print(f"[LAB 02] Melhor Solucao: {best_ind}")
    print(f"[LAB 02] Fitness: {best_fit}")
    print(f"[LAB 02] Peso: {best_weight}/{max_weight}")


def lab03_pso():
    print("\n=== LAB 03: PSO ===")
    def fitness_function(position):
        return np.sum(position ** 2)

    num_particles = 10
    dimensions = 2
    max_iter = 15
    X = np.random.uniform(-5, 5, (num_particles, dimensions))
    V = np.random.uniform(-1, 1, (num_particles, dimensions))
    pbest_X = np.copy(X)
    pbest_fitness = np.array([fitness_function(p) for p in pbest_X])
    gbest_index = np.argmin(pbest_fitness)
    gbest_X = np.copy(pbest_X[gbest_index])

    w = 0.5
    c1 = 1.5
    c2 = 1.5

    for _ in range(max_iter):
        for i in range(num_particles):
            r1, r2 = np.random.rand(), np.random.rand()
            V[i] = (w * V[i]) + (c1 * r1 * (pbest_X[i] - X[i])) + (c2 * r2 * (gbest_X - X[i]))
            X[i] = X[i] + V[i]
            current_fitness = fitness_function(X[i])
            if current_fitness < pbest_fitness[i]:
                pbest_fitness[i] = current_fitness
                pbest_X[i] = X[i]
                if current_fitness < fitness_function(gbest_X):
                    gbest_X = np.copy(X[i])

    print(f"[LAB 03] Melhor posicao encontrada pelo Enxame (gbest): {gbest_X}")
    print(f"[LAB 03] Fitness do gbest: {fitness_function(gbest_X):.6f}")


def lab04_aco_feromonio():
    print("\n=== LAB 04: ACO - Feromonio ===")
    latency_matrix = np.array([
        [0, 5, 2, 9],
        [5, 0, 3, 1],
        [2, 3, 0, 7],
        [9, 1, 7, 0]
    ])

    num_nodes = len(latency_matrix)
    pheromone = np.ones((num_nodes, num_nodes))
    rho = 0.25

    def update_pheromone(pheromone_matrix, paths, costs, rho):
        pheromone_matrix = (1.0 - rho) * pheromone_matrix
        for path, cost in zip(paths, costs):
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                pheromone_matrix[u][v] += (1.0 / cost)
        return pheromone_matrix

    mock_paths = [[0, 2, 1, 3], [0, 1, 3]]
    mock_costs = [6.0, 6.0]
    updated_pheromone = update_pheromone(pheromone, mock_paths, mock_costs, rho)
    print("[LAB 04] Matriz de Feromonio Atualizada:\n", updated_pheromone)


def lab05_memetico():
    print("\n=== LAB 05: Memetico ===")
    def rastrigin(x):
        return 10 * len(x) + sum(x**2 - 10 * np.cos(2 * np.pi * x))

    def local_search_hill_climbing(solution, step_size=0.01, max_steps=20):
        current_sol = np.copy(solution)
        current_fit = rastrigin(current_sol)
        for _ in range(max_steps):
            neighbor = current_sol + np.random.uniform(-step_size, step_size, size=len(solution))
            neighbor_fit = rastrigin(neighbor)
            if neighbor_fit < current_fit:
                current_sol, current_fit = neighbor, neighbor_fit
        return current_sol, current_fit

    initial_solution = np.array([2.5, -3.1])
    refined_solution, final_fit = local_search_hill_climbing(initial_solution)
    print(f"[LAB 05] Solucao Inicial: {initial_solution} | Fitness: {rastrigin(initial_solution):.4f}")
    print(f"[LAB 05] Solucao Refinada: {refined_solution} | Fitness: {final_fit:.4f}")


if __name__ == "__main__":
    lab01_aco_hibrido()
    lab02_ag_mochila()
    lab03_pso()
    lab04_aco_feromonio()
    lab05_memetico()

    print("\nQuestao 1 (LAB 01): O 2-opt atua como intensificacao local depois da exploracao global do ACO; ele reordena trechos da rota para reduzir custo sem abandonar a busca ampla. ")
    print("Questao 2 (LAB 01): Se rho = 0.0, o feromonio nao evapora, acumula-se indefinidamente e a convergencia tende a ser prematura, com pouca diversidade e maior risco de ficar em solucoes locais. ")
    print("Questao 1 (LAB 02): A mutacao introduce diversidade genetica e ajuda a escapar de otimos locais. Com taxa 100%, a populacao se torna essencialmente aleatoria e o algoritmo perde convergencia. ")
    print("Questao 2 (LAB 02): A penalizacao por peso impede que individuos inviaveis ganhem vantagem, forcando a evolucao a explorar apenas solucoes validas dentro da restricao. ")
    print("Questao 1 (LAB 03): Com c1=0, as particulas perdem a memoria individual e passam a seguir principalmente o melhor global, aumentando risco de convergir para minimo local. ")
    print("Questao 2 (LAB 03): A inercia w equilibra exploracao e explotacao; w alto favorece ampla exploracao, enquanto w baixo favorece refinamento local. ")
    print("Questao 1 (LAB 04): A evaporacao evita que feromonio antigo domine a busca e permite esquecimento de caminhos pouco promissores. ")
    print("Questao 2 (LAB 04): Sem evaporacao, em grafos complexos, caminhos antigos e pouco bons podem dominar o feromonio e bloquear a exploracao; eta = 1 / latencia, ou seja, enlaces mais curtos/rapidos possuem maior atratividade inicial. ")
    print("Questao 1 (LAB 05): AG puro depende da evolucao populacional para explorar o espaco; ja o memetico combina evolucao com busca local intensiva em cada individuo. ")
    print("Questao 2 (LAB 05): Aplicar busca local para todos os individuos a cada geracao aumenta muito o custo computacional, pois multiplica o numero de avaliacoes da funcao objetivo pelo tamanho da populacao e pelo numero de passos locais. ")



