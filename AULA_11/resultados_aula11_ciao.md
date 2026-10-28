# Resultados da Aula 11: Triagem de risco na UTI

Implementei um sistema fuzzy Mamdani que recebe frequência cardíaca (40 a 160 bpm) e SpO₂ (70 a 100%) e retorna um risco de 0 a 100%. A saída usa o método do centroide. Também incluí a validação dos limites das entradas, que retorna `ValueError` para valores fora da faixa.

As cinco regras estão no arquivo `src/uti_triagem.py`. Para o caso de frequência normal e SpO₂ limítrofe, usei peso `0,8` no risco moderado. Sem esse ajuste, o risco para SpO₂ de 95% foi `35,71%`, um pouco acima do limite `<35%` pedido no teste. Com o peso, caiu para `34,08%`. Em 89%, o risco calculado foi `85,57%`.

## Casos testados

| Frequência cardíaca | SpO₂ | Risco | Resultado esperado |
| ---: | ---: | ---: | --- |
| 75 bpm | 98% | 11,67% | Abaixo de 30% |
| 75 bpm | 95% | 34,08% | Abaixo de 35% |
| 75 bpm | 89% | 85,57% | Acima de 65% e maior que em 95% |
| 39 bpm ou 101% de SpO₂ | Fora da faixa | `ValueError` | Rejeitar a entrada |

## Execução dos testes

Na primeira execução, antes de ajustar o peso da regra moderada, dois testes passaram e o teste de transição falhou: para 95% de SpO₂, o resultado foi `35,7067%`. Depois do ajuste, os três testes da triagem passaram.

Também fiz a falha proposital pedida no roteiro, mudando temporariamente o limite de 95% de `<35%` para `<30%`. O resultado foi um teste com falha e dois aprovados; a mensagem mostrou o valor calculado de `34,0758%`. Em seguida, restaurei o limite de `<35%`.

Resultados finais:

- `pytest -v AULA_11/test_uti_triagem.py`: 3 testes aprovados.
- `pytest -s AULA_11/test_uti_triagem.py`: 3 testes aprovados.
- `pytest -v AULA_11`: 10 testes aprovados, incluindo as suítes que já estavam na pasta.
- Cobertura de `src.uti_triagem`: 100% (28 instruções; nenhuma sem cobertura).
- O teste de latência do motor existente mediu 3,633 ms por inferência, abaixo do limite de 10 ms.

O `scikit-fuzzy 0.5.0` mostrou avisos de depreciação internos relacionados ao NumPy, mas eles não impediram os testes de passar.

Para instalar as dependências: `python -m pip install -r AULA_11/requirements.txt`.