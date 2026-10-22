"""Aula 10 — motor Mamdani e superfície de decisão 3D.

Executar (na pasta AULA_10):
    python -m pip install -r requirements.txt
    python lab01_aula10.py

O programa codifica as nove regras da matriz, compara os métodos do desafio
dos extremos e grava superficie_decisao.png na mesma pasta deste arquivo.
"""

from pathlib import Path

import matplotlib

# Permite executar sem abrir janelas e salva a figura para a entrega.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


PASTA_ATUAL = Path(__file__).resolve().parent


def criar_sistema(forma_critica="triangulo", metodo="centroid"):
    """Monta a base Mamdani com as 9 regras solicitadas.

    forma_critica: ``triangulo`` reproduz o desafio original; ``trapezio``
    aumenta a região de pertinência máxima perto de 100.
    metodo: método de defuzzificação do consequente (``centroid`` ou ``mom``).
    """
    impacto = ctrl.Antecedent(np.arange(0, 101, 1), "impacto")
    explorabilidade = ctrl.Antecedent(
        np.arange(0, 10.01, 0.1), "explorabilidade"
    )
    urgencia = ctrl.Consequent(
        np.arange(0, 100.01, 0.1), "urgencia", defuzzify_method=metodo
    )

    # Entradas: os conjuntos se sobrepõem e cobrem todo o domínio informado.
    impacto["baixo"] = fuzz.trapmf(impacto.universe, [0, 0, 20, 40])
    impacto["medio"] = fuzz.trimf(impacto.universe, [20, 50, 80])
    impacto["alto"] = fuzz.trapmf(impacto.universe, [60, 80, 100, 100])

    explorabilidade["baixa"] = fuzz.trapmf(
        explorabilidade.universe, [0, 0, 2, 4]
    )
    explorabilidade["moderada"] = fuzz.trimf(
        explorabilidade.universe, [2, 5, 8]
    )
    explorabilidade["alta"] = fuzz.trapmf(
        explorabilidade.universe, [6, 8, 10, 10]
    )

    # A base triangular nas bordas reproduz o viés do centroide: 4,33 e 87,50.
    urgencia["baixa"] = fuzz.trimf(urgencia.universe, [0, 0, 13])
    urgencia["media"] = fuzz.trimf(urgencia.universe, [20, 50, 80])
    urgencia["alta"] = fuzz.trimf(urgencia.universe, [45, 70, 85])
    if forma_critica == "trapezio":
        urgencia["critica"] = fuzz.trapmf(
            urgencia.universe, [62.5, 85, 100, 100]
        )
    else:
        urgencia["critica"] = fuzz.trimf(urgencia.universe, [62.5, 100, 100])

    # Matriz 3 x 3: linhas = impacto; colunas = explorabilidade.
    regras = [
        ctrl.Rule(impacto["baixo"] & explorabilidade["baixa"], urgencia["baixa"]),
        ctrl.Rule(impacto["baixo"] & explorabilidade["moderada"], urgencia["baixa"]),
        ctrl.Rule(impacto["baixo"] & explorabilidade["alta"], urgencia["media"]),
        ctrl.Rule(impacto["medio"] & explorabilidade["baixa"], urgencia["media"]),
        ctrl.Rule(impacto["medio"] & explorabilidade["moderada"], urgencia["alta"]),
        ctrl.Rule(impacto["medio"] & explorabilidade["alta"], urgencia["alta"]),
        ctrl.Rule(impacto["alto"] & explorabilidade["baixa"], urgencia["critica"]),
        ctrl.Rule(impacto["alto"] & explorabilidade["moderada"], urgencia["critica"]),
        ctrl.Rule(impacto["alto"] & explorabilidade["alta"], urgencia["critica"]),
    ]
    return ctrl.ControlSystem(regras)


def calcular(sistema, impacto, explorabilidade):
    """Executa uma simulação isolada e retorna a urgência numérica."""
    simulador = ctrl.ControlSystemSimulation(sistema, cache=False)
    simulador.input["impacto"] = impacto
    simulador.input["explorabilidade"] = explorabilidade
    simulador.compute()
    return simulador.output["urgencia"]


def gerar_superficie(sistema):
    """Calcula a saída em toda a grade de entrada e salva a superfície 3D."""
    impactos = np.arange(0, 101, 2)
    explorabilidades = np.arange(0, 10.01, 0.2)
    grade_impacto, grade_explorabilidade = np.meshgrid(impactos, explorabilidades)
    saida = np.empty_like(grade_impacto, dtype=float)

    for linha, explorabilidade in enumerate(explorabilidades):
        for coluna, impacto in enumerate(impactos):
            saida[linha, coluna] = calcular(sistema, impacto, explorabilidade)

    figura = plt.figure(figsize=(11, 8))
    eixo = figura.add_subplot(111, projection="3d")
    superficie = eixo.plot_surface(
        grade_impacto,
        grade_explorabilidade,
        saida,
        cmap="viridis",
        edgecolor="none",
        antialiased=True,
    )
    eixo.set_title("Superfície de decisão do sistema Mamdani", pad=18)
    eixo.set_xlabel("Impacto (%)", labelpad=10)
    eixo.set_ylabel("Explorabilidade", labelpad=10)
    eixo.set_zlabel("Urgência (%)", labelpad=10)
    eixo.set_xlim(0, 100)
    eixo.set_ylim(0, 10)
    eixo.set_zlim(0, 100)
    eixo.view_init(elev=28, azim=-130)
    figura.colorbar(superficie, ax=eixo, shrink=0.62, pad=0.1, label="Urgência (%)")
    figura.tight_layout()
    caminho = PASTA_ATUAL / "superficie_decisao.png"
    figura.savefig(caminho, dpi=180, bbox_inches="tight")
    plt.close(figura)
    return caminho


def main():
    sistemas = {
        "Centroide + triângulos": criar_sistema("triangulo", "centroid"),
        "Centroide + trapézio crítico": criar_sistema("trapezio", "centroid"),
        "MOM + triângulos": criar_sistema("triangulo", "mom"),
    }

    print("Comparação do desafio dos extremos")
    print(f"{'Método':<34} {'(0, 0)':>10} {'(100, 10)':>12}")
    print("-" * 60)
    for nome, sistema in sistemas.items():
        minimo = calcular(sistema, 0, 0)
        maximo = calcular(sistema, 100, 10)
        print(f"{nome:<34} {minimo:>9.2f}% {maximo:>11.2f}%")

    caminho = gerar_superficie(sistemas["Centroide + triângulos"])
    print(f"\nSuperfície 3D salva em: {caminho.name}")


if __name__ == "__main__":
    main()
