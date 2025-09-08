"""
Student Grade Tracker

The program helps you manage students and their grades. It can:
Add students
Add grades
Calculate averages
Find the top-performing student
Display everything neatly in a table
"""



students = {}  # Dictionary to store student names and grades


def add_student(name):
    """Add a new student with an empty grade list"""
    if name in students:
        print(f"Student '{name}' already exists!")
    else:
        students[name] = []
        print(f"Student '{name}' added successfully.")


def add_grade(name, grade):
    """Add a grade for an existing student"""
    if name not in students:
        print(f"Student '{name}' not found!")
    else:
        students[name].append(grade)
        print(f"Grade {grade} added for '{name}'.")


def calculate_average(name):
    """Calculate the average grade of a student"""
    if name not in students:
        print(f"Student '{name}' not found!")
        return None
    if not students[name]:
        print(f"No grades available for '{name}'.")
        return None
    return sum(students[name]) / len(students[name])


def highest_average():
    """Find the student with the highest average grade"""
    if not students:
        print("No students in the tracker yet.")
        return None
    top_student = None
    top_avg = -1
    for name, grades in students.items():
        if grades:  # only if student has grades
            avg = sum(grades) / len(grades)
            if avg > top_avg:
                top_avg = avg
                top_student = name
    return top_student, top_avg


def display_students():
    """Display all students and their grades in a table"""
    if not students:
        print("No students to display.")
        return
    print("\nStudent Grades:")
    print("-" * 40)
    print(f"{'Name':<15} {'Grades':<15} {'Average'}")
    print("-" * 40)
    for name, grades in students.items():
        avg = calculate_average(name)
        avg_display = f"{avg:.2f}" if avg is not None else "N/A"
        print(f"{name:<15} {str(grades):<15} {avg_display}")
    print("-" * 40)


# Example usage
add_student("Alice")
add_student("Bob")

add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 70)
add_grade("Bob", 75)

display_students()

top_student, top_avg = highest_average()
if top_student:
    print(f"\nTop Student: {top_student} with average {top_avg:.2f}")
