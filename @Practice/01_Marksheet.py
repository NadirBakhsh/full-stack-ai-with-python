# Gnerate a marksheet for a student 

# Cover topics:
# 1. Variables
# 2. Numbers
# 3. Calculations (addition, subtraction, multiplication, division, percentage)

# Paper Number out of 100
paper_Number_Math = 100
paper_Number_Science = 100
paper_Number_English = 100
paper_Number_Urdu = 75
paper_Number_Islamic_Studies = 75
paper_Number_Pakistan_Studies = 50
paper_Number_History = 100
paper_Number_Geography = 100

# Total Paper Number
total_Paper_Number = paper_Number_Math + paper_Number_Science + paper_Number_English + paper_Number_Urdu + paper_Number_Islamic_Studies + paper_Number_Pakistan_Studies + paper_Number_History + paper_Number_Geography

# Student Information
student_Name = "Ali"
student_Age = 20
student_Gender = "Male"
student_Class = "10th"
student_Roll_Number = 123456

# Student Marks
student_Marks_Math = 70
student_Marks_Science = 80
student_Marks_English = 90
student_Marks_Urdu = 60
student_Marks_Islamic_Studies = 50
student_Marks_Pakistan_Studies = 40
student_Marks_History = 90
student_Marks_Geography = 60
student_Marks_Computer = 70

# Student Total Marks
student_Total_Marks = student_Marks_Math + student_Marks_Science + student_Marks_English + student_Marks_Urdu + student_Marks_Islamic_Studies + student_Marks_Pakistan_Studies + student_Marks_History + student_Marks_Geography + student_Marks_Computer

# Student Percentage
student_Percentage = (student_Total_Marks / total_Paper_Number) * 100


# Output the marksheet
print(f"Student Name: {student_Name}")
print(f"Student Age: {student_Age}")
print(f"Student Gender: {student_Gender}")
print(f"Student Class: {student_Class}")
print(f"Student Roll Number: {student_Roll_Number}")
print(f"Student Total Marks: {student_Total_Marks}")
print(f"Student Percentage: {student_Percentage}")








