# match.py
import random

while True:
    day_number = random.randint(0,8)
    match day_number:
        case 1 | 2 | 3 | 4 | 5:
            print("Weekday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print(f"{day_number} is not a valid day number")
    continuar = True if input("continuar?") == "1" else False
    if continuar:
        break