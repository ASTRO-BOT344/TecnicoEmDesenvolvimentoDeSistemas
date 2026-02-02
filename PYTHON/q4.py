def converter_notas(notas):
    conceitos = []
    for nota in notas:
        match nota:
            case n if 9 <= n <= 10:
                conceitos.append("A")
            case n if 7 <= n <= 8:
                conceitos.append("B")
            case n if 5 <= n <= 6:
                conceitos.append("C")
            case n if 0 <= n <= 4:
                conceitos.append("D")
            case _:
                conceitos.append("Inválido")
    return conceitos