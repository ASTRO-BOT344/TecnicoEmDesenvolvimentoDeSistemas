# def nome_da_funcao(parametro1,parametro2):
    # copro da nome_da_funcao
    # codigo que sera executado
    # return valor

#parametros padrao
# quando um argumento nao é fornecido(quando é generico)

def saudacao(nome, mensagem="Olá"):
    return f"{mensagem}, {nome}!"

print(saudacao("Maria"))

print(saudacao("João", "Oi"))