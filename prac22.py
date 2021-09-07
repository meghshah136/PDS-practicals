input_string = input("Enter string : ").lower()
set_of_vowels = {'a','e','i','o','u'}
count = 0

for alphabet in input_string:
    if alphabet in set_of_vowels:
        count += 1

print(f"Number of Vowels : {count}") 