


def main():
    print("Welcome to the tip calculator.")
    total = float(input("What was the total bill?\n$"))
    peoples = int(input("How many people to split the bill?\n"))
    porcentage = int(input("What porcentage tip would you like to give? 10, 12, or 15?\n"))
    if porcentage in [10,12,15]:
        calculater_tip = total*(porcentage/100)
        calculater_total = total + calculater_tip
        calculater = calculater_total/peoples
        print(f"Each person should pay: ${calculater:.1f}")
    else:
        print("Porcentage invalid.")
main()