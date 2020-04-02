'''
Implement Different output techniques in python
'''


def output_test():
    ''' Function to practice different techniques to print out data in python '''
    # General printing of array elements on the same line
    result = [1, 2, 3, 4]
    print(*result, end=' ')
    # Insted of using *result a loop can also be used
    print()
    # Printing multiple outputs using some text before it
    for i in range(len(result)):
        print("Case #{}: {}".format(i+1, result[i]))

    string_array = ['This', 'Is', 'An', 'Array']
    # printing an array as string using join
    print('It has indexes because {}'.format(' '.join(string_array)))


output_test()
