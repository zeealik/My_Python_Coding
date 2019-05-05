age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# another way
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# much simpler, ternary operator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
