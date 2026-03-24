def create_files():
    with open("students.txt", "w") as f:
        f.write("1,Ahmed Ali\n")
        f.write("2,Sara Mohamed\n")
        f.write("3,Omar Hassan\n")

    with open("grades.txt", "w") as f:
        f.write("1,Python,85\n")
        f.write("1,Math,90\n")
        f.write("2,Python,78\n")
        
create_files()