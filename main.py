from math import sqrt
root = int(input("Enter number to calculate approximate root: "))
approx = int(sqrt(root)) #The purpose of this variable is to find the closest integer square root of the number we are trying to calculate the root of.
results = []

def func(x):
    return x**2 - root
    #For this method we should create o function
    #This function will be like this x^2 - a
    # a is number we trying to calculate its root

def der_func(x):
    return 2*x
    #This is derivative of our main function

a = approx - (func(approx)/der_func(approx))
results.append(a)

for i in range(100):
    d = results[i]
    b =  d- (func(d)/der_func(d))
    results.append(b)
    if results[i] == results[i+1]:
        break
    else:
        print(b)
