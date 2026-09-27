def calculate_markgrade(marks):
    if marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

mark = float(input("Enter your marks(0-100): "))
grade = calculate_markgrade(mark)
print(f"Your mark is: {mark}%")
print(f"Your grade is: {grade}") 
