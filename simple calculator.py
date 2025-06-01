def calculator():
    while 1:
        print("Enter a number to do Operations like: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. TO quit")
        a=int(input())
        if(a==1):
            b=int(input("Enter a number 1 : "))
            c=int(input("Enter a number 2 : "))
            d=b+c
            print("Answer is ",d);
        elif(a==2):
            b=int(input("Enter a number 1 : "))
            c=int(input("Enter a number 2 : "))
            d=b-c
            print("Answer is ",d);
        elif(a==3):
            b=int(input("Enter a number 1 : "))
            c=int(input("Enter a number 2 : "))
            d=b*c
            print("Answer is ",d);
        elif(a==4):
            b=int(input("Enter a number 1 : "))
            c=int(input("Enter a number 2 : "))
            d=b/c
            print("Answer is ",d);
        elif(a==5):
            break
        else:
            print("error")

calculator()
        
