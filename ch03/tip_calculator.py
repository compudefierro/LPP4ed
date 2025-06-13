while True:
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill?>"))
    ppl = int(input("How many people to split the bill?>"))
    tip = int(input("What percentage tip would you like to give?>"))
    percentage_tip = (tip / 100) + 1
    total_tip = total_bill * (tip / 100)
    total_final = total_bill * percentage_tip
    total_each_ppl = total_final / ppl
    print(f"Total bill: {total_bill:.2f}\nTotal ppl: {ppl}\nPercentage tip: %{tip}\nTotal Tip: {total_tip:.2f}\nTotal with bill: {total_final:.2f}\nTotal each ppl: {total_each_ppl:.2f}")
    continuar = True if input("Continuar? (N para salir)>") == "N" else False
    if continuar:
        break
    
