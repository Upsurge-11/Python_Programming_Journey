name = "Arghyadeep Mukherjee"

# for slicing you may use [] and the syntax is string_name[start:stop:step], here start is the starting index, which is inclusive. Stop is the ending index +1 as it is not inclusive. Step here refers to the pattern or the jump the pointer will take while slicing. That is, by how much we are increasing from start to end while slicing.

# By default step is always 1.

first_name = name[:10] # By default start is 0, thus it is not needed to pass 0 as start.
last_name = name[11:] # By default end is len(string_name)-1, thus it is not needed to pass len(string_name)-1 as end.
print(first_name)
print(last_name)
print(name[::2])

# How to reverse a string.

reverse_name = name[::-1] # The start and end is compromised with respect to the step.
print(reverse_name)

# Slicing using slice()
# The only advantage that slice has over using [] is that you can create an object out of that and use it multiple times. 
website1 = "http://google.com"
website2 = "http://facebook.com"

slice = slice(7,-4) # same syntax as using [], that is slice(start,end,step)
print(website1[slice])
print(website2[slice])

# 0  1  2  3  4  5  6  7  8
# 6 32 45  6 69  1  2  5  4
#-9 -8 -7 -6 -5 -4 -3 -2 -1