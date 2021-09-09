import os

source = "C:\\Users\\KIIT\\Dropbox\\My PC (BT1000100888)\\Desktop\\test.txt"
destination = "C:\\Users\\KIIT\Python Programs\\Beginner\\test_folder\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source, destination)
        print(source+" was moved!!")
except FileNotFoundError:
    print(source+" was not found!")

# You can move a folder too with the same method.