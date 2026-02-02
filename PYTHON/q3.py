def dia_da_semana(numero):
    match numero:
        case 1:
            print("Segunda")
        case 2:
            print("Terça")
        case 3:
            print("Quarta")
        case 4:
            print("Quinta")
        case 5:
            print("Sexta")
        case 6:
            print("Sábado")
        case 7:
            print("Domingo")
        case _:
            print(f"Dia inválido")

dia_da_semana()