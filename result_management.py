students = []


def add_student():
    name = input("Enter student name: ")

    print("Enter marks out of 100:")

    python = float(input("Python: "))
    maths = float(input("Maths: "))
    dsa = float(input("DSA: "))
    physics = float(input("Physics: "))
    english = float(input("English: "))

    marks = [python, maths, dsa, physics, english]

    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    student = {
        "name": name,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }

    students.append(student)

    print("\nStudent added successfully!")


def view_students():
    if not students:
        print("\nNo student records found.")
        return

    print("\n===== STUDENT RESULTS =====")

    for student in students:
        print(f"\nName       : {student['name']}")
        print(f"Total      : {student['total']}/500")
        print(f"Percentage : {student['percentage']:.2f}%")
        print(f"Grade      : {student['grade']}")
        print(f"Result     : {student['result']}")


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found!")
            print(f"Name       : {student['name']}")
            print(f"Total      : {student['total']}/500")
            print(f"Percentage : {student['percentage']:.2f}%")
            print(f"Grade      : {student['grade']}")
            print(f"Result     : {student['result']}")
            return

    print("Student not found.")


def highest_student():
    if not students:
        print("\nNo student records found.")
        return

    highest = max(students, key=lambda student: student["percentage"])

    print("\n===== TOP STUDENT =====")
    print(f"Name       : {highest['name']}")
    print(f"Percentage : {highest['percentage']:.2f}%")
    print(f"Grade      : {highest['grade']}")


while True:

    print("\n==============================")
    print(" STUDENT RESULT MANAGEMENT")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Find Top Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        highest_student()

    elif choice == "5":
        print("\nThank you!")
        break

    else:
        print("\nInvalid choice!")
