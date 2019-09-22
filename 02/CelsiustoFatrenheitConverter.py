c=input("Please type in temperatire in Celsius:")
try:
    f=float(c)*1.8+32
    print("Temperature in Fahrenheit: ",f)
except ValueError:
    print("Please input a number.")