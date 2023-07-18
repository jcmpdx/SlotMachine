
def deposit():
    while True:
        amount = input("Enter deposit: $")
        # ifdigit() tests is >= 0
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"${amount} was entered.")
                break
            else:
                print("Deposit must be greater than 0")
        else:
            print("Please enter a whole number")

    return amount

def main():
    balance = deposit()

main()