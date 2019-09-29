def helloworld():
    print("Hello, World!")
def hellouser():
    name = input("What is your name?")
    print("Hello " + name)
def converter():
    c=input("Please type in temperatire in Celsius:")
    try:
      f=float(c)*1.8+32
      print("Temperature in Fahrenheit: ",f)
    except ValueError:
      print("Please input a number.")  

while True:
    print("Choose the following program to run:\n1.Hello World\n2.Hello User\n3.Celsius to Fatrenheit Converter\n4.Quit")
    var= input("Type in your choose in number:")
    try:
        if int(var)==1:
            helloworld()
        else:
            if int(var)==2:
                hellouser()
            else:
                if int(var)==3:
                    converter()
                else:
                    if int(var)==4:
                        break
                    else:
                        print("Please choose only 1 to 3")
        print("-------------------------------------")
    except ValueError:
        print("Please input a number.")  
 
