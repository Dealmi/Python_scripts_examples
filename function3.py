# def greeting(name):
#     #print(f"Hello {name}!")
#     hey=(f"Hello {name}!")
#     return hey
# print (greeting('Sasha'))

# def greeting (name='Vasya'):
#     print(f"Hello {name}!")

# greeting()
def greeting(names, m_text):
    for name in names:
        print(f"Hello {name}, {m_text}")

greeting(m_text="LETS GO FOR A beer", name="masha")

names=['masha','misha']
greeting(names)
