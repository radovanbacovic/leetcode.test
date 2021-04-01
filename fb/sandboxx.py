def make_all_combinations(list1, list2):
    if not list1:
        return []
    if not list2:
        return [x for x in list1]
    return [x + y for x in list1 for y in list2]

list1 = 'abc'
list2 = 'def'


# print(make_all_combinations(list1, list2))

full_list = [[],[]]


my_range = [(x, y) for x in range(len(full_list)) for y in range(1, len(full_list)) if x != y and y > x]
print(my_range)
for x, y in my_range:
    print(make_all_combinations(full_list[x], full_list[y]))


