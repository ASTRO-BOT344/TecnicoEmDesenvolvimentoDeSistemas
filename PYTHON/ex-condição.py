#import os
dia = input("Digite o dia da semana: ").strip().lower()

if dia.lower() == "sabado" or dia.lower() == "sábado" or dia.lower() == "domingo":
    print("O dia é fim de semana")
elif dia.lower() == "segunda" or dia.lower() == "segunda-feira":
    print(f"inicio da semana")
else:
    print(f"O dia é utíl")
#os.system("cls" if os.name == "nt" else "clear")