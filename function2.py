def sayhey(name):
    print(f"hey {name} ")
    def inner_sayhey(): #only available inside the mother function
        print(f"I'm inner function")

print (sayhey('petr'))
