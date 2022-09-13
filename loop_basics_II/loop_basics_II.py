# 1 ********************************
def biggie_size(lst):
    for i in range(0, len(lst), 1):
        if lst[i] > 0:
            lst[i] = "big"
    return lst


print(biggie_size([1, 3, -1, 4, -2]))
# 2 ********************************
def count_positives(lst):
    count = 0
    for i in range(0, len(lst), 1):
        if lst[i] > 0:
            count += 1
        lst[len(lst) - 1] = count
    return lst


print(count_positives([1, 2, 3, 4, -2, -3, -4]))
# 3 ********************************
def sum_total(lst):
    sum = 0
    for i in range(0, len(lst), 1):
        sum += lst[i]
    return sum


print(sum_total([1, 2, 3, 4, 5]))
# 4 ********************************
def average(lst):
    return sum_total(lst) / len(lst)


print(average([1, 2, 3, 4, 5]))
# 5 ********************************
def length(lst):
    return len(lst)


print(length([1, 2, 3, 4, 5]))
# 6 ********************************
def minimum(lst):
    min = lst[0]
    for i in range(1, len(lst), 1):
        if lst[i] < min:
            min = lst[i]
    return min


print(minimum([0, 1, 3, 5, -2]))
# 7 ********************************
def maximum(lst):
    max = lst[0]
    for i in range(1, len(lst), 1):
        if lst[i] > max:
            max = lst[i]
    return max


print(maximum([0, 1, 3, 5, -2]))
# 8 ********************************
def ultimate_analysis(lst):
    return {
        "sumTotal": sum_total(lst),
        "average": average(lst),
        "minimum": minimum(lst),
        "maximum": maximum(lst),
        "length": length(lst),
    }


print(ultimate_analysis([1, 2, 3, 4, 5, 6]))
# 9 ********************************
def reverse_list(lst):
    for i in range(0, int(len(lst) / 2), 1):
        temp = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = temp
    return lst


print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
