import csv
from tabulate import tabulate

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

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
for student in students:
    avg_grade = calculate_average(student[2:])  # Exclude Name and Age
    student.append(avg_grade)

# Define the table headers
student_headers = ["Name", "Age", "LA", "AI", "OS", "DB", "ML", "Average Marks"]

# Print student data in tabular format
print(tabulate(students, headers=student_headers, tablefmt="grid"))

# Calculate highest and lowest grades for each subject
subjects = ["LA", "AI", "OS", "DB", "ML"]
subject_data = []
for i, subject in enumerate(subjects):
    grades = [student[i + 2] for student in students]  # Skip Name and Age
    subject_data.append([subject, max(grades), min(grades)])

# Define the table headers
subject_headers = ["Subject", "Highest Marks", "Lowest Highest Marks"]

# Print subject data in tabular format
print(tabulate(subject_data, headers=subject_headers, tablefmt="grid"))