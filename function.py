def power (base, exponent):
    return base ** exponent

def power2(method, exponents):
    result=list()
    for exp in exponents:
        result.append(method(2,exp))
    return result


answers = power2(power, [2,4,6,7,12])
print (answers)
