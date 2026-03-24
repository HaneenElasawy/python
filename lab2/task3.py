#multiplication table
n = int(input("Enter number: "))

result = []

for i in range(1, n+1):
    row = []
    for j in range(1, i+1):
        row.append(i * j)
    result.append(row)

print(result) 