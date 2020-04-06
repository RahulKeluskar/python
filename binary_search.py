'''
Recursive implementation of binary search 
'''


def binary_search(sorted_array, low, high, key):
    ''' Accepts sorted array as input and finds the key value between high and low recursively if the value isnt found it will return the probable index for insertion of that value '''
    if high < low:
        print(f'The value can be inserted at index {low - 1}')
        return -1
    import math
    # Finding the middle term for comparison
    mid = low + math.floor((high - low)/2)
    if sorted_array[mid] == key:
        print(f'The item has been found at index {mid}')
    elif sorted_array[mid] > key:
        # Search in the left half of the sub array
        binary_search(sorted_array, low, mid - 1, key)
    elif sorted_array[mid] < key:
        # Search the right half of the subarray
        binary_search(sorted_array, mid+1, high, key)
    return mid


def binary_search_iterative(sorted_array, key):
    ''' Iterative implementation of binary search '''
    low = 0
    high = len(sorted_array)
    import math
    while low <= high:
        mid = low + math.floor((low+high)/2)
        if sorted_array[mid] == key:
            return mid
        elif sorted_array[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    # If element is not found return probable location for insertion of search value
    return low - 1


def main():
    ''' Accept input from user and pass parameters to binary search '''
    sorted_list = list(
        map(float, input('Enter space separated ascending inputs to be searched from').split()))
    KEY = int(input('Enter the search value in the list'))
    print(binary_search(sorted_list, 0, len(sorted_list), KEY))


main()
