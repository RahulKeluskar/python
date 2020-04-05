'''
Module to implement seletion sort using python
'''


def get_minimum_index(seq, start):
    ''' Get the index of the minimum element in the sequence starting from the start index provided '''
    min_index = start
    # Loop to run from the start index to the last item
    for index in range(start+1, len(seq)):
        if seq[min_index] > seq[index]:
            min_index = index
    return min_index


def selection_sort(unsorted_list):
    ''' Takes unsorted list as input and sorts values in ascending order using selection sort '''
    for index in range(len(unsorted_list)-1):
        minimum_index = get_minimum_index(unsorted_list, index)
        temp = unsorted_list[index]
        unsorted_list[index] = unsorted_list[minimum_index]
        unsorted_list[minimum_index] = temp

    return unsorted_list


def main():
    ''' Accept input for sorting '''
    input_list = list(
        map(float, input('Enter the space separated list').split()))
    print(f' The sorted list is {selection_sort(input_list)}')


main()
