'''
Implementing various usages of lambda function in python
'''


def some_decorator(f):
    def wraps(*args):
        print(f'Calling function is {f.__name__}')
        return f(args)
    return wraps


@some_decorator
def decorated_function(argument):
    print(f'With argument {argument}')


def trace(f):
    ''' Function decorator '''
    def wrap(*args, **kwargs):
        print(f'[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}')
        return f(*args, *kwargs)
    return wrap


@trace
def add_two(x):
    return x+2


def main():
    ''' Main function for implementing lambda functions in various scenarios '''
    # Adding 2 numbers using lambda function
    def addition(x, y): return x+y
    print(addition(2, 12))

    # Immediately invoked python expression
    print((lambda x, y: x+y)(10, 15))

    # Lamda function can be used as a higher order function to accept a function along with another parameter
    def higher_order_func(x, func): return x + func(x)
    print(higher_order_func(2, lambda x: x*x))
    # The higher order function can take lamda or general function as a parameter
    def square(x): return x*x
    print(higher_order_func(2, square))

    # Higher order functions are used in lamda to maximise efficiency. These functions are exposed by python in the standard library and are builtin
    # The examples include map(), filter(), functools.reduce(), sort(), sorted(), min() and max()

    # Using the dis module in python to analyse the bytecode genrated while intepreting a lambda function
    import dis
    def add(x, func): return x+func(x)
    type(add)
    dis.dis(add)

    # using lamda function with map function to define the function to map the second paramter to

    result = list(map(trace(lambda x: x*2), range(3)))
    print(result)


add_two(2)
print((trace(lambda x: x**2))(3))
main()
