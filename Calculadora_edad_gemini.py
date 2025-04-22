import tkinter as tk
from tkinter import ttk  # Para widgets con mejor aspecto (opcional pero recomendado)
from tkinter import messagebox # Para mostrar mensajes de error
import datetime # Para obtener el año actual automáticamente

# --- Función para calcular la edad ---
def calcular_edad():
    """
    Obtiene los años de los campos de entrada, calcula la edad
    y actualiza la etiqueta de resultado.
    Maneja errores si la entrada no es válida.
    """
    try:
        # Obtener los valores de los campos de entrada
        nacimiento_str = entry_nacimiento.get()
        actual_str = entry_actual.get()

        # Validar que no estén vacíos y sean dígitos
        if not nacimiento_str or not actual_str:
            messagebox.showwarning("Entrada incompleta", "Por favor, ingrese ambos años.")
            return
        if not nacimiento_str.isdigit() or not actual_str.isdigit():
             messagebox.showerror("Error de entrada", "Por favor, ingrese solo números para los años.")
             return

        # Convertir a enteros
        anho_nacimiento = int(nacimiento_str)
        anho_actual = int(actual_str)

        # Validar que el año de nacimiento no sea futuro
        if anho_nacimiento > anho_actual:
            messagebox.showerror("Error lógico", "El año de nacimiento no puede ser mayor que el año actual.")
            return

        # Calcular la edad
        edad = anho_actual - anho_nacimiento

        # Actualizar la etiqueta de resultado
        resultado_texto = f'Usted tiene {edad - 1} o {edad} años'
        label_resultado.config(text=resultado_texto)

    except ValueError:
        # Mensaje si la conversión a entero falla (aunque isdigit() debería prevenirlo)
        messagebox.showerror("Error de entrada", "Por favor, ingrese años válidos.")
    except Exception as e:
        # Captura cualquier otro error inesperado
         messagebox.showerror("Error inesperado", f"Ocurrió un error: {e}")

# --- Configuración de la ventana principal ---
root = tk.Tk()
root.title("Calculadora de Edad")
# root.geometry("300x200") # Puedes descomentar y ajustar el tamaño si lo deseas

# --- Crear un marco para organizar los widgets ---
# Usar padding añade espacio alrededor del marco
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S)) # Hace que el marco se expanda con la ventana

# Configurar el sistema de grid para que las columnas se expandan
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1) # Permite que la columna de entradas se expanda

# --- Widgets de la interfaz ---

# Etiqueta y campo para el año de nacimiento
label_nacimiento = ttk.Label(frame, text="Año de Nacimiento:")
label_nacimiento.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5) # Alineado a la izquierda (West)
entry_nacimiento = ttk.Entry(frame, width=10) # Ancho del campo
entry_nacimiento.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=5, pady=5) # Se expande horizontalmente (West, East)
entry_nacimiento.focus() # Pone el cursor en este campo al iniciar

# Etiqueta y campo para el año actual
label_actual = ttk.Label(frame, text="Año Actual:")
label_actual.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
entry_actual = ttk.Entry(frame, width=10)
entry_actual.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)
# Pre-rellenar con el año actual (mejora de usabilidad)
entry_actual.insert(0, str(datetime.date.today().year))

# Botón para calcular
boton_calcular = ttk.Button(frame, text="Calcular Edad", command=calcular_edad)
# columnspan=2 hace que ocupe ambas columnas, pady añade espacio vertical
boton_calcular.grid(column=0, row=2, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = ttk.Label(frame, text="Edad: ")
label_resultado.grid(column=0, row=3, columnspan=2, sticky=tk.W, padx=5, pady=5)

# --- Iniciar el bucle principal de la interfaz ---
root.mainloop()