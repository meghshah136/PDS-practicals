def char_counter(word):
    dict_count = {}
    for letter in word:
        dict_count[letter] = word.count(letter)
    return dict_count

input_word = input("Enter word : ")
print(char_counter(input_word))