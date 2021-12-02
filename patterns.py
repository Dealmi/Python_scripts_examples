import re

emails= '''
test@gmail.com
test@mail.ru
test@epam.com
'''

pattern = re.compile(r'[a-zA-Z_.-]+@[a-zA-Z_.-]+\.[a-zA-Z]+')
matches = pattern.finditer(emails)

for match in matches:
    print (match)
