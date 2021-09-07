def check_prime(num):
    i = 1
    count = 0
    while i <= num:
        if num%i == 0:
            count += 1
        i += 1
    if count <= 2:
        return True
    else:
        return False
num1 = int(input("Enter lower range : "))
num2 = int(input("Enter higher range : "))
for i in range(num1, num2+1):
    if check_prime(i):
        print(i,end=" ")
    else:
        pass