# for i in range(10):
#     print(f"It's {i}")

class NegativeNumber(Exception):
    pass

while True:
    try:
        x = int(input("please enter number 1:  "))
        if x < 0:
            raise NegativeNumber (f"Your number is negative: {str(x)}")
    except ValueError:
        print("It's not a number")
        break
    except NegativeNumber as exception:
        print (exception)
        break
    try:
        y = int(input("please enter number 2:  "))
    except ValueError:
        print("It's not a number")
        break
    z=x+y
    print (z)
    break
