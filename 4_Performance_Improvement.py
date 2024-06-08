import csv
from tabulate import tabulate

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to convert numerical grade to letter grade
def grade_to_letter(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    else:
        return 'F'

# Function to load student data from CSV file
def load_data(file):
    data = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            name = row[0]
            age = int(row[1])
            grades = [int(g) for g in row[2:]]
            student = [name, age] + grades
            data.append(student)
    return data

# Load student data
students = load_data('student_grades.csv')

# Calculate average grade for each student and add it to the student data
i = 0
while i < len(students):
    avg_grade = calculate_average(students[i][2:])  # Exclude Name and Age
    students[i].append(avg_grade)
    students[i].append(grade_to_letter(avg_grade))
    i += 1

# Define the table headers
student_headers = ["Name", "Age", "LA", "AI", "OS", "DB", "ML", "Average Marks", "Grade"]

# Print student data in tabular format
print(tabulate(students, headers=student_headers, tablefmt="grid"))