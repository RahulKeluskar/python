'''
Different greedy implementation of the coins problem
'''


def get_coin_number(denominations, value):
    '''
    Using modulus implementation of the coins problem'''
    import math
    quotient = value
    no_of_coins = 0
    for i in denominations:
        if value <= 0:
            break
        quotient = math.floor(value/i)
        value = value % i
        no_of_coins += quotient
        print(f'{quotient} of Denomination {i}')
    return no_of_coins


if __name__ == '__main__':
    INPUT = int(input('Enter the total amount to be split'))
    # Taking predefined denominations
    print(get_coin_number([10, 2, 1], INPUT))
