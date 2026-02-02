from tkinter import * 

expressao = "" #guarda cadeia de caracteres "12+5*3"

def pressionar(tecla):
    global expressao
    expressao += str(tecla)
    visor.set(expressao)#atualizar o visor

def calcular():
    global expressao
    try:
        resultado = str(eval(expressao)) #eval = interpreta string como expresão python e faz o cálculo
        visor.set(resultado)
        expresao = ""
    except:
        visor.set("Erro")
        expressao = ""

    def limpar():
        global expressao
        expressao = ""
        visor.set("")

if __name__ == "__main__":
    root = Tk()
    root.tittle("Calculadora Simples")
    root.geometry("320x280")
    root.configure(bg="#d0f0c0")
    root.realizable(False, False)

    visor = StringVar()
    entrada = Entry(root, textvariable=visor, font=("Helvtica", 20), bd= 5,
                    relief=SUNKEN, justify='right'
                    
                    )
