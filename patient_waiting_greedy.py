'''
Implementation of Greedy algorithm to find the least waiting time at a clinic
'''


def get_minimum_time(array):
    ''' 
    Get index of minimum element in array in parameter 
    '''
    minimum = array[0]
    minimum_index = 0
    for index, value in enumerate(array):
        if value < minimum:
            minimum_index = index
    return minimum_index


def get_optimum_time(array):
    '''
    Accept an array and provide the least amount of time to be taken in the form of a 2d array with the first element being the time and the second being the patient number
    '''
    time = []
    while len(array) > 0:
        minimum = get_minimum_time(array)
        time.append((array.pop(minimum), f'Patient number {minimum+1}'))
    return time


if __name__ == '__main__':
    LIMIT = int(input('Enter the number of patients'))
    ARRAY = [
        int(input(f'Enter the waiting time for patient {i+1}:')) for i in range(LIMIT)]
    print(get_optimum_time(ARRAY))
