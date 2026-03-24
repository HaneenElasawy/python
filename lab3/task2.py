def read_students():
    with open("students.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            name = data[1]
            print(name)

read_students()