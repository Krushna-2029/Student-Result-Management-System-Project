# ============================================
#   Student Result Management System
#   Author  : Krushna
#   Sem     : 1st Semester
#   Language: Python (No External Libraries)
# ============================================

students = []   # List to store all student records


# ---------- UTILITY FUNCTIONS ----------

def line(ch="-", n=50):
    print(ch * n)

def get_grade(percentage):
    if percentage >= 90:
        return "O  (Outstanding)"
    elif percentage >= 75:
        return "A+ (Excellent)"
    elif percentage >= 60:
        return "A  (Very Good)"
    elif percentage >= 50:
        return "B  (Good)"
    elif percentage >= 40:
        return "C  (Average)"
    else:
        return "F  (Fail)"

def is_pass(marks_list):
    for m in marks_list:
        if m < 40:
            return False
    return True


# ---------- CORE FUNCTIONS ----------

def add_student():
    line("=")
    print("         ADD NEW STUDENT")
    line("=")

    name = input("Enter Student Name   : ").strip()
    roll = input("Enter Roll Number    : ").strip()

    # Check if roll number already exists
    for s in students:
        if s["roll"] == roll:
            print("\n  Roll number already exists!")
            return

    subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]
    marks = []

    print(f"\n  Enter marks out of 100 for each subject:")
    for sub in subjects:
        while True:
            try:
                m = int(input(f"    {sub:<12}: "))
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                else:
                    print("    Enter marks between 0 and 100.")
            except ValueError:
                print("    Invalid input. Enter a number.")

    total      = sum(marks)
    percentage = total / len(subjects)
    grade      = get_grade(percentage)
    result     = "PASS" if is_pass(marks) else "FAIL"

    student = {
        "name"      : name,
        "roll"      : roll,
        "subjects"  : subjects,
        "marks"     : marks,
        "total"     : total,
        "percentage": percentage,
        "grade"     : grade,
        "result"    : result
    }

    students.append(student)
    print(f"\n  Student '{name}' added successfully!")


def view_all():
    line("=")
    print("         ALL STUDENTS RESULT")
    line("=")

    if not students:
        print("  No student records found.")
        return

    print(f"  {'Roll':<8} {'Name':<20} {'Total':<8} {'%':<8} {'Result'}")
    line()
    for s in students:
        print(f"  {s['roll']:<8} {s['name']:<20} {s['total']:<8} {s['percentage']:<8.1f} {s['result']}")
    line()
    print(f"  Total Students: {len(students)}")


def view_result_card():
    line("=")
    print("         VIEW RESULT CARD")
    line("=")

    if not students:
        print("  No student records found.")
        return

    roll = input("  Enter Roll Number: ").strip()

    found = None
    for s in students:
        if s["roll"] == roll:
            found = s
            break

    if not found:
        print("  Student not found!")
        return

    line("*")
    print("           RESULT CARD")
    line("*")
    print(f"  Name        : {found['name']}")
    print(f"  Roll Number : {found['roll']}")
    line()
    print(f"  {'Subject':<15} {'Marks':>6}  {'Status'}")
    line()
    for i in range(len(found["subjects"])):
        status = "Pass" if found["marks"][i] >= 40 else "FAIL"
        print(f"  {found['subjects'][i]:<15} {found['marks'][i]:>6}  {status}")
    line()
    print(f"  {'Total':<15} {found['total']:>6}")
    print(f"  {'Percentage':<15} {found['percentage']:>5.1f}%")
    print(f"  {'Grade':<15} {found['grade']}")
    print(f"  {'Result':<15} {found['result']}")
    line("*")


def show_topper():
    line("=")
    print("         CLASS TOPPER")
    line("=")

    if not students:
        print("  No student records found.")
        return

    topper = students[0]
    for s in students:
        if s["percentage"] > topper["percentage"]:
            topper = s

    print(f"  Name       : {topper['name']}")
    print(f"  Roll No    : {topper['roll']}")
    print(f"  Percentage : {topper['percentage']:.1f}%")
    print(f"  Grade      : {topper['grade']}")
    print(f"  Result     : {topper['result']}")


def search_student():
    line("=")
    print("         SEARCH STUDENT")
    line("=")

    if not students:
        print("  No student records found.")
        return

    name = input("  Enter name to search: ").strip().lower()
    found_list = []

    for s in students:
        if name in s["name"].lower():
            found_list.append(s)

    if not found_list:
        print("  No student found with that name.")
    else:
        print(f"\n  Found {len(found_list)} result(s):\n")
        for s in found_list:
            print(f"  Roll: {s['roll']}  |  Name: {s['name']}  |  {s['percentage']:.1f}%  |  {s['result']}")


def show_statistics():
    line("=")
    print("         CLASS STATISTICS")
    line("=")

    if not students:
        print("  No student records found.")
        return

    total_students = len(students)
    passed = sum(1 for s in students if s["result"] == "PASS")
    failed = total_students - passed
    avg    = sum(s["percentage"] for s in students) / total_students
    high   = max(s["percentage"] for s in students)
    low    = min(s["percentage"] for s in students)

    print(f"  Total Students : {total_students}")
    print(f"  Passed         : {passed}")
    print(f"  Failed         : {failed}")
    print(f"  Pass %         : {(passed/total_students)*100:.1f}%")
    print(f"  Class Average  : {avg:.1f}%")
    print(f"  Highest Score  : {high:.1f}%")
    print(f"  Lowest Score   : {low:.1f}%")


# ---------- MAIN MENU ----------

def main():
    print("\n" + "=" * 50)
    print("    STUDENT RESULT MANAGEMENT SYSTEM")
    print("    Python | No External Libraries")
    print("=" * 50)

    while True:
        print("\n  MENU")
        line()
        print("  1. Add Student")
        print("  2. View All Students")
        print("  3. View Result Card")
        print("  4. Search Student")
        print("  5. Show Class Topper")
        print("  6. Class Statistics")
        print("  7. Exit")
        line()

        choice = input("  Choose (1-7): ").strip()

        if   choice == "1": add_student()
        elif choice == "2": view_all()
        elif choice == "3": view_result_card()
        elif choice == "4": search_student()
        elif choice == "5": show_topper()
        elif choice == "6": show_statistics()
        elif choice == "7":
            print("\n  Thank you! Goodbye.\n")
            break
        else:
            print("  Invalid choice. Enter 1-7.")


if __name__ == "__main__":
    main()