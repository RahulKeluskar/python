'''
Different Ways of accepting input in python
'''


def input_testing():
    ''' Practicing the different input methods in python to minimise time spent in accepting inputs and using advanced python techniques '''

    # Normal input
    var = input('Enter a normal input')
    print(var)
    var = int(input('Parsing this input as soon as it is accepted'))
    print(var)
    # Taking a fixed number of space separated units like in matrix dimensions
    row, column = input('Enter the row and column').split()
    print(f'Row:{row} , Column:{column}')
    # This works as the input returns a space separated string
    # Accepting row and column as integers
    row, column = map(int, input(
        'Enter the row and column an itll be parsed as integers:').split())
    print(f'Row:{row} , Column:{column}')
    # To accept multiple variables but not waste space for one of them
    row, _, column = map(int, input('Enter 3 space separated inputs').split())
    print(f'Row:{row} , Column:{column}')
    # How to inialise a dynamic list without asking for the limit first
    var = list(
        map(int, input('Enter the values in array separated by space').trim().split()))
    print(var)
    # How to take one constant and other variable number of inputs in python like the number to be found and then the rest of array
    constant, * \
        l = input('Enter one constant and then array elements to follow:').split()

    l = list(map(int, l))
    print(f'The constant value is {constant} and the list is {l}')


input_testing()
