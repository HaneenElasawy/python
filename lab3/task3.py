def show_python_grades():
    with open("grades.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            student_id = data[0]
            subject = data[1]
            grade = data[2]

            if subject == "Python":
                print(student_id, grade)

show_python_grades()