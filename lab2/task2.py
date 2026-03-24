text= input("Enter text: ")
letter = input("Enter letter: ")

result = []
# for index, char in enumerate(text):  
#     if char.lower() == letter.lower():
#         result.append(index)


for i in range(len(text)):
    if text[i].lower() == letter.lower():
        result.append(i)

print(result)