# word = input("Enter a word: ")
# vowels = "aeiou"
# result = ""
# for char in word:
#     if char not in vowels:
#         result += char
# print(result)

def remove_vowels(word):
    vowels = "aeiou"

    for v in vowels:
        word = word.replace(v, "")
    return word

word = input("Enter a word: ")
print(remove_vowels(word))