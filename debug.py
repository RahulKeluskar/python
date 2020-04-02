'''
Implementing Python debugger pdb for efficient debugging of code and analyzing stack traces to improve efficiency
'''


def test_function():
    ''' Function with miscellaneous functionality to test the debugging techniques in python '''
    var = int(input('Enter a value: '))
    import pdb
    pdb.set_trace()
    print(var)


test_function()
