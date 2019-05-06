# def multipy(x, y):
#     return x * y


# multipy(3, 2)
# multipy(3, 2, 3, 5) that doesn't work


# def multipy(*numbers):
#     print(numbers)


# multipy(33, 2, 3, 2, 2)


def multipy(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multipy(3, 23, 3, 2, 2, 2, 243, 5, 2, 5, 32))
