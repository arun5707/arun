import random
def random1():
    while 1:
        a = int(input("Enter a number from 1 to 100 : "))
        b = random.randint(1, 100)
        if a == b:
            print("Numbers are equal")
            break
        else:
            print("Numbers are not equal")
            
random1()


