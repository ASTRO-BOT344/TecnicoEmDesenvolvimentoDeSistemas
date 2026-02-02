#import os

idade = int(input("Digite um numero: "))

if idade < 13:
    print("A pessoa é Criança")
elif idade < 20:
    print("A pessoa é Adolescente")
elif idade < 60:
    print("A pessoa é Adulta")
else:
    print("Idoso")


#os.system("cls" if os.name == "nt" else "clear")