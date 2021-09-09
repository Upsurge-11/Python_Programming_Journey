name = "arghyadeep mukherjee"
print(len(name)) # returns the length of  the string.
print(name.find("m")) # returns the first index of occurence of the element passed as parameter. returns -1 if no such elementis found.
print(name.capitalize()) # capitalizes the element present at index 0.
print(name.upper())# capitalizes every character of the string. Spaces are left as such.
print(name.lower()) # lowers every character of the string. Spaces are left as such.
print(name.isdigit()) # returns a boolean that weather a string contains only digits or not.
name = "123"
print(name.isdigit())
name = "arghyadeep mukherjee"
print(name.isalpha()) # It will give a false because we have added a space between them.
name = "rick"
print(name.isalpha()) # returns a boolean that weather a string contains only alphabets or not.
name = "arghyadeep"
print(name.count("a")) # gives the frequency of the element passed as parameter in the function.
print(name.replace("a", "o")) # replaces the first parameter with the second parameter everywhere in the string.
print(name*3) # it's not a function but it is helpful to 