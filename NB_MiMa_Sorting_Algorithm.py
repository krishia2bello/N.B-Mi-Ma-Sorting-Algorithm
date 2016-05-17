def sort_list(list_of_integers):
    list_input = list_of_integers                          # copying the input list for execution
    sorted_list = []                                       # defining the new(sorted) list
    min_index = 0                                          # defining the index of the minimum value to be inserted in the new list
    max_index = 1                                          # defining the index of the maximum value to be inserted in the new list
    while len(list_input) != 0:                            # while there is still an integer in the input list
        sorted_list.insert(min_index, min(list_input))     # inserting the least value of the input list to the new list
        list_input.remove(min(list_input))                 # removing what was inserted from the previous line
        min_index = min_index + 1                          # setting the next index of the least value to be inserted in the new list
        if len(list_input) != 0:                           # if there are still integers in the list remaining
            sorted_list.insert(max_index, max(list_input)) # insert the greatest value of the input list to the new list
            list_input.remove(max(list_input))             # removing what was inserted from the previous line
            max_index = max_index + 1                      # setting the next index of the greatest value to be inserted in the new list
    return sorted_list                                     # returning the new list as output


print(Test Cases!)

# empty list,
sort_list([]) # expect []

# even length,
sort_list([4, 3, 2, 1]) # expect 1 2 3 4

# odd length,
sort_list([2, 3, 4, 5, 1]) # expect 1 2 3 4 5

# consist of positive and negative integer values,
sort_list([3, -3, 2, -2, 1, 0, -1 ]) # expect -3 -2 -1 0 1 2 3

# consist of integers having the same value in the list,
sort_list([10, -3, 0, 6, 4, 5, 2, 7, 3, 1, -1, 8, 7, 9, -2, -3, 10, 2]) # expect -3 -3 -2 -1 0 1  2 2 3 4 5 6 7 7 8 9 10 10
