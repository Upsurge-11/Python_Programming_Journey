student = ("Arghyadeep",18,"male")
print(student.count("Arghyadeep"))
print(student.count("Hi"))
print(student.index(18))

for i in student:
    print(i)

if "Arghyadeep" in student:
    print("Arghyadeep is here.")

# Tuples are similiar to lists, just that they are immutable.