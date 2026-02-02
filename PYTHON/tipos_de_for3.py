frutas = ['maça', 'banana', 'laranja']
for fruta in frutas:
    if fruta == 'banana':
        break
    print(fruta)

#interar sobre strings
mensagem = "óla"
for caractere in mensagem:
    print(caractere)

#enumerate
for indice, fruta in enumerate(frutas):
    print(f"índice {indice}: {fruta} ")