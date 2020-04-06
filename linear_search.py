''' Divide and conquer implementation of linear search in python '''


def linear_search(array, low, high, key):
    ''' Find the key value within range low and high in array '''
    if high < low:
        print('The value doesnt exist in array')
        return -1
    if array[low] == key:
        return low
    return linear_search(array, low+1, high, key)


def main():
    ''' Accept array input and the search key to be passed to the linea search function '''

    unsorted_list = list(
        map(float, input('Enter space separated inputs to be searched from').split()))
    KEY = int(input('Enter the search value in the list'))
    print(linear_search(unsorted_list, 0, len(unsorted_list), KEY))


main()
