'''
Greedy implementation of finding maximum number from given digits
'''


def max_value(array):
    '''
    Finding maximum number from array
    '''
    maximum = array[0]
    index = 0
    for i in array:
        if i > maximum:
            maximum = i
        index += 1

    return index-1


def find_max_num(limit, numbers):
    '''
    Find the maximum number that can be formed from the given set of numbers
    '''

    solution = 0
    limit -= 1
    while len(numbers) > 0:
        maximum_limit = max_value(numbers)
        print(maximum_limit)
        solution += numbers.pop(maximum_limit)*pow(10, limit)
        limit -= 1
    return solution


if __name__ == '__main__':
    LIMIT = int(input('Enter the number of digits'))
    NUMBERS = [int(input('Enter the digit')) for i in range(LIMIT)]

    print(
        f'The maximum number to be formed with the inputs is {find_max_num(LIMIT, NUMBERS)}')
