#faça uma função que recebe base e altura e retorna a área do triângulo
#área = (base x altura)

def funcao():
    
    b = int(input("Digite a base: "))
    a = int(input("Digite a altura: "))
    area = b * a/2 
    return area
# print(area)
resultado = funcao()
print(f"O resultado é {resultado}")

# ***************************************** agora sem input

def area_triangulo(base, altura):
    area = base * altura/2
    return f'A área do triangulo é de {area} cm'
print(area_triangulo(2,3))