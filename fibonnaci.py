def fibonacci(n):
    array = [0 for i in range(n)]
    array[0] = 0
    array[1] = 1
    for i in range(2, n):
        array[i] = array[i-1] + array[i-2]
    return array[n-1]


print(fibonacci(99))
