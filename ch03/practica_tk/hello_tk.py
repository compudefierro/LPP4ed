import tkinter as tk

def cambiarTitulo():
    root.title("otro titulo")

root = tk.Tk()
root.title("Ejemplo sin ttk")

# Botón clásico de tkinter
boton = tk.Button(root, text="Hola mundo",command=cambiarTitulo).pack()


root.mainloop()