def find_max(num):
    max_val = num[0]

    for n in num:
        if n>max_val:
            max_val = n
    return max_val
print(find_max([2,4,6,8,9]))
