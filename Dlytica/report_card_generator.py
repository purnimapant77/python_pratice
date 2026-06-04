# Student report card generator

print("Student report card generator:")
name = input("Enter the name of student:")
roll_no = int(input("Enter roll number of student:"))
print(f"Enter marks of {name} out of 100 in following subject:")
science = float(input("Enter obtained marks in Science:"))
maths = float(input("Enter obtained marks in Maths:"))
computer = float(input("Enter obtained marks in Computer:"))

# Store student details in dictionary
student = {
    "student_name": name,
    "roll_no": roll_no,
    "science": science,
    "maths": maths,
    "computer": computer
}

# Calculate total and percentage
total = science + maths + computer
percentage = total / 3

# Check pass or fail using logical operator
passed = science >= 40 and maths >= 40 and computer >= 40

# Assign grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Distinction remark using nested if and set membership test
remark = "No Distinction"
if passed:
    if grade in {"A+", "A"}:
        remark = "Distinction"

# Final status using ternary operator
status = "PASS" if passed else "FAIL"

# Print report card
print("\n" + "=" * 40)
print("         STUDENT REPORT CARD")
print("=" * 40)
print(f"Student Name : {student['student_name']}")
print(f"Roll Number  : {student['roll_no']}")
print("-" * 40)
print(f"Science      : {science}")
print(f"Maths        : {maths}")
print(f"Computer     : {computer}")
print("-" * 40)
print(f"Total Marks  : {total}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
print(f"Remark       : {remark}")
print(f"Status       : {status}")
print("=" * 40)