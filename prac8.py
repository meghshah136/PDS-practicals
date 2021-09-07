number = input("Enter number : ")
total = 0
for i in number:
    total += int(i)**3
if int(number) == total:
    print("Number is armstrong")
else:
    print("Number is not armstrong")