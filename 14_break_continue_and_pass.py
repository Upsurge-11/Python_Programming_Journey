while 1:
    name = input()
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i,end = "")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i,end=" ")

# This statement is used to skip over the execution part of the loop on a certain condition. After that, it transfers the control to the beginning of the loop. Basically, it skips its following statements and continues with the next iteration of the loop.

# As the name suggests pass statement simply does nothing. We use pass statement to write empty loops. Pass is also used for empty control statements, functions and classes.

# In break the loop ends, in continue the loop skips that particular iteration, whereas pass does nothing.