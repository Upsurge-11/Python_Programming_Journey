import os

path_file = "C:\\Users\\KIIT\\Python Programs\\Beginner\\text.txt"
path_folder = "C:\\Users\\KIIT\\Python Programs\\Beginner\\test_folder"

if os.path.exists(path_file):
    print("That location exist!!")
    if os.path.isfile(path_file):
        print("That is a file.")
if os.path.exists(path_folder):
    print("That location exist!!")
    if os.path.isdir(path_folder):
        print("This is a directory!!")
else:
    print("That location doesn't exist!!")