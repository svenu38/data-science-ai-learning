print("welcome to out play a greater then 3 number program ")

num1 = int(input("Enter a first number:  "))
num2 = int(input("Enter a second number:  "))
num3 = int(input("Enter a third number:  "))

print("The numbers you entered are:", num1, num2, num3)
print(type(num1), type(num2), type(num3))

if num1 > num2 and num1 > num3 :
    print(f"{num1} is the grestes number")
elif num2 > num1 and num2 > num3 :
    print(f"{num2} is the grestes number")
else :
    print(f"{num3} is the grestes number")
