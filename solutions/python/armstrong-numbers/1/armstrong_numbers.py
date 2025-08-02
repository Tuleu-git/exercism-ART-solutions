def is_armstrong_number(number):
    n = 0
    while True:
        if number // (10**n):
            n += 1 
        else:
            break    
    return number == sum([ (number % (10 ** (i+1)) // (10 ** i)) ** n for i in range(n)])