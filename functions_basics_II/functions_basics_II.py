# 1 ********************************
def count_down():
    print("Enter the number:")
    num = int(input())
    lst = []
    for i in range(num, -1, -1):
        lst.append(i)
    return lst


print(count_down())

# 2 ********************************
def print_and_return(lst):
    print(lst[0])
    return lst[1]


print(print_and_return([1, 3]))

# 3 ********************************
def first_plus_length(lst):
    return lst[0] + len(lst)


print(first_plus_length([1, 5, 8, 7, 4, 6]))

# 4 ********************************
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    else:
        new_lst = []
        for i in range(0, len(lst), 1):
            if lst[i] > lst[1]:
                new_lst.append(lst[i])
        print(len(new_lst))
        return new_lst


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))

# 5 ********************************
def length_and_value(rep, num):
    new_lst = []
    for i in range(0, rep, 1):
        new_lst.append(num)
    return new_lst


print(length_and_value(3, 6))
