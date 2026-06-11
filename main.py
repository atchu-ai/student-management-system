students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")
        dept = input("Enter Department: ")

        student = {
            "Name": name,
            "Roll": roll,
            "Department": dept
        }

        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent Records:")
        for student in students:
            print(student)

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        found = False

        for student in students:
            if student["Roll"] == roll:
                print(student)
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")