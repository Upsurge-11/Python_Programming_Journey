import shutil

# copyfile() = copies contents of a file.
# copy() = copyfile() + permission mode + destination can be a directory.
# copy2() = copy() + copies metadata (file's creation and modification times).

shutil.copyfile("C:\\Users\\KIIT\\Python Programs\\Beginner\\test_folder\\src.txt","C:\\Users\\KIIT\\Python Programs\\Beginner\\test_folder\\dst.txt")  # src,dst