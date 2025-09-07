def grade_checker():
    try:
        score = int(input("Enter your score (0-100): "))

        if score < 0 or score > 100:
            print("❌ Invalid input! Please enter a score between 0 and 100.")
            return

        if score >= 90:
            grade = "A"
            message = "🌟 Excellent work! Keep shining."
        elif score >= 80:
            grade = "B"
            message = "👍 Great job! You’re doing really well."
        elif score >= 70:
            grade = "C"
            message = "😊 Good effort! Keep improving."
        elif score >= 60:
            grade = "D"
            message = "💪 You passed! Keep working hard to improve."
        else:
            grade = "F"
            message = "📘 Don’t give up! Learn from mistakes and try again."

        print(f"Your Grade: {grade}")
        print(message)

    except ValueError:
        print("❌ Invalid input! Please enter a number between 0 and 100.")


# Run the program
grade_checker()
