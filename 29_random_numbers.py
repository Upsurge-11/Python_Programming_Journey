import random

x = random.randint(1, 6)
print(x)

y = random.random()  # Returns numbers between 0 and 1.

print(y)

my_list = ["King", "Arghyadeep", "Boss", "Powerful"]
z = random.choice(my_list)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "K", "Q", "J"]

random.shuffle(cards)
print(cards)
