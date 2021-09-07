def check_palindrome(stri):
    i = len(stri) - 1
    reverse = ""
    while i >= 0:
        reverse += stri[i]
        i -= 1
    if reverse == stri:
        return "String is palindrome"
    else:
        return "String is not palindrome"
inp = input("Enter number : ")
print(check_palindrome(inp))