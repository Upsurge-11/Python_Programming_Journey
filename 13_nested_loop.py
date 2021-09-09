rows = int(input())
columns = int(input())
symbol = input()

for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print()

# By default the end of print is always \n which is next line. We can change it by using end keyword as above.