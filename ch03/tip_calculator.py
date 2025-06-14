import tkinter as tk

# Función que toma el texto del Entry y lo muestra en la etiqueta
def calcular():
    total_bill = total_bill_e.get()
    ppl = ppl_e.get()
    tip = tip_e.get()
    
    total_bill = float(total_bill)
    ppl = int(ppl)
    tip = int(tip)
    
    percentage_tip = (tip / 100) + 1
    total_tip = total_bill * (tip / 100)
    total_final = total_bill * percentage_tip
    total_each_ppl = total_final / ppl
    
    
    etiqueta.config(text=f"Total bill: {total_bill:.2f}\nTotal ppl: {ppl}\nPercentage tip: %{tip}\nTotal Tip: {total_tip:.2f}\nTotal with bill: {total_final:.2f}\nTotal each ppl: {total_each_ppl:.2f}")

ventana = tk.Tk()
ventana.title("Entrada de texto")
ventana.geometry("600x600")

# Campo de total_bill
total_bill_e = tk.Entry(ventana)
total_bill_e.pack(pady=10)
total_bill_e.insert(0, "124")

# Campo de total_bill
ppl_e = tk.Entry(ventana)
ppl_e.pack(pady=10)
ppl_e.insert(0, "5")

# Campo de total_bill
tip_e = tk.Entry(ventana)
tip_e.pack(pady=10)
tip_e.insert(0, "12")

# Botón que toma el texto del Entry
boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack(pady=5)

# Etiqueta donde se muestra el texto
etiqueta = tk.Label(ventana, text="clic Calcular...")
etiqueta.pack(pady=10)

ventana.mainloop()


# print("Welcome to the tip calculator.")
# total_bill = float(input("What was the total bill?>"))
# ppl = int(input("How many people to split the bill?>"))
# tip = int(input("What percentage tip would you like to give?>"))
# percentage_tip = (tip / 100) + 1
# total_tip = total_bill * (tip / 100)
# total_final = total_bill * percentage_tip
# total_each_ppl = total_final / ppl
# print(f"Total bill: {total_bill:.2f}\nTotal ppl: {ppl}\nPercentage tip: %{tip}\nTotal Tip: {total_tip:.2f}\nTotal with bill: {total_final:.2f}\nTotal each ppl: {total_each_ppl:.2f}")
