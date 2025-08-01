from agronomia import Agronomia

'''frutas: Manga	5,50	40.000
Maracujá	4,50	12.700
Mamão	1,00	60.000
Abacaxi	2,00	36.000
Acerola	3,00	40.000'''

print("\n ---PRODUÇÃO DE FRUTAS---")
hectare = int(input("Digite a quantidade de hectares: "))

print("\n SELECIONE A FRUTA DESEJADA: \n 1 - MANGA\n2 - MAMÃO\n 3 - ABACAXI\n 4 - MARACUJÁ\n 5 - ACEROLA\n ")

opcao = input("Digite a opção da fruta desejada: ")

match opcao:
    case "1":
        try:
            nome, preco_kg, produtividade = "Manga", 5.50, 40000

        except ValueError:
            print("Você digitou um numero indisponivel!")

    case "2":
        try:
            nome, preco_kg, produtividade = "Mamão", 1, 60000

        except ValueError:
            print("Você digitou um numero indisponivel!")

    case "3":
        try:
            nome, preco_kg, produtividade = "Abacaxi", 2, 36000

        except ValueError:
            print("Você digitou um numero indisponivel!")

    case "4":
        try:
            nome, preco_kg, produtividade = "Maracujá", 4.50, 12700

        except ValueError:
            print("Você digitou um numero indisponivel!")

    case "5":
        try:
            nome, preco_kg, produtividade = "Acerola", 3, 40000

        except ValueError:
            print("Você digitou um numero indisponivel")

resultado = Agronomia(nome, preco_kg, produtividade, hectare)
resultado.mostrar_produtividade(nome)
