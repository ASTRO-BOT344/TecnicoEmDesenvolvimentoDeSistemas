homens_18 = 0
mulheres = 0
outros = 0
sexo = 0
while True:
    # n = input("Digite o nome: ").strip().upper()
    s = input("Digite o sexo (M/F/Outro): ").strip().upper()
    i = input("Digite o idade: ").strip().upper()


    if i < 0:
        print("O programa será encerrado.")
        break

match sexo:
    case "M": 
        if s > 18:
            homens_18 += 1
    case "F":
        mulheres += 1
    case "Outro":
        outros += 1
    case _:
        print("Gênero inválido. Digite ")

print(f"Quantidade de homens acima de 18: {homens_18} ")
print(f"Quantidade de mulheres de qualquer idade: {mulheres} ")
print(f"Quantidade de alunos com outro genêro: {outros}")
