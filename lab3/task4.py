def show_student_details():
    sid = input("Enter student ID: ")
    name = None

    with open("students.txt", "r") as f:
        for line in f:
            student_id, student_name = line.strip().split(",")
            if student_id == sid:
                name = student_name

    if name is None:
        print("Student not found")
        return

    print("Name:", name)
    print("Grades:")

    with open("grades.txt", "r") as f:
        for line in f:
            student_id, subject, grade = line.strip().split(",")
            if student_id == sid:
                print(subject, grade)

show_student_details()