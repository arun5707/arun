def convertions():
    while 1:
        print("Temperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Quit")
        c=int(input("Choose an option (1-6): "))
        if c==1:
            r=(t*9/5)+32
            print("Fahrenheit: ", r)
        elif c==2:
            r=(t-32)*5/9
            print("Celsius: ", r)
        elif c==3:
            r=t+273.15
            print("Kelvin: ", r)
        elif c==4:
            r=t-273.15
            print("Celsius: ", r)
        elif c==5:
            r=(t-32) * 5/9 + 273.15
            print("Kelvin: ", r)
        elif c==6:
            r=(t-273.15)*9/5+32
            print("Fahrenheit: ", r)
        elif c==7:
            exit()
        else:
            print("Invalid choice.")
convertions()
