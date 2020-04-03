'''
Python module to solve the knapsack problem to maximise loot using greedy algorithms
'''


import math


def get_best_item(input_list):
    ''' Get the best item from the remaining items based on maximum value per weight ratio '''
    most_valuable_index = 0
    best_value = 0
    index = 0
    for weight, value in input_list:

        if weight > 0:
            if weight/value > best_value:
                best_value = weight/value
                most_valuable_index = index
        index += 1
    return most_valuable_index


def optimal_knapsack():
    ''' Accept the inputs for the values and return the maximum loot configuration of the items '''
    temp = input(
        'Enter comma separated inputs or all separate values and space separated weights\nExample:\nw1 v1,w2 v2 ....').split(',')
    input_list = [list(map(int, i.split())) for i in temp]
    cap = int(input('Enter the capacity of the knapsack'))
    total = 0
    knapsack = []
    limit = len(input_list)
    index = 0
    while index < limit:
        best_option = get_best_item(input_list)
        print(best_option)
        print(input_list[best_option])
        weight = input_list[best_option][0]
        quantity = math.floor(cap/weight)
        knapsack.append((weight, quantity))
        input_list.pop(best_option)
        cap -= weight * quantity
        total += weight * quantity
        index += 1

    print(f' The knapsack is :\n{knapsack} \nThe total is {total}')


optimal_knapsack()
