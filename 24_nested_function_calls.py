# Function calls inside other function call.
# Innermost function calls are resolved first.
# Returned value is used as argument for the next outer function.

print(round(abs(float(input()))))