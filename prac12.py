def check_palindrome(num):
    number = str(num)
    i = len(number) - 1
    reverse_num = ""
    while i >= 0:
        reverse_num += number[i]
        i -= 1
    if reverse_num == number:
        return "Number is palindrome"
    else:
        return "Number is not palindrome"
inp = int(input("Enter number : "))
print(check_palindrome(inp))