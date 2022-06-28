coins = [25, 10, 5, 1]

def main():
    # ask for user input until valid
    input = input("Change owed: ")
    while not is_positive_number(input):
        input = input("Change owed: ")

    #calculate and print
    minimum_number_of_coins = calculate_minimum_coins(float(input))
    print(minimum_number_of_coins)

def is_positive_number(input: str) -> bool:
    if input == 'Nan':
        return False
    try:
        float(input)
        if float(input) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def calculate_minimum_coins(amount_in_dollars: float) -> int:
    amount_in_cents = int(amount_in_dollars * 100)
    number_of_coins = 0

    # Given the possible type of coins, a greedy approach will give the best result
    while amount_in_cents > 0:
        possible_coins = [coin for coin in coins if coin <= amount_in_cents]
        max_possible_coin = max(possible_coins)
        amount_in_cents -= max_possible_coin
        number_of_coins += 1

    return number_of_coins


if __name__ == "__main__":
    main()