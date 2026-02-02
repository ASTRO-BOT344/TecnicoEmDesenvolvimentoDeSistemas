#criar funcao
def crescente():     
    numero = [2,6,3,7,8]
    print(f"A lista original é essa: {numero}")
    organizado = sorted(numero)
    print(f"A lista organizada é essa {organizado}")
    return organizado

crescente()

