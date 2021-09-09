text = "Hello, my name is Arghyadeep Mukherjee.\nI am your king.\nCall me your god."

with open("test.txt","w") as file:
    file.write(text)

with open("test.txt","a") as file:
    file.write("Have a nice day!!")