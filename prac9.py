number = input("Enter number : ")
i = len(number) - 1
reverse_num = ""
while i >= 0:
    reverse_num += number[i]
    i -= 1
if reverse_num == number:
    print("Number is palindrome")
else:
    print("Number is not palindrome")