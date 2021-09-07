def find_HCF(num1,num2):
    i = 1
    if num1 == num2:
        return num1
    elif num1 > num2:
        while True:
            if (num1*i)%num2 == 0:
                return (num1*i)
            i += 1
    else:
        while True:
            if (num2*i)%num1 == 0:
                return (num2*i)
            i += 1

def find_GCD(num1,num2):
    if num1 == num2:
        return num1
    elif num1 < num2:
        i = num1
        while True:
            if num2%i == 0:
                return i
            i -= 1
    else:
        i = num2
        while True:
            if num1%i == 0:
                return i
            i -= 1

number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
print(f"HCF of {number1} & {number2} = {find_HCF(number1,number2)}")
print(f"GCD of {number1} & {number2} = {find_GCD(number1,number2)}")