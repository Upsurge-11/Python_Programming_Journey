# **kwargs are parameters that will pack all arguments into a dictionary.
# Useful so that a function can accept a varying amount of keyword arguments.

def hello(**kwargs):
    print("Hello", end=" ")
    for k, v in kwargs.items():
        print(v, end=" ")
    print("!")


hello(title="Ser", first="The King", middle="Arghyadeep", last="Mukherjee")
