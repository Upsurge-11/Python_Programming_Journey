import math

pi = 3.14159
print(round(pi)) # the round function returns the integer part of the number passed as the parameter.
print(math.ceil(pi)) # the ceil funciton returns the ceil value of the number passed as the parameter.
print(math.floor(pi)) # the floor function returns the floor value of the number passed as the parameter.

x = -4.5
print(round(x))
print(math.floor(x))
# There is a subtle between floor and round function, which may be not visible in using them on non negative numbers.
# floor function gives the gif of the number, while the round function gives the integer part of the number passed as the parameter.

print(abs(x)) # the abs function gives the positive of the number, that is, it makes negative number positive and let the positive number be as such.

x = 3.14159
print(pow(x,2)) # pow(x,y) function returns x**y.

print(math.sqrt(pi)) # the sqrt function returns the sqaure root of the paramter passed. It takes only positive numbers as parameters.

x = 1.9
y = 2.1
z = 3.3

print(max(x,y,z)) # the max function returns the maximum of the numbers passed as the parameter.
print(min(x,y,z)) # the min function returns the minimum of the numbers passed as the parameter.