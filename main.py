import tkinter as tk
from tkinter import messagebox

from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir

def calcular(operacion):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operacion == "suma":
            resultado = sumar(a, b)
        elif operacion == "resta":
            resultado = restar(a, b)
        elif operacion == "multiplicacion":
            resultado = multiplicar(a, b)
        elif operacion == "division":
            resultado = dividir(a, b)
        else:
            resultado = "Operación no válida"

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

# Interfaz
ventana = tk.Tk()
ventana.title("Calculadora - FullStack")
ventana.geometry("300x300")

tk.Label(ventana, text="Primer número:").pack()
entry1 = tk.Entry(ventana)
entry1.pack()

tk.Label(ventana, text="Segundo número:").pack()
entry2 = tk.Entry(ventana)
entry2.pack()

tk.Button(ventana, text="Sumar", command=lambda: calcular("suma")).pack(pady=5)
tk.Button(ventana, text="Restar", command=lambda: calcular("resta")).pack(pady=5)
tk.Button(ventana, text="Multiplicar", command=lambda: calcular("multiplicacion")).pack(pady=5)
tk.Button(ventana, text="Dividir", command=lambda: calcular("division")).pack(pady=5)

label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack(pady=10)

ventana.mainloop()
