import os
import sys
import tkinter as tk
from tkinter import messagebox
import re

def leer_conjunto_manual(entrada):
    """Convierte una entrada de texto en un conjunto, validando los elementos."""
    elementos = entrada.strip().split("\n")
    conjunto = set()
    for elem in elementos:
        elem = elem.strip()
        if re.match(r'^[a-zA-Z0-9]+$', elem) and len(conjunto) < 10:
            conjunto.add(elem)
    return conjunto

def evaluar_expresion(expresion, conjuntos):
    """Evalúa una expresión de conjuntos con operadores y paréntesis."""
    try:
        for nombre, conjunto in conjuntos.items():
            expresion = expresion.replace(nombre, str(conjunto))
        return eval(expresion, {"__builtins__": None}, {"|": set.union, "&": set.intersection, "-": set.difference, "^": set.symmetric_difference})
    except Exception as e:
        messagebox.showerror("Error", f"Expresión inválida: {e}")
        return None

def calcular():
    """Realiza la operación seleccionada y muestra el resultado."""
    conjuntos = {
        "A": leer_conjunto_manual(text_conjunto1.get("1.0", tk.END)),
        "B": leer_conjunto_manual(text_conjunto2.get("1.0", tk.END)),
        "C": leer_conjunto_manual(text_conjunto3.get("1.0", tk.END)),
        "U": leer_conjunto_manual(text_conjunto4.get("1.0", tk.END))
    }
    
    # Mostrar los conjuntos ingresados
    conjuntos_label.config(text=f"A = {conjuntos['A']}\nB = {conjuntos['B']}\nC = {conjuntos['C']}\nU = {conjuntos['U']}")
    
    expresion = entry_expresion.get()
    resultado = evaluar_expresion(expresion, conjuntos)
    resultado_label.config(text=f"RESULTADO: {resultado}")

# Verificar compatibilidad con Windows para evitar errores al generar ejecutable
if sys.platform.startswith("win"):  
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except AttributeError:
        pass  # Evitar errores en sistemas sin esta función

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Conjuntos")
root.geometry("600x700")

# Variables
tk.Label(root, text="Ingrese el conjunto A (máx 10 elementos, uno por línea):").pack()
text_conjunto1 = tk.Text(root, width=30, height=5)
text_conjunto1.pack()

tk.Label(root, text="Ingrese el conjunto B (máx 10 elementos, uno por línea):").pack()
text_conjunto2 = tk.Text(root, width=30, height=5)
text_conjunto2.pack()

tk.Label(root, text="Ingrese el conjunto C (máx 10 elementos, uno por línea):").pack()
text_conjunto3 = tk.Text(root, width=30, height=5)
text_conjunto3.pack()

tk.Label(root, text="Ingrese el conjunto U (máx 10 elementos, uno por línea):").pack()
text_conjunto4 = tk.Text(root, width=30, height=5)
text_conjunto4.pack()

tk.Label(root, text="Ingrese la operación (usando A, B, C, U y operadores |, &, -, ^, con paréntesis):").pack()
entry_expresion = tk.Entry(root, width=50)
entry_expresion.pack()

tk.Button(root, text="Calcular", command=calcular).pack()

conjuntos_label = tk.Label(root, text="Conjuntos definidos:")
conjuntos_label.pack()

resultado_label = tk.Label(root, text="RESULTADO:")
resultado_label.pack()

# Ejecutar la aplicación
root.mainloop()