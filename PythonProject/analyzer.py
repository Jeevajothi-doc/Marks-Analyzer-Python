# marks_analyzer.py
# Project by Jeevajothi U | B.Sc Maths 2026
# Day 1 Python Intern Task: Read CSV, Find Average, Topper, Filter

import pandas as pd

print("✅ File loaded successfully!")

# Step 1: Read the CSV file
data = pd.read_csv('marks.csv')

print("\n--- All Student Marks ---")
print(data)

# Step 2: Find Class Average for Maths and Python
maths_avg = data['Maths'].mean()
python_avg = data['Python'].mean()

print("\n--- Class Average ---")
print(f"Maths Average: {maths_avg:.2f}")
print(f"Python Average: {python_avg:.2f}")

# Step 3: Find Class Topper
topper_index = data['Total'].idxmax()
topper_name = data.loc[topper_index, 'Name']
topper_marks = data.loc[topper_index, 'Total']

print("\n--- Class Topper ---")
print(f"Name: {topper_name}")
print(f"Total Marks: {topper_marks}")

# Step 4: Filter students who need Python improvement < 70
weak_students = data[data['Python'] < 50][['Name', 'Python']]

print("\n--- Students Need Python Improvement ---")
if weak_students.empty:
    print("Great! No student scored below 70 in Python.")
else:
    print(weak_students)

print("\n--- Analysis Complete ---")
print("Project by Jeevajothi U | B.Sc Maths 2026 | GitHub: github.com/jeevajothi")