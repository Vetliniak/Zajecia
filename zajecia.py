def sort_recipe(list_element):
    if list_element[1] != list_element[1]:
        return list_element[2]
    else:
        return list_element[1]
list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort.sort(key=sort_recipe, reverse=False)
print(list_to_sort)

list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

list_to_sort_2.sort(key=sort_recipe, reverse=False)
print(list_to_sort_2)
