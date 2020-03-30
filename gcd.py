def gcd(num1, num2):
    '''
    Effective implementation to find gcd of number
    '''
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


print(gcd(270, 120))
