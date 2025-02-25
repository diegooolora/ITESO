import tkinter as tk
from tkinter import messagebox
from itertools import product

# Genera la tabla de verdad para la expresión dada y las variables
def generar_tabla_de_verdad(expresion, variables):
    tabla = []
    combinaciones = list(product([False, True], repeat=len(variables)))

    for valores in combinaciones:
        contexto = dict(zip(variables, valores))
        try:
            resultado = eval(expresion, contexto)
        except Exception:
            resultado = "Error"
        tabla.append(list(valores) + [resultado])

    return tabla

# Evaluador de expresiones lógicas
def evaluar_expresion(expresion):
    try:
        variables = sorted(set(filter(str.isalpha, expresion)))
        expresion = expresion.replace("¬", "not ").replace("∧", " and ").replace("∨", " or ")
        expresion = expresion.replace("→", " <= ").replace("↔", " == ")
        tabla = generar_tabla_de_verdad(expresion, variables)
        return tabla
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")
        return []

# Manejo de la entrada
def agregar_caracter(caracter):
    entrada_var.set(entrada_var.get() + caracter)

def borrar():
    entrada_var.set("")

def borrar_ultimo():
    entrada_var.set(entrada_var.get()[:-1])

def calcular():
    resultado = evaluar_expresion(entrada_var.get())
    mostrar_tabla(resultado)

# Muestra la tabla de verdad en un cuadro de diálogo
def mostrar_tabla(tabla):
    if not tabla:
        return

    variables = sorted(set(filter(str.isalpha, entrada_var.get())))
    encabezado = " | ".join(variables + ["Resultado"])
    separador = "-" * len(encabezado)

    mensaje = [encabezado, separador]
    for fila in tabla:
        mensaje.append(" | ".join(map(str, fila)))

    messagebox.showinfo("Tabla de Verdad", "\n".join(mensaje))

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora Lógica")
root.configure(bg="#7E8C8D")

entrada_var = tk.StringVar()

entrada = tk.Entry(root, textvariable=entrada_var, font=("Arial", 18), width=20, bd=5, bg="#A3A944")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

