import pytest

from src.uti_triagem import avaliar_paciente, criar_sistema_triagem_uti


@pytest.fixture
def simulador_uti():
    return criar_sistema_triagem_uti()


def test_paciente_saudavel_baixo_risco(simulador_uti):
    risco = avaliar_paciente(simulador_uti, 75, 98)
    assert risco < 30.0


def test_salto_nao_linear_queda_spo2(simulador_uti):
    risco_spo2_95 = avaliar_paciente(simulador_uti, 75, 95)
    risco_spo2_89 = avaliar_paciente(simulador_uti, 75, 89)

    assert risco_spo2_95 < 35.0
    assert risco_spo2_89 > 65.0
    assert risco_spo2_89 > risco_spo2_95


def test_validacao_limites_fisiologicos(simulador_uti):
    with pytest.raises(ValueError):
        avaliar_paciente(simulador_uti, 39, 98)

    with pytest.raises(ValueError):
        avaliar_paciente(simulador_uti, 75, 101)