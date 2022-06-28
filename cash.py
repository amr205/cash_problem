coins = [25, 10, 5, 1]

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