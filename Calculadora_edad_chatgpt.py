import tkinter as tk
from tkinter import messagebox

def calcular_edad():
    try:
        anho_nacimiento = int(entry_nacimiento.get())
        anho_actual = int(entry_actual.get())
        edad = anho_actual - anho_nacimiento
        resultado = f'Usted tiene {edad - 1} o {edad} años'
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("300x200")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Año de nacimiento:").pack(pady=5)
entry_nacimiento = tk.Entry(ventana)
entry_nacimiento.pack()

tk.Label(ventana, text="Año actual:").pack(pady=5)
entry_actual = tk.Entry(ventana)
entry_actual.pack()

# Botón de cálculo
tk.Button(ventana, text="Calcular Edad", command=calcular_edad).pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
