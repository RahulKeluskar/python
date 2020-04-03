'''
Python module to solve the knapsack problem to maximise loot using greedy algorithms
'''


def get_best_item(input_list):
    ''' Get the best item from the remaining items based on maximum value per weight ratio '''
    most_valuable_index = 0
    bestValue = 0
    index = 0
    for weight, value in input_list:
        index += 1
        if weight > 0:
            if weight/value > bestValue:
                bestValue = weight/value
                most_valuable_index = i
    return most_valuable_index


def optimal_knapsack():
    ''' Accept the inputs for the values and return the maximum loot configuration of the items '''
    l = input('Enter comma separated inputs or all separate values and space separated weights\nExample:\nw1 v1,w2 v2 ....').split(',')
    input_list = [list(map(float, i.split())) for i in l]
    print(input_list)


optimal_knapsack()
