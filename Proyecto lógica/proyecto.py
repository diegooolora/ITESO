import tkinter as tk
from tkinter import messagebox

# Evaluador de expresiones lógicas
def evaluar_expresion(expresion):
    try:
        expresion = expresion.replace("¬", "not ").replace("∧", " and ").replace("∨", " or ")
        expresion = expresion.replace("→", " <= ").replace("↔", " == ")
        resultado = eval(expresion, {"p": True, "q": True, "r": True, "s": True})
        return resultado
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")
        return ""

# Manejo de la entrada
def agregar_caracter(caracter):
    entrada_var.set(entrada_var.get() + caracter)

def borrar():
    entrada_var.set("")

def borrar_ultimo():
    entrada_var.set(entrada_var.get()[:-1])

def calcular():
    resultado = evaluar_expresion(entrada_var.get())
    entrada_var.set(str(resultado))

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora Lógica")
root.configure(bg="#7E8C8D")

entrada_var = tk.StringVar()

entrada = tk.Entry(root, textvariable=entrada_var, font=("Arial", 18), width=20, bd=5, bg="#A3A944")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    ("AC", borrar), ("DEL", borrar_ultimo), ("(", lambda: agregar_caracter("(")), (")", lambda: agregar_caracter(")")),
    ("¬", lambda: agregar_caracter("¬")), ("∧", lambda: agregar_caracter("∧")), ("∨", lambda: agregar_caracter("∨")), ("→", lambda: agregar_caracter("→")),
    ("p", lambda: agregar_caracter("p")), ("q", lambda: agregar_caracter("q")), ("↔", lambda: agregar_caracter("↔")), ("⊕", lambda: agregar_caracter("⊕")),
    ("r", lambda: agregar_caracter("r")), ("s", lambda: agregar_caracter("s")), ("=", calcular)
]

fila, columna = 1, 0
for texto, comando in botones:
    tk.Button(root, text=texto, width=6, height=2, font=("Arial", 14), command=comando, bg="#333", fg="white").grid(row=fila, column=columna, padx=5, pady=5)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

root.mainloop()

