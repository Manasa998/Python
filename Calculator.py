#this is calculator program using functions
#functions will follow the main rule 
# 1) take inputs
# 2) perform the required action
# 3) then return the vaule
def add(num , num1): # take inputs
    a = num + num1   # perform the required action
    return a         # then return the vaule 

def sub(num , num1):
    b = num - num1
    return b

def mul(num , num1):
    c = num * num1
    return c

def div(num , num1):
    d = num / num1
    return d

def per(num , num1):
    e = num % num1
    return e

print(add(23,34))
print(sub(3,8))
print(mul(5,8))
print(div(5,6))
print(per(5,7))
