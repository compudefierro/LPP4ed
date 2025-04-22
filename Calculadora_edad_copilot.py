import tkinter as tk
from tkinter import messagebox

def calcular_edad():
    # Se obtienen los valores de los campos de entrada
    anho_nacimiento = entry_anho_nacimiento.get()
    anho_actual = entry_anho_actual.get()
    try:
        # Se realiza la operación: la edad puede ser (edad-1) o (edad)
        edad = int(anho_actual) - int(anho_nacimiento)
        resultado = f'Usted tiene {edad - 1} o {edad} años'
        label_resultado.config(text=resultado)
    except ValueError:
        # Se muestra un mensaje de error en caso de que los datos no sean numéricos
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Se crea la ventana principal
root = tk.Tk()
root.title("Calculadora de Edad")

# Se configura un frame para organizar los elementos
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Título de la herramienta
label_titulo = tk.Label(frame, text="Calculadora de Edad", font=("Arial", 16))
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Etiqueta y campo de entrada para el año de nacimiento
label_anho_nacimiento = tk.Label(frame, text="Año de Nacimiento:")
label_anho_nacimiento.grid(row=1, column=0, sticky="e")
entry_anho_nacimiento = tk.Entry(frame)
entry_anho_nacimiento.grid(row=1, column=1)

# Etiqueta y campo de entrada para el año actual
label_anho_actual = tk.Label(frame, text="Año Actual:")
label_anho_actual.grid(row=2, column=0, sticky="e")
entry_anho_actual = tk.Entry(frame)
entry_anho_actual.grid(row=2, column=1)

# Botón para calcular la edad
btn_calcular = tk.Button(frame, text="Calcular", command=calcular_edad)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=5)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(frame, text="", font=("Arial", 12))
label_resultado.grid(row=4, column=0, columnspan=2)

# Se inicia el bucle principal de la aplicación
root.mainloop()
