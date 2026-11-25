import periodictable

def distribuicao_pauling(z):
    elemento = periodictable.elements[z]
    eletrons = z

    subniveis = [
        ("1s", 2),
        ("2s", 2), ("2p", 6),
        ("3s", 2), ("3p", 6),
        ("4s", 2), ("3d", 10), ("4p", 6),
        ("5s", 2), ("4d", 10), ("5p", 6),
        ("6s", 2), ("4f", 14), ("5d", 10), ("6p", 6),
        ("7s", 2), ("5f", 14), ("6d", 10), ("7p", 6)
    ]

    distribuicao = []

    for subnivel, capacidade in subniveis:
        if eletrons <= 0:
            break

        qtd = min(eletrons, capacidade)

        expoentes = {
            "1": "¹", "2": "²", "3": "³",
            "4": "⁴", "5": "⁵", "6": "⁶",
            "7": "⁷", "8": "⁸", "9": "⁹",
            "10": "¹⁰", "11": "¹¹", "12": "¹²",
            "13": "¹³", "14": "¹⁴"
        }

        distribuicao.append(f"{subnivel}{expoentes[str(qtd)]}")
        eletrons -= qtd

    return elemento, " ".join(distribuicao)

print("=== Calculadora do Diagrama de Pauling ===")
print("Digite 0 a qualquer momento para encerrar.\n")

while True:
    entrada = input("Digite o número atômico (1 a 118): ")

    try:
        z = int(entrada)

        if z == 0:
            print("\nPrograma encerrado!")
            break

        if z < 1 or z > 118:
            print("Aviso: Digite um número entre 1 e 118.\n")
            continue

        elemento, resultado = distribuicao_pauling(z)

        print(f"\n-> Elemento: {elemento.name.capitalize()} ({elemento.symbol})")
        print(f"-> Distribuição: {resultado}\n")
        print("-" * 45)

    except ValueError:
        print("Erro: Digite apenas números inteiros.\n")
