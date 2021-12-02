import os
print (f"I'm here: {os.getcwd()}")
dir_name= 'test_dir'

if os.path.isdir('test_dir'):
    print ('This dir exists')

else:
    os.mkdir(dir_name)
    print(f"{dir_name} created")

os.chdir(dir_name)
print(f"Now i'm here: {os.getcwd()}")
