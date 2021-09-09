# A Function is a block of code which executes only when it is called.

def hello(first_name,last_name,age):
    print("Hello! "+first_name+" "+last_name+". Your age is "+str(age)+".")

first_name = input()
last_name = input()
age = int(input())
hello(first_name,last_name,age)