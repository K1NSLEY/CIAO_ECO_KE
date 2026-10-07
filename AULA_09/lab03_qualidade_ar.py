"""Sistema fuzzy para orientar o cuidado com o ar na Marginal de São Paulo.

As leituras usadas nos testes são cenários simulados inspirados no horário de
pico, e não constituem medições oficiais de qualidade do ar.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # Permite salvar as imagens sem abrir janelas.

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


PASTA_ATUAL = Path(__file__).resolve().parent
PASTA_IMAGENS = PASTA_ATUAL / "imagens_aula09"


# 1. Universos de discurso
particulas = ctrl.Antecedent(np.arange(0, 151, 1), "particulas")
fumaca_odor = ctrl.Antecedent(np.arange(0, 10.1, 0.1), "fumaca_odor")
cuidado = ctrl.Consequent(np.arange(0, 101, 1), "cuidado")


# 2. Funções de pertinência
particulas["baixa"] = fuzz.trapmf(particulas.universe, [0, 0, 20, 45])
particulas["media"] = fuzz.trimf(particulas.universe, [25, 60, 95])
particulas["alta"] = fuzz.trapmf(particulas.universe, [75, 110, 150, 150])

fumaca_odor["fraco"] = fuzz.trapmf(fumaca_odor.universe, [0, 0, 2, 4])
fumaca_odor["moderado"] = fuzz.trimf(fumaca_odor.universe, [3, 5, 7])
fumaca_odor["intenso"] = fuzz.trapmf(fumaca_odor.universe, [6, 8, 10, 10])

cuidado["baixo"] = fuzz.trimf(cuidado.universe, [0, 0, 45])
cuidado["atencao"] = fuzz.trimf(cuidado.universe, [25, 50, 75])
cuidado["alto"] = fuzz.trimf(cuidado.universe, [55, 100, 100])


# 3. Base de regras. '&' representa E e '|' representa OU.
regras = [
    ctrl.Rule(particulas["baixa"] & fumaca_odor["fraco"], cuidado["baixo"]),
    ctrl.Rule(particulas["baixa"] & fumaca_odor["moderado"], cuidado["atencao"]),
    ctrl.Rule(particulas["media"] & fumaca_odor["fraco"], cuidado["atencao"]),
    ctrl.Rule(particulas["media"] & fumaca_odor["moderado"], cuidado["atencao"]),
    ctrl.Rule(particulas["alta"] & fumaca_odor["fraco"], cuidado["atencao"]),
    ctrl.Rule(particulas["media"] & fumaca_odor["intenso"], cuidado["alto"]),
    ctrl.Rule(particulas["alta"] & fumaca_odor["moderado"], cuidado["alto"]),
    ctrl.Rule(particulas["alta"] | fumaca_odor["intenso"], cuidado["alto"]),
]

sistema = ctrl.ControlSystem(regras)


def classificar_cuidado(valor: float) -> str:
    """Converte o número defuzzificado para o texto exibido ao usuário."""
    if valor < 33:
        return "baixo"
    if valor < 67:
        return "atenção"
    return "alto"


def calcular_cuidado(valor_particulas: float, valor_fumaca_odor: float) -> float:
    """Calcula o nível de cuidado para uma leitura do sensor."""
    simulacao = ctrl.ControlSystemSimulation(sistema)
    simulacao.input["particulas"] = valor_particulas
    simulacao.input["fumaca_odor"] = valor_fumaca_odor
    simulacao.compute()
    return float(simulacao.output["cuidado"])


def salvar_grafico(universo, conjuntos, titulo: str, eixo_x: str, arquivo: str) -> None:
    """Salva um gráfico das funções de pertinência de uma variável fuzzy."""
    fig, eixo = plt.subplots(figsize=(8, 4.5))
    for nome, valores in conjuntos.items():
        eixo.plot(universo, valores, linewidth=2, label=nome.capitalize())

    eixo.set_title(titulo)
    eixo.set_xlabel(eixo_x)
    eixo.set_ylabel("Grau de pertinência")
    eixo.set_ylim(-0.05, 1.05)
    eixo.grid(alpha=0.25)
    eixo.legend()
    fig.tight_layout()
    fig.savefig(PASTA_IMAGENS / arquivo, dpi=160)
    plt.close(fig)


def gerar_imagens(resultados: list[tuple[str, float, float, float, str]]) -> None:
    """Gera os gráficos exigidos para a documentação da atividade."""
    PASTA_IMAGENS.mkdir(exist_ok=True)

    salvar_grafico(
        particulas.universe,
        {
            "baixa": particulas["baixa"].mf,
            "media": particulas["media"].mf,
            "alta": particulas["alta"].mf,
        },
        "Partículas no ar",
        "Concentração de partículas (µg/m³)",
        "particulas.png",
    )
    salvar_grafico(
        fumaca_odor.universe,
        {
            "fraco": fumaca_odor["fraco"].mf,
            "moderado": fumaca_odor["moderado"].mf,
            "intenso": fumaca_odor["intenso"].mf,
        },
        "Intensidade de fumaça ou odor",
        "Índice do sensor (0 a 10)",
        "fumaca_odor.png",
    )
    salvar_grafico(
        cuidado.universe,
        {
            "baixo": cuidado["baixo"].mf,
            "atencao": cuidado["atencao"].mf,
            "alto": cuidado["alto"].mf,
        },
        "Nível de cuidado recomendado",
        "Nível de cuidado (0 a 100)",
        "nivel_cuidado.png",
    )

    nomes = [resultado[0] for resultado in resultados]
    valores = [resultado[3] for resultado in resultados]
    cores = ["#5d9c59" if valor < 33 else "#d4a72c" if valor < 67 else "#c94c4c" for valor in valores]
    fig, eixo = plt.subplots(figsize=(8, 4.5))
    barras = eixo.bar(nomes, valores, color=cores)
    eixo.axhline(33, color="#555555", linestyle="--", linewidth=1)
    eixo.axhline(67, color="#555555", linestyle="--", linewidth=1)
    eixo.set_title("Resultado dos cenários simulados")
    eixo.set_ylabel("Nível de cuidado (0 a 100)")
    eixo.set_ylim(0, 100)
    eixo.grid(axis="y", alpha=0.25)
    for barra, valor in zip(barras, valores):
        eixo.text(barra.get_x() + barra.get_width() / 2, valor + 2, f"{valor:.1f}", ha="center")
    fig.tight_layout()
    fig.savefig(PASTA_IMAGENS / "testes.png", dpi=160)
    plt.close(fig)


def main() -> None:
    # Cenários inspirados no trajeto às 8h, mas com leituras simuladas.
    testes = [
        ("Trânsito leve", 15, 1.5, "baixo"),
        ("Trânsito normal", 45, 4, "atenção"),
        ("Horário de pico", 80, 7, "alto"),
        ("Congestionamento intenso", 130, 9, "alto"),
    ]

    resultados = []
    for nome, valor_particulas, valor_fumaca_odor, esperado in testes:
        valor_cuidado = calcular_cuidado(valor_particulas, valor_fumaca_odor)
        classificacao = classificar_cuidado(valor_cuidado)
        resultados.append((nome, valor_particulas, valor_fumaca_odor, valor_cuidado, classificacao))
        print(
            f"{nome}: partículas={valor_particulas} µg/m³, "
            f"fumaça/odor={valor_fumaca_odor} -> "
            f"cuidado={valor_cuidado:.1f} ({classificacao}); esperado: {esperado}"
        )

    gerar_imagens(resultados)
    print(f"\nImagens salvas em: {PASTA_IMAGENS}")


if __name__ == "__main__":
    main()
