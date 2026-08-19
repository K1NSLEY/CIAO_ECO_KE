from pathlib import Path
import sys
import subprocess
import urllib.request
import traceback


# ============================================================
# IDENTIFICAÇÃO DA DUPLA
# ============================================================

ALUNO_1 = "Kinsley Chinda Amadi"
RA_1 = "97399"

ALUNO_2 = "Eduardo Lima"
RA_2 = "105764"


# ============================================================
# CONFIGURAÇÕES
# ============================================================

GITHUB_RAW = (
    "https://raw.githubusercontent.com/"
    "PROFSANTARELLI/CIAO_ECO_2026/main/AULA_03/"
)

PASTA = Path("AULA_03")

ARQUIVOS_ORIGINAIS = [
    "lab01_aula03_CIAO.py",
    "lab02_aula03_CIAO.py",
    "lab03_aula03_CIAO.py",
    "roteiro_aula03_CIAO.txt",
]

ARQUIVOS_ENTREGA = [
    "lab01_aula03.ipynb",
    "lab02_aula03.ipynb",
    "lab03_aula03.ipynb",
    "resultados_aula03.md",
]


# ============================================================
# DEPENDÊNCIAS
# ============================================================

def instalar_dependencia(pacote, modulo=None):
    if modulo is None:
        modulo = pacote

    try:
        __import__(modulo)
    except ImportError:
        print("Instalando " + pacote + "...")
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            pacote
        ])


def preparar_dependencias():
    print("\n[1/8] Verificando dependências...")

    instalar_dependencia("nbformat")
    instalar_dependencia("nbclient")
    instalar_dependencia("ipykernel")
    instalar_dependencia("numpy")
    instalar_dependencia("matplotlib")

    print("\nRegistrando kernel Python...")

    subprocess.check_call([
        sys.executable,
        "-m",
        "ipykernel",
        "install",
        "--user",
        "--name",
        "python3",
        "--display-name",
        "Python 3"
    ])

    print("Kernel Python registrado.")
    print("Dependências OK.")



# ============================================================
# DOWNLOAD
# ============================================================

def baixar_arquivo(nome):
    url = GITHUB_RAW + nome
    destino = PASTA / nome

    print("Baixando " + nome + "...")

    try:
        with urllib.request.urlopen(url, timeout=60) as resposta:
            dados = resposta.read()

        destino.write_bytes(dados)

    except Exception as erro:
        raise RuntimeError(
            "Não foi possível baixar:\n"
            + url
            + "\n\nErro: "
            + str(erro)
        )


def baixar_arquivos():
    print("\n[2/8] Baixando arquivos oficiais...")

    for nome in ARQUIVOS_ORIGINAIS:
        baixar_arquivo(nome)


# ============================================================
# CORREÇÃO DO LAB-03
# ============================================================

def corrigir_lab03():
    print("\n[3/8] Preparando LAB-03...")

    arquivo = PASTA / "lab03_aula03_CIAO.py"

    codigo = arquivo.read_text(encoding="utf-8")

    # --------------------------------------------------------
    # FUNÇÃO bits_para_x
    # --------------------------------------------------------

    inicio = codigo.find("def bits_para_x(")

    if inicio == -1:
        raise RuntimeError(
            "A função bits_para_x não foi encontrada no LAB-03."
        )

    fim = codigo.find("\ndef ", inicio + 5)

    if fim == -1:
        raise RuntimeError(
            "Não foi possível localizar o fim de bits_para_x."
        )

    nova_funcao = '''def bits_para_x(bits):
    """
    Converte uma lista de bits para um valor real
    no intervalo [X_MIN, X_MAX].
    """

    decimal = 0

    for bit in bits:
        decimal = decimal * 2 + bit

    valor_maximo = (2 ** BITS) - 1

    x = X_MIN + (
        decimal / valor_maximo
    ) * (X_MAX - X_MIN)

    return x
'''

    codigo = codigo[:inicio] + nova_funcao + codigo[fim:]


    # --------------------------------------------------------
    # FUNÇÃO fitness
    # --------------------------------------------------------

    inicio = codigo.find("def fitness(")

    if inicio == -1:
        raise RuntimeError(
            "A função fitness não foi encontrada no LAB-03."
        )

    fim = codigo.find("\ndef ", inicio + 5)

    if fim == -1:
        raise RuntimeError(
            "Não foi possível localizar o fim de fitness."
        )

    nova_funcao = '''def fitness(individuo):
    """
    Calcula o fitness de um indivíduo.
    O objetivo é maximizar a função objetivo.
    """

    x = bits_para_x(individuo)

    return funcao_objetivo(x)
'''

    codigo = codigo[:inicio] + nova_funcao + codigo[fim:]


    # --------------------------------------------------------
    # FUNÇÃO mutacao
    # --------------------------------------------------------

    inicio = codigo.find("def mutacao(")

    if inicio == -1:
        raise RuntimeError(
            "A função mutacao não foi encontrada no LAB-03."
        )

    # mutacao normalmente é a última função do arquivo.
    # Portanto podemos substituir até o final.
    nova_funcao = '''def mutacao(individuo):
    """
    Aplica mutação bit-flip.
    Cada bit possui TAXA_MUT de chance
    de ser invertido.
    """

    individuo = individuo.copy()

    for i in range(len(individuo)):
        if random.random() < TAXA_MUT:
            individuo[i] = 1 - individuo[i]

    return individuo
'''

    codigo = codigo[:inicio] + nova_funcao + "\n"


    arquivo.write_text(
        codigo,
        encoding="utf-8"
    )

    print("LAB-03 preparado.")


# ============================================================
# CRIAÇÃO DOS NOTEBOOKS
# ============================================================

def criar_notebook(codigo, numero):
    import nbformat as nbf

    notebook = nbf.v4.new_notebook()

    notebook["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python"
        }
    }

    introducao = (
        "# AULA 03 — AC-1 PARTE 2\n\n"
        "## LAB-" + numero + "\n\n"
        "**Aluno 1:** " + ALUNO_1 + " — RA " + RA_1 + "\n\n"
        "**Aluno 2:** " + ALUNO_2 + " — RA " + RA_2 + "\n\n"
        "---\n\n"
        "Código baseado no material oficial da Aula 03."
    )

    notebook["cells"] = [
        nbf.v4.new_markdown_cell(introducao),
        nbf.v4.new_code_cell(codigo)
    ]

    return notebook


# ============================================================
# EXECUÇÃO
# ============================================================

def executar_notebook(notebook, nome):
    from nbclient import NotebookClient

    print("Executando " + nome + "...")

    cliente = NotebookClient(
        notebook,
        timeout=300,
        kernel_name="python3",
        allow_errors=False
    )

    cliente.execute(
        cwd=str(PASTA.resolve())
    )

    print(nome + " executado com sucesso.")

    return notebook


# ============================================================
# SALVAR NOTEBOOK
# ============================================================

def salvar_notebook(notebook, nome):
    import nbformat

    destino = PASTA / nome

    with open(
        destino,
        "w",
        encoding="utf-8"
    ) as arquivo:
        nbformat.write(
            notebook,
            arquivo
        )


# ============================================================
# EXTRAIR OUTPUTS
# ============================================================

def extrair_output(notebook):
    """
    Obtém os resultados produzidos pelas células Python.
    """

    partes = []

    for celula in notebook.get("cells", []):

        if celula.get("cell_type") != "code":
            continue

        for output in celula.get("outputs", []):

            tipo = output.get("output_type")

            if tipo == "stream":

                texto = output.get("text", "")

                if texto.strip():
                    partes.append(texto.rstrip())

            elif tipo == "execute_result":

                dados = output.get("data", {})

                texto = dados.get(
                    "text/plain",
                    ""
                )

                if texto.strip():
                    partes.append(texto.rstrip())

            elif tipo == "display_data":

                dados = output.get("data", {})

                texto = dados.get(
                    "text/plain",
                    ""
                )

                if texto.strip():
                    partes.append(texto.rstrip())

            elif tipo == "error":

                traceback_texto = "\n".join(
                    output.get("traceback", [])
                )

                partes.append(
                    "ERRO DURANTE A EXECUÇÃO:\n"
                    + traceback_texto
                )

    if not partes:
        return "(Nenhuma saída textual foi produzida.)"

    return "\n\n".join(partes)


# ============================================================
# CONSIDERAÇÕES
# ============================================================

CONSIDERACAO_01 = """
## Considerações da dupla

No LAB-01 analisamos a aplicação de um Algoritmo Genético para
maximizar a função f(x) = x² no intervalo [0,31].

A solução é representada por um cromossomo binário de 5 bits.
O fitness corresponde ao valor da função objetivo, portanto
indivíduos com valores maiores de x possuem maior fitness.

O algoritmo utiliza mecanismos de seleção, crossover, mutação
e elitismo. O elitismo permite preservar o melhor indivíduo
encontrado, enquanto crossover e mutação permitem explorar
novas soluções.

O ótimo global conhecido é x = 31, com f(x) = 961.

Como existem operações aleatórias, diferentes execuções podem
produzir resultados diferentes.
"""


CONSIDERACAO_02 = """
## Considerações da dupla

No LAB-02 analisamos o problema OneMax. O objetivo é maximizar
a quantidade de bits iguais a 1 em um cromossomo.

Nesse problema, o fitness corresponde diretamente ao número
de bits 1. Portanto, para um cromossomo de tamanho 20, o ótimo
global é fitness igual a 20.

Foram observados os mecanismos de seleção por torneio,
crossover, mutação e elitismo.

Os parâmetros utilizados pelo Algoritmo Genético influenciam
seu comportamento. Alterações na população, quantidade de
gerações, taxa de mutação e elitismo podem modificar a
velocidade de convergência e a qualidade das soluções.
"""


CONSIDERACAO_03 = """
## Considerações da dupla

No LAB-03 foram implementadas as funções solicitadas no código
semi-pronto.

A função bits_para_x transforma o cromossomo binário de 8 bits
em um valor real no intervalo [X_MIN, X_MAX].

A função fitness utiliza o valor de x para calcular a função
objetivo, que deve ser maximizada.

A função mutacao implementa a mutação bit-flip. Cada bit possui
uma probabilidade definida por TAXA_MUT de ser invertido.

Depois dessas implementações, o Algoritmo Genético consegue
avaliar os indivíduos, realizar seleção, crossover e mutação,
buscando uma solução com alto valor de fitness.

Devido à natureza aleatória do algoritmo, os valores encontrados
podem variar entre execuções.
"""


# ============================================================
# GERAR RESULTADOS.MD
# ============================================================

def gerar_resultados(output01, output02, output03):

    print("\n[7/8] Gerando resultados_aula03.md...")

    # IMPORTANTE:
    # Não utilizamos f-string aqui.
    # Assim não existe risco de {outputs["01"]}
    # aparecer literalmente no arquivo.

    texto = ""

    texto += "# AULA 03 — AC-1 PARTE 2\n\n"

    texto += "## Identificação da dupla\n\n"

    texto += "| Aluno | RA |\n"
    texto += "|---|---:|\n"
    texto += "| " + ALUNO_1 + " | " + RA_1 + " |\n"
    texto += "| " + ALUNO_2 + " | " + RA_2 + " |\n\n"

    texto += "---\n\n"

    # --------------------------------------------------------
    # LAB 01
    # --------------------------------------------------------

    texto += "# LAB-01 — Compreensão e Execução\n\n"

    texto += "## Output\n\n"

    texto += "```text\n"
    texto += output01
    texto += "\n```\n\n"

    texto += CONSIDERACAO_01
    texto += "\n\n---\n\n"

    # --------------------------------------------------------
    # LAB 02
    # --------------------------------------------------------

    texto += "# LAB-02 — Execução do código pronto\n\n"

    texto += "## Output\n\n"

    texto += "```text\n"
    texto += output02
    texto += "\n```\n\n"

    texto += CONSIDERACAO_02
    texto += "\n\n---\n\n"

    # --------------------------------------------------------
    # LAB 03
    # --------------------------------------------------------

    texto += "# LAB-03 — Execução do código semi-pronto\n\n"

    texto += "## Output\n\n"

    texto += "```text\n"
    texto += output03
    texto += "\n```\n\n"

    texto += CONSIDERACAO_03
    texto += "\n"

    destino = PASTA / "resultados_aula03.md"

    destino.write_text(
        texto,
        encoding="utf-8"
    )

    print("resultados_aula03.md criado.")


# ============================================================
# LIMPEZA
# ============================================================

def limpar_arquivos_originais():

    for nome in ARQUIVOS_ORIGINAIS:

        arquivo = PASTA / nome

        if arquivo.exists():
            arquivo.unlink()


# ============================================================
# VERIFICAÇÃO FINAL
# ============================================================

def verificar_entrega():

    print("\n[8/8] Verificando entrega...")

    faltando = []

    for nome in ARQUIVOS_ENTREGA:

        arquivo = PASTA / nome

        if not arquivo.exists():
            faltando.append(nome)
            continue

        if arquivo.stat().st_size == 0:
            faltando.append(nome)

    print("\n" + "=" * 65)

    if faltando:

        print("ERRO: arquivos ausentes:")

        for nome in faltando:
            print(" - " + nome)

        print("=" * 65)

        return False

    print("ENTREGA GERADA CORRETAMENTE.")
    print()
    print("Arquivos:")

    for nome in ARQUIVOS_ENTREGA:
        print(" - " + nome)

    print("=" * 65)

    return True


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 65)
    print("GERADOR DE ENTREGA — AULA 03")
    print("=" * 65)

    print()
    print(ALUNO_1 + " — RA " + RA_1)
    print(ALUNO_2 + " — RA " + RA_2)
    print()

    try:

        PASTA.mkdir(
            parents=True,
            exist_ok=True
        )

        preparar_dependencias()

        baixar_arquivos()

        corrigir_lab03()

        # ----------------------------------------------------
        # LAB 01
        # ----------------------------------------------------

        print("\n[4/8] Criando LAB-01...")

        codigo01 = (
            PASTA / "lab01_aula03_CIAO.py"
        ).read_text(
            encoding="utf-8"
        )

        notebook01 = criar_notebook(
            codigo01,
            "01"
        )

        notebook01 = executar_notebook(
            notebook01,
            "lab01_aula03.ipynb"
        )

        salvar_notebook(
            notebook01,
            "lab01_aula03.ipynb"
        )

        # ----------------------------------------------------
        # LAB 02
        # ----------------------------------------------------

        print("\n[5/8] Criando LAB-02...")

        codigo02 = (
            PASTA / "lab02_aula03_CIAO.py"
        ).read_text(
            encoding="utf-8"
        )

        notebook02 = criar_notebook(
            codigo02,
            "02"
        )

        notebook02 = executar_notebook(
            notebook02,
            "lab02_aula03.ipynb"
        )

        salvar_notebook(
            notebook02,
            "lab02_aula03.ipynb"
        )

        # ----------------------------------------------------
        # LAB 03
        # ----------------------------------------------------

        print("\n[6/8] Criando LAB-03...")

        codigo03 = (
            PASTA / "lab03_aula03_CIAO.py"
        ).read_text(
            encoding="utf-8"
        )

        notebook03 = criar_notebook(
            codigo03,
            "03"
        )

        notebook03 = executar_notebook(
            notebook03,
            "lab03_aula03.ipynb"
        )

        salvar_notebook(
            notebook03,
            "lab03_aula03.ipynb"
        )

        # ----------------------------------------------------
        # OUTPUTS
        # ----------------------------------------------------

        output01 = extrair_output(notebook01)
        output02 = extrair_output(notebook02)
        output03 = extrair_output(notebook03)

        gerar_resultados(
            output01,
            output02,
            output03
        )

        limpar_arquivos_originais()

        if not verificar_entrega():
            sys.exit(1)

        print()
        print("Pasta final:")
        print(PASTA.resolve())

        print()
        print("Agora você pode enviar a pasta AULA_03")
        print("para o seu repositório do trabalho.")

    except Exception as erro:

        print("\n" + "=" * 65)
        print("O GERADOR PAROU POR CAUSA DE UM ERRO")
        print("=" * 65)

        print()
        print(str(erro))
        print()

        traceback.print_exc()

        print()
        print(
            "Os arquivos temporários foram mantidos "
            "na pasta AULA_03 para facilitar a análise."
        )

        sys.exit(1)


if __name__ == "__main__":
    main()
