utensils = {"Spoon", "Fork", "Knife", "Knife", "Knife"}

utensils.add("napkin") # Adds the element in the set.
utensils.add("Kadhai")
utensils.remove("napkin") # Removes the element from the set.

for x in utensils:
    print(x)

utensils.clear() # Removes all the element from the set.

for x in utensils:
    print(x)

dishes = {"Bowl", "Plate", "Cup"}

utensils.update(dishes) # Adds multiple(all) elements in the set from another set.

print()

for i in utensils:
    print(i)

dinner_table = utensils.union(dishes) # dinner_table = utensils + dishes

print()

for i in dinner_table:
    print(i)

print()

z = {7, 8, 4, 3, 2, 69}
y = {3, 5 , 6, 2 , 402, 3, 7}

print(z.difference(y)) # Returns those elements which are not present in y but present in z.
print(y.difference(z)) # Returns those elements which are not present in z but present in y.
print(z.intersection(y)) # Returns those elements which are common between y and z.
print(y.intersection(z))

# Sets are unindexed thus printing it's elements gives different results varying in order everytime.
# No duplicates are allowed in sets. Duplicate elements are ignored.