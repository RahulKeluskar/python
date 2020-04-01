'''
Recursive Implementation of Tower of Hanoi
'''


def move(initial, to):
    ''' Function to move from postion to destination '''
    print(f'Move from {initial} to {to} !')


def move_via(initial, auxilarry, destination):
    ''' Function to move fron initial to destination via auxilarry '''
    move(initial, auxilarry)
    move(auxilarry, destination)


def hanoi(number_discs, initial, auxilarry, destination):
    ''' Function to shift number of discs from inital to destination via the auxilarry using recersion '''
    if number_discs == 0:
        pass
    else:
        hanoi(number_discs-1, initial, destination, auxilarry)
        move(initial, destination)
        hanoi(number_discs-1, auxilarry, initial, destination)


if __name__ == '__main__':
    DISCS = int(input('Enter the number of discs'))
    hanoi(DISCS, 'A', 'B', 'C')
