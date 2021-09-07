def ispangram(str):
    all_alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in all_alphabet:
        if char not in str.lower():
            return False
    return True

string = input("Enter string to check is it pangram or not : ")
if ispangram(string):
    print("String is pangram")
else:
    print("String is not pangram")