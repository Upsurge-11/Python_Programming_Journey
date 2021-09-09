import os
import shutil

path = "C:\\Users\\KIIT\\Python Programs\\Beginner\\test_folder"

try:
    #os.remove(path) # Used for deleting the file.
    #os.rmdir(path) # This deletes only empty folders.
    shutil.rmtree(path) # delete an entire directory irrespective of whether it is empty or not.
except FileNotFoundError:
    print("The file was not found!!")
except PermissionError:
    print("You don't have the permission to delete this.")
except OSError:
    print("Yor cannot delete that using that function.")
else:
    print(path+" was deleted.")