def second_smallest(li):
    smallest = float("inf")
    second = float("inf")

    for num in li:
        if num<smallest:
            second = smallest
            smallest = num
        elif num>smallest and num<second:
            second = num

    return second
print(second_smallest([10, 5, 8, 10, 3]))
