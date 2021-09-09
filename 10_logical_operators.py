temp = int(input())

if temp >= 0 and temp <= 30:
    print("The temperature is good today... Go outside.")
elif (temp < 0 or temp > 30) and temp > -273:
    print("The temperature is not good today...... Stay home.")
elif not(temp > -273):
    print("The temperature you entered is not possible you moron.")