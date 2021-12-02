# for i in range(10):
#     print(f"It's {i}")

while True:
    try:
        x = int(input("please enter number 1:  "))
    except ValueError:
        print("It's not a number")
        break
    try:
        y = int(input("please enter number 2:  "))
    except ValueError:
        print("It's not a number")
        break
    z=x+y
    print (z)
    