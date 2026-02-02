# as variáveis tem diferentes escopos (visibilidade)

x = 10
#variável global
def funcao():
    #variavel local
    y = 5
    print(f" Dentro da função - x {x}, y: {y}")
    return y

y = funcao( )

funcao() #Saída; Dentro da função - x: 10, y:5
# A variável y não etsá disponível
print(f"Fora da função - x: {x}")
print(f"y: {y}")

#Erro: nome y não está definido
