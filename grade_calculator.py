def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"


marks = int(input("Enter marks: "))
grade = calculate_grade(marks)

print("Grade:", grade)
