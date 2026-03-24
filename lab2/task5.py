names = []

while True:
    name = input("Enter name (or done to stop): ")

    if name == "done":
        break

    names.append(name)

result = {}

for name in names:
    first_letter = name[0].lower()

    if first_letter not in result:
        result[first_letter] = []

    result[first_letter].append(name)

print(result)