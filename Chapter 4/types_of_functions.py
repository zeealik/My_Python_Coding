# Two types of functions

# 1. Perform a task
# 2. Return a value


def greet(name):  # type 1
    print(f"Hi {name}")  # type 1


round(1.9)  # type 2


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Zeeshan")
file = open("content.txt", "w")
file.write(message)
print(message)

greet("Mosh")

print(greet("Mosh"))
# will also return None
# because by default every function return None
