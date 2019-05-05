# in python there are three logical operators
# these are
# and
# or
# not

high_income = True
good_credit = True

# both conditions must be true AND
if high_income and good_credit:
    print("eligible 1")

# another try if one is false OR
high_income = False
good_credit = True

if high_income or good_credit:
    print("eligible 2")
else:
    print("Not Eligible 1")

high_income = False
good_credit = True
student = True

if not student:
    print("Eligible 3")
else:
    print("Not Eligible 2")


high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("eligible 4")
else:
    print("Not Eligible 3")
