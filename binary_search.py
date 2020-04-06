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


def main():
    ''' Accept input from user and pass parameters to binary search '''
    sorted_list = list(
        map(float, input('Enter space separated ascending inputs to be searched from').split()))
    KEY = int(input('Enter the search value in the list'))
    print(binary_search(sorted_list, 0, len(sorted_list), KEY))


main()
