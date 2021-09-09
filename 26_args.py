# *args is a parameter that will pack all arguments into a tuple.
# Useful so that a function can accept a varying amount of arguments.
# You can use any name in place of args after *. args is just a convention.

def add(*args):
    sums = 0
    for i in args:
        sums += i
    return sums


print(add(1, 2, 3, 4, 5))
