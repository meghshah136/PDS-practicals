def factorial(num):
    ans = 1
    if num < 0:
        return "Please enter positive number..."
    else:
        for i in range(1,num+1):
            ans *= i
        return ans
number = int(input("Enter number : "))
print(factorial(number))