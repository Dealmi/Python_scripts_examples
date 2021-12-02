def decorator_func(math_func):
    def num_tup(tuple_list):
        return[math_func(num[0], num[1],)for num in tuple_list]
    return num_tup

@decorator_func #decorator

def math_sum(a,b):
    return a+b

print (math_sum([(4,6),(5,7),(5,10)]))
