# Exception is an event detected during execution that interrupt the flow of a program.

try:
    num = int(input())
    den = int(input())
    res = num/den
except ZeroDivisionError as e:
    print(e)
    print("The denominator can't be zero.")
except ValueError as e:
    print(e)
    print("Enter only numbers please.")
except Exception as e:
    print(e)
    print("Something went wrong!!")
else:
    print(res)
finally:
    print("This will always execute.")