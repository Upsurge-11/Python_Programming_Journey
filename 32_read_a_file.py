try:
    with open("C:\\Users\\KIIT\\Python Programs\\Beginner\\text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!!")
print(file.closed) # If you use with keyword while opening ur file, it automatically closes the file after use.