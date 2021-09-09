# str.format is an optional method that gives users more control when displaying output.

animal = input()
item = input()

print("The {} jumped over the {}.".format(animal,item))

print("I, {1} {2} {3} will rule the {0}.".format("world","Lord","Arghyadeep","Mukherjee"))

print("The {animal} jumped over the {item}.".format(animal = "zebra",item = "girl"))
print("The {item} jumped over the {item}.".format(animal = "zebra",item = "girl"))
print("The {0} jumped over the {0}.".format(animal,item))

text = "The {} jumped over the {}"

print(text.format(animal,item))

name = "Arghyadeep"

print("Hello! my name is {}".format(name))
print("Hello! my name is {:50}. Nice to meet you".format(name)) # Default left alligned
print("Hello! my name is {:<50}. Nice to meet you".format(name)) # left alligned
print("Hello! my name is {:>50}. Nice to meet you".format(name)) # Right alligned
print("Hello! my name is {0:^50}. Nice to meet you".format(name)) # Center alligned

number = 3.14159

print("The number pi is {:.2f}.".format(number)) # 2 decimal precision

number = 1000

print("The number is {:,}.".format(number)) # Adds , after in american number system format
print("The number is {:b}.".format(number)) # Returns the binary represntation of the number
print("The number is {:o}.".format(number)) # Returns the octal represntation of the number
print("The number is {:X}.".format(number)) # Returns the hexadecimal represntation of the number
print("The number is {:E}.".format(number)) # Returns the scientific notation of the number