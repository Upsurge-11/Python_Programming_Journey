# A dictionary is a mutable, unordered collection of unique key:value pairs.
# They are fast as they use hashing. Allow us to access a value quickly.
# The keys are immutable but the values can be changed.

capitals = {"India":"New Delhi", "USA":"Washington DC", "Russia":"Moscow", "China":"Beijing"}

print(capitals["Russia"]) # To get a value to any specific key.
print()

print(capitals.get("Germany")) # Using get is more efficient as it will print None if key is not found whereas in the above method, it will give an error.
print()

print(capitals.keys()) # Return all the keys of the dictionary.
print()

print(capitals.values()) # Return all the values of the dictionary.
print()

print(capitals.items()) # Returns all the values and keys combined of the dictionary.
print()

print(capitals) # Return the dictionary as it is, with : and {}.
print()

for key,values in capitals.items(): # Way to iterate through dictionary.
    print(key,values)
print()

capitals.update({"Germany":"Berlin"}) # You may add a new key:value pair using the update method.

for key,values in capitals.items():
    print(key,values)
print()

capitals.update({"India":"Kolkata"}) # Change the value of any existing key.

for key,values in capitals.items():
    print(key,values)
print()

capitals.pop("China") # Removes an key:value pair.

for key,values in capitals.items():
    print(key,values)
print()

capitals.clear() # Deletes the whole dictionary.
print()

for key,values in capitals.items():
    print(key,values)