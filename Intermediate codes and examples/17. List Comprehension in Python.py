# NOTE: Syntax:-
# new_list = [new_item for item in list]
# new_list = [item for item in list if any_condition == True/false]

numbers = [x+1 for x in range(100)]
print(numbers, '\n\n')

even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [num for num in range(10) if num not in even_numbers]
print(odd_numbers, '\n\n')

list_of_squares = [num**2 for num in numbers]
print(list_of_squares, '\n\n')

doubled_numbers = [num*2 for num in range(1, 6)]
print(doubled_numbers, '\n\n')
