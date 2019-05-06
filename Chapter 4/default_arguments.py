def increment(number, by=1):
    return number + by

# optional parameters in functions must come after required parameters

# def increment(number, by=1,, another):
#     return number + by
# this wil not work


print(increment(2, 5))
print(increment(2))
print(increment(5))
print(increment(6, 6))
