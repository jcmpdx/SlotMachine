MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter deposit: $")
        # ifdigit() tests is >= 0
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit must be greater than 0")
        else:
            print("Please enter a whole number")

    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a whole number")

    return lines

def get_bet():
    while True:
        amount = input("Enter bet: $")
        # ifdigit() tests is >= 0
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a whole number")

    return amount


def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

main()