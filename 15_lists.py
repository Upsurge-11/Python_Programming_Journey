food = ["pizza","biriyani","burger","noodles"]
print(food)
print(food[1])
food[1] = "roasted chicken"

print(food[1])

for i in food:
    print(i)

food.append("icecream") # append adds an element at the end of the loop.
food.remove("burger") # remove deletes the element passed as a parameter, returns error if element not found.
food.append("sushi") 
food.pop() # removes the last element in the list.
print(food)
food.insert(0,"cake") # insert an element(second parameter) at the index at the index passed as the first parameter.
print(food)
food.sort() # sorts the list in lexical order if it is a string or character.
print(food)
food.clear() # deletes alll the elements inside the list.
print(food)
x = [7,4,2,5,1,69,2,4]
x.sort() # sorts the list in ascending order.
print(x)