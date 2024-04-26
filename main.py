import tkinter as tk
from datetime import datetime
import winsound

def salvar_historico(operacao, num1, num2, resultado):
    with open("historico_calculadora.txt", "a") as file:
        file.write(f"{datetime.now()} - {operacao} - {num1} e {num2} = {resultado}\n")


def beep():
    winsound.Beep(1000, 1000)

def realizar_operacao():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    operacao = operacao_var.get()
    resultado = 0

    if operacao == 'add':
        resultado = num1 + num2
    elif operacao == 'subtract':
        resultado = num1 - num2
    elif operacao == 'multiply':
        resultado = num1 * num2
    elif operacao == 'divide':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Não pode dividir por zero"


    label_resultado.config(text=f"Resultado: {resultado}")
    if isinstance(resultado, (int,float)):
        salvar_historico(operacao, num1, num2, resultado)
        beep()

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Criação dos widgets
entry_num1 = tk.Entry(root, width=10)
entry_num2 = tk.Entry(root, width=10)
entry_num1.pack(pady=10)
entry_num2.pack(pady=10)

operacao_var = tk.StringVar(root)
operacao_var.set("add") # o valor padrão

tk.OptionMenu(root, operacao_var, "add", "subtract", "multiply", "divide").pack()

button_calcular = tk.Button(root, text="Calcular", command=realizar_operacao)
button_calcular.pack(pady=20)

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.pack(pady=10)

# Execução do loop principal da interface
root.mainloop()
