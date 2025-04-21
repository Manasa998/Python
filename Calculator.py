import sys  # If I want to perform operations with command line arguments, I need to import the 'sys' module."
import os   # if i want to store senstive data in code then import "OS" module
#this is calculator program using functions
#functions will follow the main rule 

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

num  = float(sys.argv[1])
operation = sys.argv[2]
num1 = float(sys.argv[3])

if operation == "add":
    output = add(num, num1)
    print(output)

if operation == "sub":
    output = sub(num, num1)
    print(output)

if operation == "mul":
    output = mul(num, num1)
    print(output)

if operation == "div":
    output = div(num, num1)
    print(output)

if operation == "per":
    output = per(num, num1)
    print(output)

password = os.getenv("password") # sensitive info
