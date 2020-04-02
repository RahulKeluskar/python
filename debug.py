'''
Implementing Python debugger pdb for efficient debugging of code and analyzing stack traces to improve efficiency
'''


import os


def test_function():
    ''' Function with miscellaneous functionality to test the debugging techniques in python '''
    var = int(input('Enter a value: '))
    import pdb
    pdb.set_trace()
    print(var)


def test_function_2():
    ''' Function to test debugging using breakpoint() function that is inbuilt in python from version 3.7 onwards '''
    var = int(input('Enter the value : '))
    breakpoint()
    print(var)


def get_path(filename):
    ''' Returns file path or no string if no path '''
    head, tail = os.path.split(filename)
    import pdb
    pdb.set_trace()
    return head


def get_file_name():
    ''' Using file name argument and analyzing flow of the debugger '''
    filename = __file__
    import pdb
    pdb.set_trace()
    print(f'path = {get_path(filename)}')


if __name__ == '__main__':
    # test_function()
   # test_function_2()
    get_file_name()
