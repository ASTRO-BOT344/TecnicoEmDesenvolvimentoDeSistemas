#import os
aluno = (input("Digite seu nome completo:"))
ano = int(input("Digite o ano atual: "))
curso = (input("Qual o nome do seu curso?"))
matriculado_input = (input("Esta matriculado? (sim/não) "))

#matriculado = True if matriculado_input.lower() == "sim" else False
#elif= IF/ELSE

if matriculado_input.lower() == "sim":
    matriculado = True
elif matriculado_input.lower() == "não" or matriculado_input.lower() == "nao":
    matriculado = False
else:
    matriculado = False
    print(f"Resposta inválda para matrícula, não matriculado")

if matriculado:
    print(f"{aluno} está matriculado(a) no curso.")
else:
    print(f" {aluno} não está matriculado(a) no curso.")

#os.system("cls" if os.name == "nt" else "clear")

#else/ eli sempre vai ser FALSE e if vai ser TRUE, nesse caso


