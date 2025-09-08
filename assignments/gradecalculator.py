"""
The program is a grade checker that asks the user to enter a score between 0 and 100.

It uses input validation to make sure the user enters a proper number and that the number is within the valid range.

Based on the score, the program assigns a letter grade (A–F) using conditional statements (if, elif, else).

Alongside the grade, it also provides a motivational message tailored to the student’s performance.

If the user enters an invalid number (like -5, 150, or text like "hello"), the program shows an error message instead of crashing.

The code is wrapped in a function (grade_checker) so it’s neat, reusable, and easy to call.
"""


def grade_checker():
    try:
        score = int(input("Enter your score (0-100): "))

        if score < 0 or score > 100:
            print("Invalid input! Please enter a score between 0 and 100.")
            return

        if score >= 90:
            grade = "A"
            message = "Excellent work! Keep shining."
        elif score >= 80:
            grade = "B"
            message = "Great job! You’re doing really well."
        elif score >= 70:
            grade = "C"
            message = "Good effort! Keep improving."
        elif score >= 60:
            grade = "D"
            message = "You passed! Keep working hard to improve."
        else:
            grade = "F"
            message = "Don’t give up! Learn from mistakes and try again."

        print(f"Your Grade: {grade}")
        print(message)

    except ValueError:
        print("Invalid input! Please enter a number between 0 and 100.")



grade_checker()
