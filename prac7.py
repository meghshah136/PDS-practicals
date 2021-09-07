largest = 0
count = 0
for i in range(10):
    num = int(input("Enter number : "))
    if num%2 != 0:
        count += 1
        if num > largest:
            largest = num
if count == 0:
    print("You did not add any odd number...")
else:
    print(f"Largest odd number : {largest}")