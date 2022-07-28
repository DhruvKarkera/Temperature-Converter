celsius = float(input("Please input the temperature in celsius :"))
fahrenheit=(9/5)*celsius+32
print(fahrenheit)
if (fahrenheit >= 104):
    print("It's hot")
elif (fahrenheit <= 50):
    print("It's cold")
else:
    print("The temperature is nice")