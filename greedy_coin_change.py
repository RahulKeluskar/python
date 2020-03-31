'''
Implement greedy algorithm for change problem with cashier having 1 , 2 and 10 valued denominations and we must calculate the least number of coins that are required for it
'''


def check_denomination(remainder, denominations):
    '''Accepts array of the available denominations and the remainder of the money'''

    for coin in denominations:
        if remainder - coin >= 0:
            return (coin)


def find_coins_number(total):
    '''Accepts the total number to be divided into denominations as the input and returns the counter value '''
    counter = [0, []]
    denominations = [10, 2, 1]
    while total > 0:
        denomination = check_denomination(total, denominations)
        total -= denomination
        counter[0] += 1
        counter[1].append(denomination)

    return counter


if __name__ == '__main__':
    TOTAL = int(input('Enter the amount:'))
    print(find_coins_number(TOTAL))
