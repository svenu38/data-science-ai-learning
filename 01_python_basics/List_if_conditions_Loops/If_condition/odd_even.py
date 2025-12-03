n = input("enter the any number: ") # input is taken as string

print(type(n)) # to check the data type of n

if int(n) % 2 == 0: # n is converted to integer for modulus operation, 
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")