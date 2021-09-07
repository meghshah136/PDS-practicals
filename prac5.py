num1,num2,num3 = input("Enter three numbers : ").split(" ")
if (num1 > num2) and (num1 > num3) :
    largest = num1
    if num2 < num3:
        smallest = num2
    else:
        smallest = num3
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
    if num1 < num3:
        smallest = num1
    else:
        smallest = num3
else:
    largest = num3
    if num2 < num1:
        smallest = num2
    else:
        smallest = num1
print(f"Largest : {largest}")
print(f"Smallest : {smallest}")