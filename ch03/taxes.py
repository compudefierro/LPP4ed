# taxes.py

# Agregar input del usuario para poder poner el valor manualmente.
income = int(input("Brute income>"))
if income < 15000:
    tax_coefficient = 0.0 # 1
elif income < 30000:
    tax_coefficient = 0.2 # 2
elif income < 100000:
    tax_coefficient = 0.35 # 3
else:
    tax_coefficient = 0.45 # 4

# Ternary operator:
tax_coefficient = 0.5 if income > 30000 else 0 

def format_currency_string(income, tax_coefficient):
    tax_result = income * tax_coefficient
    result = f"You will pay: ${tax_result:,.2f} in taxes (coefficient: {tax_coefficient:,.2f}) for total income of ${income:,.2f}"
    return result.replace(",", "X").replace(".", ",").replace("X", ".")

# Mostrar resultado formateado
print(format_currency_string(income, tax_coefficient))

# tax_result = income * tax_coefficient
# 
# # Se agrega formato con coma decimal y se reemplaza el separador de miles , por .
# print(f"You will pay: ${tax_result:,.2f} in taxes (coefficient: {tax_coefficient:,.2f}) for total income of ${income:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))