def average_grades():
    data = {}

    with open("students.txt", "r") as f:
        for line in f:
            sid, name = line.strip().split(",")
            data[sid] = {"name": name, "grades": []}

    with open("grades.txt", "r") as f:
        for line in f:
            sid, subject, grade = line.strip().split(",")
            if sid in data:
                data[sid]["grades"].append(int(grade))

    for sid in data:
        grades = data[sid]["grades"]
        if grades:
            avg = sum(grades) / len(grades)
            print(data[sid]["name"], avg)

average_grades()