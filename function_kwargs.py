# def print_dog_info(owner, *dogs): # * <- means several arguments
#     print(f"The owner of the dog is {owner}")
#     for dog in dogs:
#         print(f"The dog's name is {dog}")

# print_dog_info('igor', 'shepherd', 'aussie')

def print_dog_info(owner, **dogs): # * <- kwargs
    print(f"The owner of the dog is {owner}")
    for dog, name in dogs.items():
        print(f"{name} is {dog}")


print_dog_info('igor', shepherd="grace", aussie="Mona")

