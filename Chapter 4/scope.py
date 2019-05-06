# def greet():
#     message = "a" # local variable
#     the scope of message is only in greet function


# print(message)

# def greet(name):
#     message = "a"
# the scope of message is only in greet function


# print(name)

# def send_email(name):
#     message = "b"

# greet("Mosh")

message = "a"  # global variable


def greet(name):
    global message
    message = "b"
    # the scope of message is only in greet function


greet("Zeeshan")
print(message)
