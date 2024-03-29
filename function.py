from utils import *


# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
# grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def nack3(values):
    temp = values.copy()

    naked_twins = {}
    for unit in unitlist:
        possible_naked_twins_in_one_unit = {}
        for box in unit:
            if len(values[box]) == 2:
                possible_twin_value = values[box]
                if possible_twin_value in possible_naked_twins_in_one_unit.keys():
                    possible_naked_twins_in_one_unit[possible_twin_value].append(box)
                else:
                    possible_naked_twins_in_one_unit[possible_twin_value] = [box]

        for key_one_twin_set, boxes in possible_naked_twins_in_one_unit.items():
            if len(boxes) >= 2:
                if key_one_twin_set in naked_twins.keys():
                    naked_twins[key_one_twin_set].append(unit)
                else:
                    naked_twins[key_one_twin_set] = [unit]

    for one_twin_set, units_list in naked_twins.items():
        for unit_has_twins in units_list:
            for box in unit_has_twins:
                if temp[box] != one_twin_set:
                    temp[box] = temp[box].replace(one_twin_set[0], '')
                    temp[box] = temp[box].replace(one_twin_set[1], '')

    return temp


def grid_values(grid):
    dictionary = dict(zip(boxes, grid))
    for key, value in dictionary.items():
        if value == '.':
            dictionary[key] = '123456789'
    return dictionary


def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values


def eliminate2(values):
    solved_boxes = [key for key in values.keys() if len(values[key]) == 1]
    for box in solved_boxes:
        solved_value = values[box]
        peer = peers[box]
        for peer_key in peer:
            values[peer_key] = values[peer_key].replace(solved_value, '')
    return values


def only_choice(values):
    for unit in unitlist:
        counter = {}
        for key in unit:
            value = values[key]

            if len(value) != 1: # doesn't work here! wrong
                for digit in value:
                    if digit in counter:
                        counter[digit] += 1
                    else:
                        counter[digit] = 1
    return values


def only_choice2(values):
    for unit in unitlist:

        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit

    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        eliminate(values)
        # Your code here: Use the Only Choice Strategy
        only_choice2(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    # values = reduce_puzzle(values)
    # if values is False:
    #     return False
    # if all(len(values[s]) == 1 for s in boxes):
    #     return values
    # n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # for value in values[s]:
    #     new_sudoku = values.copy()
    #     new_sudoku[s] = value
    #     attempt = search(new_sudoku)
    #     if attempt:
    #         return attempt
    values = reduce_puzzle(values)
    if values is False:
        return False
    unsolved_box = [box for box in boxes if len(values[box]) > 1]

    if len(unsolved_box) == 0:
        return values

    box, elements_num = min((box, len(values[box])) for box in unsolved_box)

    for unsolved_box_values in values[box]:
        temp = values.copy()
        temp[box] = unsolved_box_values
        attempt = search(temp)
        if attempt:
            return attempt

if __name__ == '__main__':
    grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    grid3 = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    dictionary2 = grid_values(grid3)
    # dictionary2 = naked_twins2(dictionary2)
    # dictionary2 = eliminate2(dictionary2)
    # dictionary2 = only_choice2(dictionary2)
    # dictionary2 = reduce_puzzle(dictionary2)
    # dictionary2 = search(dictionary2)

    print('xxxxxxxx')
    # print('xxxxxxxx')
    # display(after)
    #
    #
    # temp_dic = {}
    # temp_dic['a'] = 3
    # temp_dic['b'] = 3
    # temp_dic['c'] = 4
    # key, value = min((key, temp_dic[key]) for key in temp_dic)
    # print(key)
    # print(value)
    # for i in temp_dic:
    #     print(i)
    #
    # list1 = ['z1','a', 'b','c']
    # list2 = ['z2','c','d','e']
    # print(list1)
    # list1 = set(list1)
    # list1.remove('z1')
    # print(list1)
    # # list2 = set(list2)
    # # list3 = list1 | list2
    # # print(list3)
    # print(unitlist)
    #
    #
    reversedcol = cols[::-1]
    diagdown = [[rows[i] + cols[i] for i in range(len(rows))]]
    print(diagdown)
    diagup = [[rows[i] + reversedcol[i] for i in range(len(rows))]]

