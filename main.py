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

# Function to calculate the average grade for each subject
def calculate_subject_averages(students):
    num_subjects = len(students[0]) - 2  # Exclude Name and Age columns
    averages = []
    for i in range(num_subjects):
        grades = [student[i + 2] for student in students]  # Skip Name and Age
        averages.append(calculate_average(grades))
    return averages

# Load student data
students = load_data('student_grades.csv')

# Define the table headers
headers = ["Name", "Age", "LA", "AI", "OS", "DB", "ML"]

# Print student data
print("Student Data:")
print(tabulate(students, headers=headers, tablefmt="grid"))

# Calculate average grade for each subject
subject_averages = calculate_subject_averages(students)

# Define the table headers for subject averages
avg_headers = ["LA", "AI", "OS", "DB", "ML"]

# Print subject averages
print("\nSubject Averages:")
print(tabulate([subject_averages], headers=avg_headers, tablefmt="grid"))
